###################
#	WARM UP	#
###################

#Jiwanjot Sandhu
#Pelican Collective
#Lab 7 - SNOWMAN WARM UP

def makeSnowman():
  my_pic = makePicture(pickAFile())
  #402 180

  #body
  addOvalFilled(my_pic, 360, 150, 200, 200, white)
  addOvalFilled(my_pic, 405, 70, 120, 120, white)
  addOvalFilled(my_pic, 430, 20, 70, 70, white)

  #face
  #eyes
  addOvalFilled(my_pic, 470, 30, 10, 10, black)
  addOvalFilled(my_pic, 460, 40, 10, 10, orange)
  addOvalFilled(my_pic, 450, 30, 10, 10, black)

  addOvalFilled(my_pic, 445, 50, 10, 10, black)
  addOvalFilled(my_pic, 455, 55, 10, 10, black)
  addOvalFilled(my_pic, 465, 55, 10, 10, black)
  addOvalFilled(my_pic, 475, 50, 10, 10, black)

  arm = makeColor(208,139,82)

  addRectFilled(my_pic, 358, 100, 68,5, arm)
  addRectFilled(my_pic, 500, 100, 68,5, arm)
  myFont = makeStyle("Arial", bold, 75)

  addTextWithStyle(my_pic,550,440, "Hello Summer", myFont,white)
  writePictureTo(my_pic, pickAFile())
  #repaint(my_pic)
  explore(my_pic)

##############################
#	ST PATRICKS DAY CARD	#
##############################

#Jiwanjot Sandhu
#Pelican Collective
#Lab 7 - ST PATRICKS DAY CARD

#main
def Card():
  bgkd = makePicture(pickAFile())
  pic1 = makeNegative(makePicture(pickAFile()))
  pic2 = artify(makePicture(pickAFile()))
  pyCopy(pic1,bgkd,800,500)
  pyCopy(pic2,bgkd,460,0)
  font = makeStyle(serif,bold, 72)
  color = makeColor(255,255,255)
  addTextWithStyle(bgkd,200,380,"HAPPY ST. PATRICK'S DAY",font,color)
  writePictureTo(bgkd, pickAFile()) 
  show(bgkd)

#helper
def pyCopy(source, target, targetX, targetY):
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      if (targetX+x < getWidth(target)) and (targetY+y < getHeight(target)):
          p = getPixel(source, x, y)
          if(targetX < 0):
           targetX = 0
          if(targetY < 0):
           targetY = 0
          setColor(getPixel(target, targetX+x, targetY+y), getColor(p))
          
def makeNegative(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    negColor = makeColor(255 - r, 255 - g, 255 - b)
    setColor(p, negColor)
  return pic
  
def artify(pic):
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
      else:
        setRed(px, 223)
      
      if green < 64:
        setGreen(px, 31)
      elif green > 63 and green < 128:
        setGreen(px, 95)
      elif green > 127 and green < 192:
        setGreen(px, 159)
      else: 
        setBlue(px, 223)
      
      if blue < 64:
        setBlue(px, 31)
      elif blue > 63 and blue < 128:
        setBlue(px, 95)
      elif blue > 127 and blue < 192:
        setBlue(px, 159)
      else:
        setBlue(px, 223)
  return(pic)




