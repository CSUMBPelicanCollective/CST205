#Jason Tse
#Lab 5


#WARM UP
def expandCanvas():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getWidth(pic)*3/2, getHeight(pic)*3/2)
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      inPixel = getPixel(pic, x, y)
      outPixel = getPixel(newPic, x + getWidth(pic)/4, y + getHeight(pic)/4)
      setColor(outPixel, getColor(inPixel))
  show(newPic)
  return newPic


#PROBLEM 1
def pyCopy(source, target, targetX, targetY):
  #check for out of bounds
  if (getWidth(source) + targetX) > getWidth(target) or (getHeight(source) + targetY) > getHeight(target):
    print "Warning: The source does not fit in target bounds!"
    return
  #copy if fits  
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      inPixel = getPixel(source, x, y)
      outPixel = getPixel(target, x + targetX, y + targetY)
      setColor(outPixel, getColor(inPixel))
  return target


#PROBLEM 2
#---------------- BEGIN image manipulators ----------------- 
def mirror_quad(pic):
  for x in range (0, getWidth(pic)/2):
    for y in range (0, getHeight(pic)/2):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, getWidth(pic) - x - 1, y)
      setColor(outputPixel, getColor(inputPixel))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)/2):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, x, getHeight(pic) - y - 1)
      setColor(outputPixel, getColor(inputPixel))      
  return pic
  
def makeNegative(pic):
  pixels = getPixels(pic)
  for i in pixels:
    setRed(i, 255 - getRed(i))
    setBlue(i, 255 - getBlue(i))
    setGreen(i, 255 - getGreen(i))
  return pic

def moreRed(pic, more_percent):
  pixels = getPixels(pic)
  for i in pixels:
    redness = getRed(i)*(1 + more_percent/100)
    if redness > 255:
      redness = 255
    setRed(i, redness)
  return pic

def roseColoredGlasses(pic):
  pixels = getPixels(pic)
  for i in pixels:
    setGreen(i, (getRed(i) + getBlue(i) + getGreen(i))/3)
    setRed(i, 255)
    setBlue(i, 255)
  return pic
  
def rotatePic(pic):
  newPic = makeEmptyPicture(getHeight(pic), getWidth(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      inPixel = getPixel(pic , x, y)
      outPixel = getPixel(newPic, y, getHeight(newPic) - x -1)
      setColor(outPixel, getColor(inPixel))
  return newPic
  
def lessRed(pic, less_percent):
  pixels = getPixels(pic)
  for i in pixels:
    setRed(i, getRed(i)*(1 - less_percent/100))
  return pic
  
def BnW(pic):
  pixels = getPixels(pic)
  for i in pixels:
    average_intensity = (getRed(i) + getBlue(i) + getGreen(i)) / 3
    setRed(i, average_intensity)
    setBlue(i, average_intensity)
    setGreen(i, average_intensity)
  return(pic)
#---------------- END image manipulators ----------------- 

def makeCollage():
  #5x7 inch blank used
  collage = makeEmptyPicture(1500, 2100)
  #Establish media folder
  print "Select the folder of images. "
  setMediaFolder()
  #Collage images with pyCopy
  pic = mirror_quad(makePicture("quad_mirror.jpg"))
  pyCopy(pic, collage, 0, 0)
  
  pic = makeNegative(makePicture("negative.jpg"))
  pyCopy(pic, collage, 0, 1332)
  
  pic = moreRed(makePicture("moreRed255.jpg"), 255)
  pyCopy(pic, collage, 0, 711)
  
  pic = roseColoredGlasses(makePicture("rose_colored.jpg"))
  pyCopy(pic, collage, 476, 1332)
  
  pic = rotatePic(makePicture("rotated.jpg"))
  pyCopy(pic, collage, 732, 768)
  
  pic = lessRed(makePicture("lessRed255.jpg"), 255)
  pyCopy(pic, collage, 260, 0)
  
  pic = makePicture("tea_set.jpg")
  pyCopy(pic, collage, 388, 475)
  
  pic = rotatePic(BnW(makePicture("rotatedBnW.jpg")))
  pyCopy(pic, collage, 732, 0)
  
  #Save output
  print "Save the collage."
  writePictureTo(collage, pickAFile())
  show(collage)