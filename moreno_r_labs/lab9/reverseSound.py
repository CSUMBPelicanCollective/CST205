
def reverseSound(sound):
  target = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
  
  for sample in range(1, getLength(sound)):
    reverseSample = getLength(sound) - sample
    value = getSampleValueAt(sound, reverseSample)
    setSampleValueAt(target, sample, value)
    
  return target
  


file = pickAFile()
sound = makeSound(file)
reversed = reverseSound(sound)
explore(reversed)
play (reversed)
writeSoundTo(reversed, pickAFile())
