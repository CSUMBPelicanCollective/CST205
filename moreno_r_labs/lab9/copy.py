



def soundClip(sound, beginClip, endClip):
  sampleRate = int(getSamplingRate(sound))
  print sampleRate
  newClip = makeEmptySound(endClip - beginClip, sampleRate)
  
  index = 0
  for sample in range(beginClip, endClip):
    
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(newClip, index, value)   
    index = index + 1
  
  play(newClip)
  explore(newClip)
  return newClip


def copy(source, target, start):
  index = start
  
  for sample in range(0, getLength(source)):
    value = getSampleValueAt(source, sample)
    setSampleValueAt(target, index, value)
    index = index + 1
    
  return target
  
file = pickAFile()
sound = makeSound(file)
newCopy = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
newSound = copy(sound, newCopy, 0)

play(newSound)
#second clip
#newCopy = makeEmp
#copy(sound, newCopy, getLength(sound))

