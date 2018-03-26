#Volume Increase
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSample(sample)
    setSampleValue(sample, value * 2 )
    
  play(sound)

file = pickAFile()
soundFile = makeSound(file)
increaseVolume(soundFile)

#Volume Decrease
def decreaseVolume(sound):
  explore(sound)
  for sample in getSamples(sound):
    value = getSample(sample)
    setSampleValue(sample, value / 2 )
    
  explore(sound)

file = pickAFile()
soundFile = makeSound(file)
decreaseVolume(soundFile)



# change Volume
def changeVolume(sound, volume, factor):
  if (factor == 0):
    return sound
  elif (volume == "increase"):
    #explore(sound)
    for sample in getSamples(sound):
      value = getSample(sample)
      setSampleValue(sample, value * factor )
  else:
    #explore(sound)
    #decrease sound
    for sample in getSamples(sound):
      value = getSample(sample)
      setSampleValue(sample, value / factor )
    #explore(sound)  
  #play(sound)
  return(sound)

#Pick a file
file = pickAFile()
soundFile = makeSound(file)

#Choose to increase or decrease and by how much
volume = raw_input("increase or decrease: ")
factor = int(raw_input("by how much: "))

#Function Call and play it
play(changeVolume(soundFile, volume, factor))






#lab 8 max sample
def maxSample(sound):
  maxNumber  = 0
  newMax = 0

  for x in range(1,getLength(sound)):
    valueX = getSampleValueAt(sound, x - 1)   
    valueY = getSampleValueAt(sound, x)
    newMax = max(valueX, valueY)
    
    if maxNumber < newMax:
      maxNumber = newMax
      position = x
      
  #print "postion " 
  #print position
  return maxNumber
 



#goToEleven Function
def goToEleven(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767 - value)
    elif value < 0:
      setSampleValue(sample, abs(value) - 32678)
  explore(sound)
  return sound

file = pickAFile()
sound = makeSound(file)

play(goToEleven(sound))



