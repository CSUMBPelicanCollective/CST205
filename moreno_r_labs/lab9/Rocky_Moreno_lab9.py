#Rocky Moreno
#lab9

###############################################
#       SOUNDCLIP FUNCTION                    #
#       THIS IS CLIP FUNCTION PROBLEM 1       #
###############################################
def soundClip(sound, beginClip, endClip):
  sampleRate = int(getSamplingRate(sound))
  #print sampleRate
  newClip = makeEmptySound(endClip - beginClip, sampleRate)
  
  index = 0
  for sample in range(beginClip, endClip):    
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(newClip, index, value)   
    index = index + 1

  return newClip

#############################
#       COPY FUNCTION       #
#       PROBLEM 2           #
#############################
def copy(source, target, start):
  # IF NEW CLIP START AT 0 ELSE HOLD CURRENT CLIP, MAKE NEW EMPTY SOUND THEN COMBINE
  if start == 0:  
    index = start  
    for sample in range(0, getLength(source)):
      value = getSampleValueAt(source, sample)
      setSampleValueAt(target, index, value)
      index = index + 1
    return target 
  else:
    targetHold = target  
    newTarget = makeEmptySound(getLength(targetHold) + getLength(source), int(getSamplingRate(source)))
    #COMBINING SOUNDS
    index = 0
    for sample in range(0, getLength(targetHold)):
      value = getSampleValueAt(targetHold, sample)
      setSampleValueAt(newTarget, index, value)
      index = index + 1
          
    for sample in range(0, getLength(source)):
      value = getSampleValueAt(source, sample)
      setSampleValueAt(newTarget, index, value)
      index = index + 1
        
  return newTarget

    
            
##############################
##############################          
#THIS WAS USED TO CREATE CLIPS

#file = pickAFile()
#sound = makeSound(file)
#def soundClip(sound, beginClip, endClip):

#explore(sound)
#beginClip = 307458
#endClip = 906192
#newSoundClip = soundClip(sound, beginClip, endClip)

#writeSoundTo(newSoundClip, pickAFile())
###############################
###############################
 
   
  
#############################
#       SOUND COLLAGE       #
#         PROBLEM 3         #
############################# 
def soundCollage():  
  file = pickAFile()
  sound1 = makeSound(file)
  newCopy = makeEmptySound(getLength(sound1),int(getSamplingRate(sound1)))
  newSound1 = copy(sound1, newCopy, 0)

  file = pickAFile()
  sound2 = makeSound(file)
  newSound2 = copy(sound2, newSound1, getLength(newSound1))

  file = pickAFile()
  sound3 = makeSound(file)
  newSound3 = copy(sound3, newSound2, getLength(newSound2))

  file = pickAFile()
  sound4 = makeSound(file)
  newSound4= copy(sound4, newSound3, getLength(newSound3))

  file = pickAFile()
  sound5 = makeSound(file)
  newSound5 = copy(sound5, newSound4, getLength(newSound4))

  return(newSound5)

#############################  
#       REVERSE SOUND       #
#         PROBLEM 4         #
#############################
def reverseSound(sound):
  target = makeEmptySound(getLength(sound), int(getSamplingRate(sound)))
  
  # MAKE VARIABLE THAT COUNTS BACKWARDS AS SAMPLE COUNTS FORWARD
  for sample in range(1, getLength(sound)):
    reverseSample = getLength(sound) - sample
    value = getSampleValueAt(sound, reverseSample)
    setSampleValueAt(target, sample, value)
    
  return target
 
############################################
############################################ 
# FUNCTION CALL AND WRITE TO FILE FOR COLLAGE 
writeSoundTo(soundCollage(), pickAFile())
#explore(soundCollage())