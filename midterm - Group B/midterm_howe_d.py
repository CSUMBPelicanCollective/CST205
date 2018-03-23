#Midterm Project
#Pelican Collective Brief Members
#Daniel Howe, Rogelio Moreno, Jiwan Sandhu
#just a comment-jiwan
def artify(sourceImage):
  for x in range(0, getWidth(sourceImage)):
    for y in range(0, getHeight(sourceImage)):
      px = getPixel(sourceImage, x, y)
      red = getRed(px)
      green = getGreen(px)
      blue = getBlue(px)
      
      if red < 64:
        setRed(px, 31)
      elif red > 63 and red < 128:
        setRed(px, 95)
      elif red > 127 and red < 192:
        setRed(px, 159)
      else: # 191 < color < 256
        setRed(px, 223)
      
      if green < 64:
        setGreen(px, 31)
      elif green > 63 and green < 128:
        setGreen(px, 95)
      elif green > 127 and green < 192:
        setGreen(px, 159)
      else: # 191 < color < 256
        setBlue(px, 223)
      
      if blue < 64:
        setBlue(px, 31)
      elif blue > 63 and blue < 128:
        setBlue(px, 95)
      elif blue > 127 and blue < 192:
        setBlue(px, 159)
      else: # 191 < color < 256
        setBlue(px, 223)
  #show(pic)
  #writePictureTo(pic, filename + "_Artified.jpg")
  return(sourceImage)

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
      pic = artify(sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 2:
      print 'Working on picture: %d' % (i,)
      pic = artify(sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = 0
      #lastY = height
      lastY = getWidth(pic)
    elif i == 3:
      print 'Working on picture: %d' % (i,)
      pic = artify(sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 4:
      print 'Working on picture: %d' % (i,)
      pic = artify(sourceImage)
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