#Midterm Project
#Pelican Collective Brief Members
#Daniel Howe, Rogelio Moreno, Jiwan Sandhu

######################
# Modifiers of Color #
######################
def shadesTriColor(picture):
  #Apply color transformation to each pixel in for loop
  for x in range (0,getWidth(picture)):
    for y in range (0, getHeight(picture)):
      pixel = getPixel(picture, x, y)
      #Get initial values before setting ignoring red as that is default
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      
      if (y < getHeight(picture) * 1 / 3):
        #print 'Adding blue (0, 48, 87) to upper third'
        rx, gx, bx = ratioRGB(1.0, 48.0, 87.0)
        setRed(pixel, r * rx)
        setGreen(pixel, g * gx)
        setBlue(pixel, b * bx)
        
      elif (y >= getHeight(picture) * 1 / 3 and y <= getHeight(picture) * 2 / 3):
        #print 'Adding green (79, 110, 94) to middle third'
        rx, gx, bx = ratioRGB(79.0, 110.0, 94.0)
        setRed(pixel, r * rx)
        setGreen(pixel, g * gx)
        setBlue(pixel, b * bx)
      
      elif (y >= getHeight(picture) * 2 / 3):
        #print 'Adding sand (132,117,78) to lower third'
        rx, gx, bx = ratioRGB(132.0, 117.0, 78.0)
        setRed(pixel, r * rx)
        setGreen(pixel, g * gx)
        setBlue(pixel, b * bx)
  return(picture)

def ratioRGB(rColour, gColour, bColour):
  maximum = max(rColour, gColour, bColour)
  minimum = min(rColour, gColour, bColour)
  newRedRatio = (rColour - minimum) / (maximum - minimum)
  newGreenRatio = (gColour - minimum) / (maximum - minimum)
  newBlueRatio = (bColour - minimum) / (maximum - minimum)
  return (newRedRatio, newGreenRatio, newBlueRatio)

def betterBnW(pic):
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  return(pic)

def logoPrep(source, target, targetX, targetY):   
  # Copy the source into a target in a given position
  canvas = makeEmptyPicture(getWidth(target), getHeight(target), green)
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      pic_pixel = getPixel(source, x, y)
      pic_pixel_color = getColor(pic_pixel)  
      setColor(getPixel(canvas, x + targetX ,y + targetY), pic_pixel_color)
      
  myFont = makeStyle("Arial", bold, 31)
  addTextWithStyle(canvas, targetX - 1, targetY, "Nothing hOtter", myFont, black)
  addTextWithStyle(canvas, targetX + 1, targetY, "Nothing hOtter", myFont, black)
  myFont = makeStyle("Arial", bold, 30)
  addTextWithStyle(canvas, targetX, targetY, "Nothing hOtter", myFont, red)
  return canvas 

def shrink(picture):
  pic_empty = makeEmptyPicture(getWidth(picture)/2, getHeight(picture)/2)
  
  for x in range(1, getWidth(picture), 2):
    for y in range(1, getHeight(picture), 2):
      pic_pixel = getPixel(picture, x, y)
      pic_pixel_color = getColor(pic_pixel)
      setColor(getPixel(pic_empty, x/2, y/2),pic_pixel_color)
  #repaint(pic_empty)
  #print pic_empty
  return pic_empty


def logoChroma(source, target):
  #dimensional check
  if getWidth(source) > getWidth(target) or getHeight(source) > getHeight(target):
    print "Warning: source dimension is larger than target. operation aborted."
    return
    
  #replace green source pixel with target pixel
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      sPixel = getPixel(source, x, y)
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
        
      #whites
      elif (getGreen(sPixel) > 250 and getRed(sPixel) > 250 and getBlue(sPixel) > 250):
        setColor(sPixel, getColor(tPixel))
  
  #ADD TEXT TO TOP AND CENTER OF PICTURE      
  myFont = makeStyle("Arial", bold, 30)
  addTextWithStyle(source, getWidth(source) / 4, 50, "We are the Sea Otters", myFont, blue)
  
  show(source)
  return(source)
  
def addLogoText(target,size, targetX, targetY):
  myFont = makeStyle("Arial", bold, size + 3)
  addTextWithStyle(target, targetX, targetY - 15, "Nothing hOtter", myFont, black)
  myFont = makeStyle("Arial", bold, size)
  addTextWithStyle(target, targetX, targetY - 15, "Nothing hOtter", myFont, red)
  
def addTopText(target,size, targetX, targetY):
  myFont = makeStyle("Arial", bold, size)
  addTextWithStyle(target, targetX, targetY, "We are the Sea Otters", myFont, blue)

def outLine(pic,threshold):
  # Convert picture to black and white and get dimensions
  pic = betterBnW(pic)
  h = getHeight(pic)
  w = getWidth(pic)
  
  for x in range(0, w-1):
    for y in range(0 , h-1):
      pix = getPixel(pic, x, y)
      rP = getPixel(pic, x+1, y)
      dP = getPixel(pic, x, y+1)
      # we can adjust the values to get desired effect try playing with it
      if abs(getRed(pix)- getRed(rP)) > 2.0 and abs(getRed(pix) - getRed(dP)) > threshold + 2:
        setColor(pix, black)
      else :
        setColor(pix, white)
  
  # Convert to Worhol collage
  effect_warholdPic = effect_warhol(pic)
  return effect_warholdPic

def effect_warhol(pic):
  w= getWidth( pic)
  h= getHeight( pic)
  picNew= makeEmptyPicture(w, h)
  for x in range(0,w/2):
    for y in range (0,h/2):
      px=getPixel(pic,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      # If dark
      if r >0:
        setColor(pxNew,blue)
      # If light
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

####################
# Image management #
####################

def pyCopy(source, target, targetX, targetY):
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
      print 'Working on upper left image'
      pic = (sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 2:
      print 'Working on upper right image'
      pic = (sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = 0
      lastY = getHeight(pic)
    elif i == 3:
      print 'Working on lower left image'
      pic = (sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 4:
      print 'Working on lower right image'
      pic = (sourceImage)
      newImage = pyCopy(pic, newImage, lastX, lastY)
  print 'Completed Warhol collage will now return image..' 
  return newImage

###############
# Main Source #
###############

def csumbRize():
  #CSUMB Logo
  showWarning("Select the CSUMB logo")
  filename = pickAFile()
  logo = makePicture(filename)
  #show(logo)
  
  # PICK A PICTURE FOR THE TARGET
  showWarning("Select the background image")
  file = pickAFile()
  picture = makePicture(file)

  while (getWidth(logo) > getWidth(picture)):
    logo = shrink(logo)
  
  #SET THE LOGO TO BOTTOM RIGHT
  targetX = getWidth(picture) - getWidth(logo)
  targetY = getHeight(picture)- getHeight(logo)
  
  #PREP THE LOGO FOR DESTINATION
  logo = logoPrep(logo, picture, targetX, targetY)
  
  #PLACE LOGO IN PICTURE
  picture = logoChroma(logo, picture)
  
  #ADD COLOR BANDS
  picture = shadesTriColor(picture)
  
  #show(picture)
  showWarning("Save image to new file")
  filenameSave = pickAFile()
  writePictureTo(picture, filenameSave)
  return picture

def warholize():
  showWarning("Pick a file for the Andy Warhol tribute collage source image")
  filename = pickAFile()
  image = makePicture(filename)
  print filename
  image = makeWarhol(image)
  #writePictureTo(image, filename[0-2]+"warHol.jpg")
  #takes the file from make warhol and colorizes/outlines the effect
  #may be we can autmate this part so the end user does't have to pick file again
  #print 'pick the same file just saved with the warhol effect'
  pic = image
  # pic = makePicture( filename[0-2]+"warHol.jpg" )
  # change threshold to effect outline 2.5 to 2.9 seem best
  threshold = 2.9
  newPic = outLine(pic,threshold)
  showWarning("Save image to new file")
  writePictureTo(newPic, pickAFile())
  show(newPic)

#######################
# Implementation Test #
#######################
userInput = requestInteger("Press 1 for CSUMBerize\nPress 2 for Andy Warhol Tribute")
if (userInput == 1):
  csumbRize()
if (userInput == 2):
  warholize()
#(filename + "_result.jpg")
