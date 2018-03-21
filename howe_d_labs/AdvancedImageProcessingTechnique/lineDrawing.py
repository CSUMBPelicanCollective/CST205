def test():
  # Get user image
  filename = pickAFile()
  picture = makePicture(filename)
  # Get an integer input from user to use as threshold in lineDrawing function later
  lineThreshold = requestNumber("Enter a threshold for converting image to line drawing :")
  while (lineThreshold < 0):
      lineThreshold = requestInteger("Re-enter a threshold for converting image to line drawing greater than 0:")
  # Convert image to black and white
  picture = betterBnW(picture)
  # Convert image to line drawing
  picture = lineDrawing(picture, lineThreshold)
  show(picture)
  writePictureTo(picture, pickAFile())
  print 'Done'

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