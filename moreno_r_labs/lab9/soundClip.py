#Rocky Moreno
#Lab 9 Sound Clip


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
  
  
  
file = pickAFile()
sound = makeSound(file)

#print getSamplingRate(sound)
#beginIndex = 23452
endingIndex = 35014

#play(soundClip(sound,beginIndex,endingIndex))
explore(sound)


    