#Jason Tse
#Lab 8

#Input: sound object
#Output: sound object
#Function: doubles volume
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
  return sound
  
#Input: sound object
#Output: sound object
#Function: halves volume
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)
  return sound
  
#Input: sound object, int value
#Output: sound object
#Function: increase sound by given factor
def decreaseVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)
  return sound
    
#Input: sound object
#Output: integer value
#Function: returns loudest sound sample value
def maxSample(sound):
  #initialize with highest sample variable
  #use abs() to convert negative values
  highestSampleValue = abs(getSampleValueAt(sound, 0))
  for sample in getSamples(sound):
    highestSampleValue = max(highestSampleValue, abs(getSampleValue(sample)))
  return highestSampleValue

# --------- THE FUNCTIONS BELOW ONLY WORK WITH 16-BIT SOUNDS --------- #
            
#Input: sound object
#Output: sound object
#Function: returns normalized sound
def maxVolume(sound):
  #find highest sample value
  factor = maxSample(sound)
  for sample in getSamples(sound):
    #32767 is the largest possible sample value
    #dividing the maximum by a factor will give the complementary factor
    normalizedValue = getSampleValue(sample) * 32767 / factor
    setSampleValue(sample, normalizedValue)
  return sound
    
#Input: sound object
#Output: sound object
#Function: positive and negative sample values are set to respective maximums
def goToEleven(sound):
  for sample in getSamples(sound):
    if getSampleValue(sample) > 0:
      setSampleValue(sample, 32767)
    elif getSampleValue(sample) < 0:
      setSampleValue(sample, -32768)
    #0 values remain at 0
    #Sound should still be audible because the frequency is unchanged; only the amplitude is changed.
  return sound