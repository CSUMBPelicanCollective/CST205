#Jason Tse
#Lab 9

#PROBLEM 1
#Input: sound object, integer, integer
#Output: sound object
#Function: Clips audio from specified start to end
def clip(source, start, end):
  #make sound object to fit clip with matching sampling rate.
  clippedSound = makeEmptySound(end - start, int(getSamplingRate(source)))
  #copy samples to sound object
  for index in range(start, end):
    inputValue = getSampleValueAt(source, index)
    #(index - start) gives us index starting at 0 for clipped sound
    outputSample = getSampleObjectAt(clippedSound, index - start)
    setSampleValue(outputSample, inputValue)
  
  return clippedSound
    
#PROBLEM 2
#Input: sound object, sound object, integer
#Output: sound object
#Function: Appends source sound to target sound at given start index
def copy(source, target, start):
  #make new sound object to fit resulting sound
  totalSamples = start + getNumSamples(source)
  copySound = makeEmptySound(totalSamples, int(getSamplingRate(target)))
  #copy target into new sound
  for index in range(0, start):
    inputValue = getSampleValueAt(target, index)
    outputSample = getSampleObjectAt(copySound, index)
    setSampleValue(outputSample, inputValue)
  #copy source into new sound after target
  for index in range(start, totalSamples):
    inputValue = getSampleValueAt(source, index - start)
    outputSample = getSampleObjectAt(copySound, index)
    setSampleValue(outputSample, inputValue)
  
  return copySound
  
#PROBLEM 3
#Input: none
#Output: sound object
#Function: Selects media folder and makes collage from 5 specific clips
def clipCollage():
  #set media folder
  setMediaFolder(pickAFolder())
  #get media files
  clip1 = makeSound("button.wav")
  clip2 = makeSound("countTo3.wav")
  clip3 = makeSound("DNA.wav")
  clip4 = makeSound("frog.wav")
  clip5 = makeSound("dinosaur.wav")
  #create half second of silence
  silence = makeEmptySound(int(getSamplingRate(clip1)*0.5), int(getSamplingRate(clip1)))
  #append clips to clip 1
  clip1 = copy(clip2, clip1, getNumSamples(clip1))
  clip1 = copy(silence, clip1, getNumSamples(clip1))
  clip1 = copy(clip3, clip1, getNumSamples(clip1))
  clip1 = copy(silence, clip1, getNumSamples(clip1))
  clip1 = copy(clip4, clip1, getNumSamples(clip1))
  clip1 = copy(silence, clip1, getNumSamples(clip1))
  clip1 = copy(clip5, clip1, getNumSamples(clip1))
  
  return clip1

#PROBLEM 4
#Input: sound object
#Output: sound object
#Function: Revereses sound object
def reverse(sound):
  #make new sound object
  reversed = makeEmptySound(getNumSamples(sound), int(getSamplingRate(sound)))
  #copy sound backwards into new sound object
  for index in range(0, getNumSamples(sound)):
    reversedIndex =  getNumSamples(sound) - index - 1  #(-1) is use to normalize length to index value
    inputValue = getSampleValueAt(sound, reversedIndex)
    outputSample = getSampleObjectAt(reversed, index)
    setSampleValue(outputSample, inputValue)
  
  return reversed