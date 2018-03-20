#Pelican Collective
#Lab 6

#WARM UP
def redEyeReducer():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for i in pixels:
    #Adjust distance for tolerance
    if distance(cyan, getColor(i)) > 320:
      #Adjust denominator for reduction amount
      setRed(i, getRed(i)/4)
      #for crazy color/debugging
      #setColor(i, green)
  show(pic)
  writePictureTo(pic, filename + "_redEye.jpg")
  return pic

# PROBLEM 1
def betterBnW(pic):
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  return(pic)
  
def sepia():
  filename = pickAFile()
  pic = betterBnW(makePicture(filename))
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      px = getPixel(pic, x, y)
      red = getRed(px)
      blue = getBlue(px)
      if red < 63:
        setRed(px, red * 1.1)
        setBlue(px, blue * 0.9)
      elif red > 62 and red < 192:
        setRed(px, red * 1.15)
        setBlue(px, blue * 0.85)
      elif red > 191 and red < 236:
        setRed(px, red * 1.08)
        setBlue(px, blue * 0.93)
      else:
        setRed(px, 255)
        setBlue(px, blue * 0.93)
  show(pic)
  writePictureTo(pic, filename + "_Sepia.jpg")
  return(pic)
  
# PROBLEM 2
def artify():
  filename = pickAFile()
  pic = makePicture(filename)
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      px = getPixel(pic, x, y)
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
  show(pic)
  writePictureTo(pic, filename + "_Artified.jpg")
  return(pic)
  
#PROBLEM 3
#source is the keyed image, target is the background
def chromakey():
  filename = pickAFile()
  source = makePicture(filename)
  filename = pickAFile()
  target = makePicture(filename)
  #dimensional check
  if getWidth(source) > getWidth(target) or getHeight(source) > getHeight(target):
    print "Warning: source dimension is larger than target. operation aborted."
    return
  #replace green source pixel with target pixel
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      sPixel =  getPixel(source, x, y)
      tPixel = getPixel(target, x, y)
      #midtone greens
      if getGreen(sPixel) > 95 and getRed(sPixel) < 80:
        setColor(sPixel, getColor(tPixel))
      #shadow greens
      elif getGreen(sPixel) > 60 and getRed(sPixel) < 50 and getBlue(sPixel) < 65:
        setColor(sPixel, getColor(tPixel))
      #highlight greens
      elif getGreen(sPixel) > 150 and getRed(sPixel) < 95 and getBlue(sPixel) < 95:
        setColor(sPixel, getColor(tPixel))
  show(source)
  writePictureTo(source, filename + "_chromakey.jpg")
  return(source)