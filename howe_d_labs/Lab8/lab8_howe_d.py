######################
# Select File Helper #
######################
def selectSoundFile():
  filename = pickAFile()
  soundFile = makeSound(filename)
  return (soundFile)
  
##############################
#   Change and Inspect Vol   #
##############################
def changeVolume(sound, factor):
  # Increase sound of whole clip by factor
  print 'Increasing sound by a factor of ' + str(factor)
  for i in range (0, getLength(sound)):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, soundValue * factor)
  return sound
  
def halfAndHalf(sound, factor):
  # Modify first half of sound clip to increase sound by factor
  print 'Increasing sound by a factor of ' + str(factor) + ' for the first half of the sound'
  for i in range (0, getLength(sound) / 2):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, soundValue * factor)
  # Modify second half of sound clip to decrease sound by factor  
  print 'Decreasing sound by a factor of ' + str(factor) + ' for the first half of the sound'
  for i in range (getLength(sound) / 2, getLength(sound)):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, soundValue / factor)
  return sound
  
def decreaseVolume(sound):
  # Decrease sound of whole clip by half
  print 'Decreasing sound by half'
  for i in range (0, getLength(sound)):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, soundValue / 2)
  return sound

def maxSample(sound):
  maxVal = 0
  for i in range (0, getLength(sound)):
    # Determine the max value of the sound file and save it
    maxVal = max(getSampleValueAt(sound, i), maxVal)
  print 'Max value for the provided sound clip is ' + str(maxVal)
  print 'Max value possible is 32767'
  return maxVal

def maxVolume(sound):
  # Determine the max value and determine the factor to increase the whole sound clip to the max volume possible
  factor = 32767.0 / maxSample(sound)
  print 'Changing sound by a factor of ' + str(factor)
  sound = changeVolume(sound, factor)
  return sound
  
def goToEleven(sound):
  for i in range (0, getLength(sound)):
    soundValue = getSampleValueAt(sound, i)
    if (soundValue > 0):
      setSampleValueAt(sound, i, 32767)
    elif (soundValue < 0):
      setSampleValueAt(sound, i, -32767)
  return sound

##################
# Combine Sounds #
##################  
def combineSounds(startSound, endSound):
  if ( getSamplingRate(startSound) !=  getSamplingRate(endSound)):
    print 'Mismatched sample rate'
    return
  # Create new sound file that is the length of the two parameters, or sound objects
  newSound = makeEmptySound(getLength(startSound) + getLength(endSound), getSamplingRate(startSound))
  newSoundIndex = 0
  # Copy both sounds to the new sound object
  for i in range (0, getLength(startSound)):
    soundValue = getSampleValueAt(startSound, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  for i in range (0, getLength(endSound)):
    soundValue = getSampleValueAt(endSound, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  return newSound