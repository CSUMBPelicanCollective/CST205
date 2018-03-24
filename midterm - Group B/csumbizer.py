
def logoPrep(source, target, targetX, targetY):   
  canvas = makeEmptyPicture(getWidth(target), getHeight(target), green)
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      pic_pixel = getPixel(source, x, y)
      pic_pixel_color = getColor(pic_pixel)  
      setColor(getPixel(canvas, x + targetX ,y + targetY), pic_pixel_color)
      
  #show (canvas)
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
  show(source)
  #writePictureTo(source, "C://Users//rocky.moreno//Documents//JES//image_portfolio//Lab6 green screen//mango_palm_green_screen.jpg")
  return(source)
  
def usersPicture():
  #CSUMB Logo
  filename = ("C:\Users\computer1\Documents\JES\midterm\\csumb_logo_greenscreen.png")
  logo = makePicture(filename)
  #show(logo)
  
  
  
  # PICK A PICTURE FOR THE TARGET
  file = pickAFile()
  picture = makePicture(file)
  
  
  #print logo
  #logo = shrink(logo)
  #print logo
  
  logoWidth = getWidth(logo)
  while (getWidth(logo) > getWidth(picture)):   
    logo = shrink(logo)
    #print " This is logo width " 
    #print logo
    #print "Ths is getwidthPicture " 
    #print getWidth(picture)
  
  #SET THE LOGO TO BOTTOM RIGHT
  targetX = getWidth(picture) - getWidth(logo)
  targetY = getHeight(picture)- getHeight(logo)
  
  #PREP THE LOGO
  logo = logoPrep(logo, picture, targetX, targetY)
  
  #PLACE LOGO IN PICTURE
  picture = logoChroma(logo, picture)
  
  show(picture)
  return picture

  
    
#FUNCTION CALL  
usersPicture()
  

  