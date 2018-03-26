#Midterm Project
#Pelican Collective Brief Members
#Daniel Howe, Rogelio Moreno, Jiwan Sandhu

###########################
#NEW CODE USING LAB3 BnW  #
###########################


def betterBnW(pic):
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  return(pic)


def outLine(pic):

  pic = betterBnW(pic)
  h = getHeight(pic)
  w = getWidth(pic)
  
  for x in range(0, w-1):
    for y in range(0 , h-1):
      pix = getPixel(pic, x, y)
      rP = getPixel(pic, x+1, y)
      dP = getPixel(pic, x, y+1)
      # we can adjust the values to get desired effect try playing with it
      if abs(getRed(pix)- getRed(rP)) > 2 and abs(getRed(pix) - getRed(dP)) > 5:
        setColor(pix, black)
      else :
        setColor(pix, white)

  effect_warholdPic=effect_warhol(pic)
  return effect_warholdPic

###########################
#RESOURCE CODE BELOW      #
#WE CAN DELETE IT BEFORE  #
#SUBMITING THE FINAL FILE #
###########################


#def makeOutline(pic):
#  w = getWidth(pic)
#  h = getHeight(pic)
#  picEdge=makeEmptyPicture(w,h)
#  for x in range (0, w-1):
#    for y in range (0, h-1):
#      here=getPixel(picEdge,x,y)
#      down = getPixel(pic,x,y+1)
#      right = getPixel(pic, x+1,y)
#      hereL=(getRed(here)+getGreen(here)+getBlue(here))/3
#      downL=(getRed(down)+getGreen(down)+getBlue(down))/3
#      rightL=(getRed(right)+getGreen(right)+getBlue(right))/3
#      if abs (hereL-downL)>100 and abs(hereL-rightL)>100:
#        setColor(here,black)
#      if abs (hereL-downL)<=100 or abs(hereL-rightL)<=100:
#        setColor(here,white)
#  effect_warholdPic=effect_warhol(pic)
#  return effect_warholdPic

def effect_warhol(pic):
  w= getWidth( pic)
  h= getHeight( pic)
  picNew= makeEmptyPicture(w, h)
  for x in range(0,w/2):
    for y in range (0,h/2):
      px=getPixel(pic,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,blue)
      else:
        setColor(pxNew,yellow)
  for x in range (w/2,w):
    for y in range (h/2,h):
      px=getPixel(pic,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,yellow)
      else:
        setColor(pxNew,blue)

  for x in range(0,w/2):
    for y in range (h/2,h):
      px=getPixel(pic,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,green)
      else:
        setColor(pxNew,red)
  for x in range (w/2,w):
    for y in range (0,h/2):
      px=getPixel(pic,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,red)
      else:
        setColor(pxNew,green)


  return picNew
def pyCopy(source, target, targetX, targetY):
  print 'Starting copy of '
  print source
  print 'To target '
  print target
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      p = getPixel(source, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      if (x + targetX > getWidth(target)) or (y + targetY > getHeight(target)):
        print 'image too large, skipping pixels'
      else:
        newPix = getPixel(target, x + targetX, y + targetY)
        setRed(newPix, r)
        setGreen(newPix, g)
        setBlue(newPix, b)
  #show(newPicture)
  return(target)

    
def makeWarhol(sourceImage):
  #Create new canvas that is 2 x 2 of the original picture size
  width = getWidth(sourceImage) * 2
  height = getHeight(sourceImage) * 2
  newImage = makeEmptyPicture(width, height, black)
  #Store x and y values for the start of the image to track where the next image needs to be placed
  lastX = 0
  lastY = 0
  for i in range(1, 5):
    if i == 1:
      print 'Working on picture: %d' % (i,)

      #randomModifier = random.uniform(0.1, 0.9)
      #pic = artify(sourceImage, randomModifier)
      pic = (sourceImage)

      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 2:
      print 'Working on picture: %d' % (i,)

      #randomModifier = random.uniform(0.1, 0.9)
      #pic = artify(sourceImage, randomModifier)
      pic = (sourceImage)

      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = 0
      lastY = getHeight(pic)
    elif i == 3:
      print 'Working on picture: %d' % (i,)

      #randomModifier = random.uniform(0.1, 0.9)
      #pic = artify(sourceImage, randomModifier)
      pic = (sourceImage)

      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 4:
      print 'Working on picture: %d' % (i,)

      #randomModifier = random.uniform(0.1, 0.9)
      #pic = artify(sourceImage, randomModifier)
      pic = (sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
  print 'Completed Warhol collage will now return image..' 
  #repaint(newImage)
  #writePictureTo(newImage, "/Users/danielhowe/Desktop/collageOutput.jpg")
  return newImage

def test():
  print 'run this function to test the makeWarhol implementation'
  filename = pickAFile()
  image = makePicture(filename)
  image = makeWarhol(image)
  writePictureTo(image, pickAFile())
  #takes the file from make warhol and colorizes/outlines the effect
  #may be we can autmate this part so the end user does't have to pick file again
  print 'pick the same file just saved with the warhol effect'
  pic= makePicture( pickAFile() )
  newPic= outLine(pic )
  show(newPic)

