#Jason Tse
#Lab 3

#Warmup 1
def halfRed():
  lessRed(50)

#Warmup 2
def noBlue():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    setBlue(i, 0)
  return(pic)

#Problem 1
def lessRed(less_percent):
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    setRed(i, ((getRed(i)*(100 - less_percent))/100))
  return(pic)
  
#Problem 2
def moreRed(more_percent):
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    redness = getRed(i) + ((getRed(i) * more_percent)/100)
    if redness > 255:
      redness = 255
    setRed(i, redness)
  return(pic)

#Problem 3
def roseColoredGlasses():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    setGreen(i, (getRed(i) + getBlue(i) + getGreen(i))/3)
    setRed(i, 255)
    setBlue(i, 255)
  return(pic)

#Problem 4
def lightenUp():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    setColor(i, makeLighter(getColor(i)))
  return(pic)

#Problem 5
def makeNegative():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    setRed(i, 255 - getRed(i))
    setBlue(i, 255 - getBlue(i))
    setGreen(i, 255 - getGreen(i))
  return(pic)

#Problem 6
def BnW():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    average_intensity = (getRed(i) + getBlue(i) + getGreen(i)) / 3
    setRed(i, average_intensity)
    setBlue(i, average_intensity)
    setGreen(i, average_intensity)
  return(pic)


def betterBnW():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  return(pic)
    
