#Jason Tse
#Week 3 - Advanced Image Processing Technique

def lineDrawing():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  #convert image to black and white
  for i in pixels:
    average_luminosity = ((getRed(i) + getBlue(i) + getGreen(i))/3)
    setRed(i, average_luminosity)
    setBlue(i, average_luminosity)
    setGreen(i, average_luminosity)
  #convert to line drawing. adjust sensitivity to tweak results
  sensitivity = 10
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      #get current, right, and below pixel. edge cases will default white.
      currentPixel = getPixel(pic, x, y)
      if x + 1 != getWidth(pic):
        rightPixel = getPixel(pic, x + 1, y)
      else:
        rightPixel = getPixel(pic, x , y)
      if y + 1 != getHeight(pic):
        belowPixel = getPixel(pic, x, y + 1)
      else:
        belowPixel = getPixel(pic, x , y)
      #luminosity comparison.
      #each color channel value is the same due to black and white conversion.
      if abs(getRed(currentPixel) - getRed(rightPixel)) > sensitivity and abs(getRed(currentPixel) - getRed(belowPixel)) > sensitivity:
        setColor(currentPixel, black)
      else:
        setColor(currentPixel, white)
  repaint(pic)
  return pic