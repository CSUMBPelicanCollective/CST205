
def logoPrep(source, target, targetX, targetY):   
  # Copy the source into a target in a given position
  canvas = makeEmptyPicture(getWidth(target), getHeight(target), green)
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      pic_pixel = getPixel(source, x, y)
      pic_pixel_color = getColor(pic_pixel)  
      setColor(getPixel(canvas, x + targetX ,y + targetY), pic_pixel_color)
  font_color = makeColor(255,153,51)    
  myFont = makeStyle("Arial", bold, 30)
  addTextWithStyle(canvas, targetX, targetY, "Nothing hOtter", myFont, font_color)
  
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
  
  #ADD TEXT TO TOP AND CENTER OF PICTURE
  fontColor = makeColor(204,238,255)   
  myFont = makeStyle("Arial", bold, 20)
  addTextWithStyle(source, getWidth(source) / 4, 50, "We are the Sea Otters", myFont, white)
  #addTextWithStyle(source, (getWidth(source) / 4)+1, 51, "We are the Sea Otters", myFont, white)
  
  show(source)
  return(source)
  
def usersPicture():
  #CSUMB Logo
  print 'Select the CSUMB logo'
  filename = pickAFile()
  logo = makePicture(filename)
  #show(logo)
  
  # PICK A PICTURE FOR THE TARGET
  print 'Select the destination image'
  file = pickAFile()
  picture = makePicture(file)

  while (getWidth(logo) > getWidth(picture)):
    logo = shrink(logo)
  
  #SET THE LOGO TO BOTTOM RIGHT
  targetX = getWidth(picture) - getWidth(logo)
  targetY = getHeight(picture)- getHeight(logo)
  
  #PREP THE LOGO - ? HOW WHY
  logo = logoPrep(logo, picture, targetX, targetY)
  
  #PLACE LOGO IN PICTURE
  picture = logoChroma(logo, picture)
  
  show(picture)
  print 'Saving image to same directory with _result.jpg appended..'
  writePictureTo(pic, filename + "_result.jpg")
  return picture
 
#FUNCTION CALL  
usersPicture()
  

                        