#Midterm Project
#Pelican Collective Brief Members
#Daniel Howe, Rogelio Moreno, Jiwan Sandhu

import random
import time
# Make the numbers random
random.seed(time.time())

def lineDrawing(pic, threshold):
  print 'Converting image to line drawing with a threshold of %d' % (threshold,)
  # Begin searching image for pixels that match the condition: 
  # If there is a large enough difference to find the difference, 
  # subtract and use the abs function to get the absolute value in the 
  # luminance between your pixel and BOTH the pixels to the right and below,
  # then make your pixel black.  Otherwise, make your pixel white
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      # Get the current pixel and store colors
      px = getPixel(pic, x, y)
      red = getRed(px)
      green = getGreen(px)
      blue = getBlue(px)
      currentLuminosity = red * 0.299 + blue * 0.114 + green * 0.587
      if (x + 1 < getWidth(pic)):
        # Get the pixel to the right and store colors
        px = getPixel(pic, x + 1, y)
        red = getRed(px)
        green = getGreen(px)
        blue = getBlue(px)
        leftLuminosity = red * 0.299 + blue * 0.114 + green * 0.587
        if (y + 1 < getHeight(pic)):
          # Get the pixel below and store colors 
          px = getPixel(pic, x, y + 1)
          red = getRed(px)
          green = getGreen(px)
          blue = getBlue(px)
          bottomLuminosity = red * 0.299 + blue * 0.114 + green * 0.587
          if (abs(bottomLuminosity - currentLuminosity) > threshold and abs(leftLuminosity - currentLuminosity) > threshold):
            # Get current x,y pixel
            px = getPixel(pic, x, y)
            # Set pixel to black
            setRed(px, 0)
            setGreen(px, 0)
            setBlue(px, 0)
      else:
        # Either the for loop has reached the edge of the image or non of the conditions were matched above
        # Set the pixel to white
        px = getPixel(pic, x, y)
        setRed(px, 255)
        setGreen(px, 255)
        setBlue(px, 255)
  return(pic)
      
def betterBnW(pic):
  print 'Converting image to black and white'
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  return(pic)

def artify(sourceImage):
  for x in range(0, getWidth(sourceImage)):
    for y in range(0, getHeight(sourceImage)):
      px = getPixel(sourceImage, x, y)
      red = getRed(px)
      green = getGreen(px)
      blue = getBlue(px)
      ran = random.random()
      ran = ran + 1
      if red < 64:
        # Use modifier in the second argument below
        setRed(px, 31 * ran)
      elif red > 63 and red < 128:
        setRed(px, 95 * ran)
      elif red > 127 and red < 192:
        setRed(px, 159 * ran)
      else: # 191 < color < 256
        setRed(px, 223)
      
      if green < 64:
        setGreen(px, 31 * ran)
      elif green > 63 and green < 128:
        setGreen(px, 95 * ran)
      elif green > 127 and green < 192:
        setGreen(px, 109 * ran)
      else: # 191 < color < 256
        setBlue(px, 223)
      
      if blue < 64:
        setBlue(px, 31 * ran)
      elif blue > 63 and blue < 128:
        setBlue(px, 95 * ran)
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
  for i in range(1, 3):
    if i == 1:
      print 'Working on picture: %d' % (i,)
      pic1 = artify(sourceImage)
      newImage = pyCopy(pic1, newImage, lastX, lastY)
      lastX = getWidth(pic1) + lastX
    elif i == 2:
      print 'Working on picture: %d' % (i,)
      pic2 = artify(sourceImage)
      newImage = pyCopy(pic2, newImage, lastX, lastY)
      lastX = 0
      lastY = getHeight(pic2)
    elif i == 3:
      print 'Working on picture: %d' % (i,)
      pic3 = artify(sourceImage)
      newImage = pyCopy(pic3, newImage, lastX, lastY)
      lastX = getWidth(pic3) + lastX
    elif i == 4:
      print 'Working on picture: %d' % (i,)
      pic4 = artify(sourceImage)
      newImage = pyCopy(pic4, newImage, lastX, lastY)
  print 'Completed Warhol collage will now return image..' 
  return newImage

def test():
  print 'run this function to test the makeWarhol implementation'
  filename = pickAFile()
  image = makePicture(filename)
  image = betterBnW(image)
  image = lineDrawing(image, 0.9)
  newImage = makeWarhol(image)
  writePictureTo(newImage, pickAFile())
