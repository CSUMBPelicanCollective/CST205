######################
# Select File Helper #
######################
def selectSoundFile():
  filename = pickAFile()
  soundFile = makeSound(filename)
  return (soundFile)
  
##################
#  Clip Sound    #
##################
def clip(sound, start, end):
  # Make a new sound that is the clipped length
  newSound = makeEmptySound(end - start, int(getSamplingRate(sound)))
  newSoundIndex = 0
  # Copy both sounds to the new sound object
  for i in range (start, end):
    soundValue = getSampleValueAt(startSound, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  return newSound

############################
# Modify and Create Sounds #
############################
def createSilence(time, sampleRate):
  newSound = makeEmptySound(time, sampleRate)
  for i in range (0, time):
    setSampleValueAt(newSound, i, 0)
  return newSound
  
def reverse(sound):
  newSound = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
  # Store the end of the sound index for sampling, this will get modified in for loop
  soundIndex = int(getLength(sound)) - 1
  for i in range (0, getLength(sound) - 1):
    soundValue = getSampleValueAt(sound, soundIndex)
    setSampleValueAt(newSound, i, soundValue)
    # Work backwards from end, subtract one from sampling index
    soundIndex = soundIndex - 1
  return newSound
  
def changeVolume(sound, factor):
  # Increase sound of whole clip by factor
  print 'Increasing sound by a factor of ' + str(factor)
  for i in range (0, getLength(sound)):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, soundValue * factor)
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
  
##################
# Combine Sounds #
##################  
def combineSounds(startSound, endSound):
  #if ( getSamplingRate(startSound) !=  getSamplingRate(endSound)):
    #print 'Mismatched sample rate'
    #return
  # Create new sound file that is the length of the two parameters, or sound objects
  newSound = makeEmptySound(getLength(startSound) + getLength(endSound), int(getSamplingRate(startSound)))
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
  
def copy(sound, target, start):
  # Make a new sound object that is the required length
  print 'Creating new sound ' + str(getLength(sound) + getLength(target))
  newSound = makeEmptySound(getLength(sound) + getLength(target), int(getSamplingRate(sound)))
  newSoundIndex = 0
  targetSoundIndex = 0
  
  print 'Copying differencial in target to new sound from %d to %d' % (0, start)
  for i in range (0, start):
    soundValue = getSampleValueAt(target, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
    targetSoundIndex = targetSoundIndex + 1
  
  print 'Splicing provided sound from %d into new sound clip at %d' % (start, getLength(sound) + start - 1)
  for i in range (0, getLength(sound) - 1):
    soundValue = getSampleValueAt(sound, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  
  print 'Copying remaining sound from %d to %d to new sound at %d' % (targetSoundIndex, getLength(target) - 1, newSoundIndex)
  for i in range (targetSoundIndex, getLength(target) - 1):
    soundValue = getSampleValueAt(target, i)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  return newSound
  
def collageSound():
  numberOfSamples = 5
  newSoundCollage = makeEmptySound(1, 44100)
  for request in range (0, numberOfSamples):
    newSoundProvided = selectSoundFile()
    # Increase volume to max for every sample
    newSoundProvided = maxVolume(newSoundProvided)
    # Add some silence at the beginning of sound for clip
    silenceTime = int(0.1 * getSamplingRate(newSoundProvided))
    silenceSampleRate = int(getSamplingRate(newSoundProvided))
    newSoundProvided = combineSounds(createSilence(int(0.1 * getSamplingRate(newSoundProvided)), int(getSamplingRate(newSoundProvided))), newSoundProvided)
    if (request == 0):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, 0)
    if (request == 1):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, getLength(newSoundCollage) / 1)
    if (request == 2):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, getLength(newSoundCollage) / 2)
    if (request == 3):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, getLength(newSoundCollage) / 3)
    if (request == 4):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, getLength(newSoundCollage) / 4)
    if (request == 5):
      newSoundCollage = copy(newSoundProvided, newSoundCollage, getLength(newSoundCollage) / 5)
  explore(newSoundCollage)
  print 'Choose where to save the collage'
  writeSoundTo(newSoundCollage, pickAFile())
  print 'For kicks we will reverse it and save it '
  newSoundCollage = reverse(newSoundCollage)
  writeSoundTo(newSoundCollage, pickAFile())
  
def collageSoundSpliced():
  numberOfSamples = 5
  newSoundCollage = makeEmptySound(1, 44100)
  for request in range (0, numberOfSamples):
    newSoundProvided = selectSoundFile()
    # Increase volume to max for every sample
    newSoundProvided = maxVolume(newSoundProvided)
    # Add some silence at the beginning of sound for clip
    silenceTime = int(0.1 * getSamplingRate(newSoundProvided))
    silenceSampleRate = int(getSamplingRate(newSoundProvided))
    newSoundProvided = combineSounds(createSilence(int(0.1 * getSamplingRate(newSoundProvided)), int(getSamplingRate(newSoundProvided))), newSoundProvided)
    if (request % 2):
      newSoundCollage = combineSounds(newSoundProvided, newSoundCollage)
    else:
      newSoundCollage = combineSounds(newSoundCollage, newSoundProvided)
  explore(newSoundCollage)
  print 'Choose where to save the collage'
  writeSoundTo(newSoundCollage, pickAFile())
  print 'For kicks we will reverse it and save it '
  newSoundCollage = reverse(newSoundCollage)
  writeSoundTo(newSoundCollage, pickAFile())