#Jason Tse
#Lab 4


#PROBLEM 1
#range(a,b) goes up to b-1. 
#inputPixel goes according to range. 
#outputPixel must subtract 1 from mirrored axis for correct indexing. 

def vertical_mirror(): #mirrors left to right half
  pic = makePicture(pickAFile())
  for x in range (0, getWidth(pic)/2):
    for y in range (0, getHeight(pic)):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, getWidth(pic) - x - 1, y)
      setColor(outputPixel, getColor(inputPixel))
  show(pic)
  return pic 

def mirror_top(): #mirrors top to bottom half
  pic = makePicture(pickAFile())
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)/2):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, x, getHeight(pic) - y - 1)
      setColor(outputPixel, getColor(inputPixel))
  show(pic)
  return pic 

def mirror_bottom(): #mirrors bottom to top half
  pic = makePicture(pickAFile())
  for x in range (0, getWidth(pic)):
    for y in range (getHeight(pic)/2, getHeight(pic)):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, x, getHeight(pic) - y - 1)
      setColor(outputPixel, getColor(inputPixel))
  show(pic)
  return pic  

def mirror_quad(): #mirrors left vertically, then top half horizontally
  pic = makePicture(pickAFile())  
  for x in range (0, getWidth(pic)/2):
    for y in range (0, getHeight(pic)):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, getWidth(pic) - x - 1, y)
      setColor(outputPixel, getColor(inputPixel))

  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)/2):
      inputPixel = getPixel(pic, x, y)
      outputPixel = getPixel(pic, x, getHeight(pic) - y - 1)
      setColor(outputPixel, getColor(inputPixel))      
  show(pic)
  return pic 


#PROBLEM 2
def simpleCopy():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      inPixel = getPixel(pic , x, y)
      outPixel = getPixel(newPic, x, y)
      setColor(outPixel, getColor(inPixel))
  show(newPic)
  return newPic 


#PROBLEM 3
def rotatePic():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getHeight(pic), getWidth(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      inPixel = getPixel(pic , x, y)
      outPixel = getPixel(newPic, y, getHeight(newPic) - x -1)
      setColor(outPixel, getColor(inPixel))
  show(newPic)
  return newPic 


#PROBLEM 4
def shrinkPic():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getWidth(pic)/2, getHeight(pic)/2)
  for x in range (1, getWidth(pic), 2):
    for y in range (1, getHeight(pic), 2):
      inPixel = getPixel(pic , x, y)
      outPixel = getPixel(newPic, x / 2, y / 2)
      setColor(outPixel, getColor(inPixel))
  show(newPic)
  return newPic 