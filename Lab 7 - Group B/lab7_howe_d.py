# Lab 7
# Pelican Collective Sub-Group: Daniel, Rogelio, Jiwan

def snowMan(pic):
  #filename = pickAFile()
  #pic = makePicture(filename)
  #explore(pic)
  xCordinate = requestInteger("Where should the Snowman go? Please enter X coordinate:")
  yCordinate = requestInteger("Where should the Snowman go? Please enter Y coordinate:")
  #xCordinate = 250
  #yCordinate = 850
  snowBallSize = requestInteger("How big should the base of the Snowman be?")
  #snowBallSize = 200
  while (xCordinate - snowBallSize / 2 <= 0 or getWidth(pic) < xCordinate + snowBallSize):
    xCordinate = requestInteger("The Snowman is too wide for the coordinates provided. Please enter new X coordinate:")
  offset = 0
  for i in range(0,3):
    if (i == 2):
      # The nose is drawn fist so that it is below the oval that will be drawn below (the end of the for loop)
      print "Drawing nose.."
      startX = int(xCordinate + offset / 2)
      startY = int(yCordinate - offset + snowBallSize / 2)
      endX = int(startX + (snowBallSize / 2) + (snowBallSize * 0.5))
      endY = startY - 2
      print "First line of the nose starts at %d, %d, and ends at %d, %d" % (startX, startY, endX, endY)
      addLine(pic, startX, startY, endX, endY, red)
      addLine(pic, startX + 1, startY + 1, endX + 1, endY + 1, red)
      addLine(pic, startX - 1, startY - 1, endX - 1, endY - 1, red)
      startX = startX - 10
      print "Second line of the nose starts at %d, %d, and ends at %d, %d" % (startX, startY, endX, endY)
      for addWeight in range (0, 10):
         addLine(pic, startX + addWeight, startY + addWeight, endX + addWeight, endY + addWeight, red)     
    print "Drawing %d oval at %d, %d with the size of %d by %d" % (i, int(xCordinate - offset / 2), int(yCordinate + offset), int(snowBallSize), int(snowBallSize * 0.95))
    addOvalFilled(pic, int(xCordinate + offset / 4), int(yCordinate - offset), int(snowBallSize), int(snowBallSize * 0.95), white)
    if (i == 2):
      print "Drawing eye"
      separation = int(snowBallSize / 6)
      sizeEye = int(snowBallSize / 7)
      startX = int(xCordinate + offset / 2 + separation)
      startY = int(yCordinate - offset + snowBallSize / 2 - sizeEye)
      addOvalFilled(pic, startX, startY, sizeEye, sizeEye, black)
      print "Drawing eye at %d, %d and is %d big" % (startX, startY, sizeEye)
      startX = int(xCordinate + offset / 2 - separation)
    if (i == 1):
      print "Drawing arm"
      startX = int(xCordinate + offset)
      startY = int(yCordinate - offset + snowBallSize / 2)
      endX = int(xCordinate)
      endY = int(yCordinate - offset / 2)
      print "Line of the arm starts at %d, %d, and ends at %d, %d" % (startX, startY, endX, endY)
      for addWeight in range (0, 10):
        addLine(pic, startX + addWeight, startY + addWeight, endX + addWeight, endY + addWeight, black)
    offset = offset + (snowBallSize * 0.5)
    snowBallSize = snowBallSize * 0.75
  return pic
  
def insertText(pic, bgColor):
  #filename = pickAFile()
  #pic = makePicture(filename)
  import java.awt.Font as Font
  thoughtBalloons = requestInteger("How many text objects do you want to place?:")
  for i in range(0,thoughtBalloons):
    xCordinate = requestInteger(str(i) + ": Where should the text go? Please enter X coordinate:")
    yCordinate = requestInteger(str(i) + ": Where should the text go? Please enter Y coordinate:")
    text = requestString("Enter the text:")
    while (getWidth(pic) < xCordinate or xCordinate < 0):
      xCordinate = requestInteger("The text won't show in that coordinate.. Please enter new X coordinate:")
    while (getHeight(pic) < yCordinate or yCordinate < 0):
      yCordinate = requestInteger("The text won't show in that coordinate.. Please enter Y coordinate:")
    print "Adding text to image.."
    print "Length of text is %d characters" % (len(text))
    rectPadding = 10
    textSize = 40
    rectWidth = len(text) * textSize / 2 + rectPadding
    rectHeight = int(textSize * 0.5) + rectPadding * 2
    addRectFilled(pic, xCordinate - rectPadding, yCordinate - rectPadding, rectWidth + rectPadding, rectHeight + rectPadding, bgColor)
    choiceFont = makeStyle("Chalkboard", Font.BOLD, textSize)
    addTextWithStyle(pic, xCordinate, yCordinate + rectHeight - rectPadding, text, choiceFont)
  return pic
  
def pyCopy(source, target, targetX, targetY):
  #target = makeEmptyPicture(getWidth(source) + targetX * 2, getHeight(source) + targetY * 2)
  print 'Starting copy of '
  print source
  print 'To target '
  print target
  #print source
  #print 'Copying to '
  #print target
  #print 'X Offset '
  #print targetX
  #print 'Y Offset'
  #print targetY
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

def chromakey(target, source):
  print 'Starting chromakey function sourcing: '
  print source
  print 'To target: '
  print target
  #dimensional check
  if getWidth(source) > getWidth(target) or getHeight(source) > getHeight(target):
    print "Warning: source dimension is larger than target. operation aborted."
    return
  #replace green source pixel with target pixel
  sourceX = 0
  sourceY = 0
  for x in range (0, getWidth(target)):
    for y in range (0, getHeight(target)):
      sPixel = getPixel(source, sourceX, sourceY)
      tPixel = getPixel(target, x, y)
      #green condition check
      if getGreen(tPixel) > 200 and getRed(tPixel) < 80 and getBlue(tPixel) < 80:
        print 'Chromakey detected at %d, %d' % (x, y)
        setColor(tPixel, getColor(sPixel))
        #sourceX = sourceX + 1
        sourceY = sourceY + 1
    if getGreen(tPixel) > 200 and getRed(tPixel) < 80 and getBlue(tPixel) < 80:
        sourceX = sourceX + 1
  return(target)

def makeCollage(targetImage, targetX, targetY):
  width = 4000
  height = 1000
  print 'New collage target image size is %d x %d' % (width, height)
  print 'Each image should be no greater than %d x %d' % (width / 4, height)
  lastX = targetX
  lastY = targetY
  #newImage = makeEmptyPicture(width, height, black)
  for i in range(1, 5):
    filename = pickAFile()
    pic = makePicture(filename)
    #show(pic)
    #print 'Importing image %d x %d' % (getWidth(pic), getHeight(pic))
    while (getWidth(pic) > 1000 or getHeight(pic) > 1000):
      print 'Image too large.  Select new image no greater than 1000 x 1000'
      filename = pickAFile()
      pic = makePicture(filename)
    if i == 1:
      print 'Working on picture: %d' % (i,)
      #pic = makePicture("/Users/danielhowe/Desktop/Desert/1000x/ridgeline.jpg")
      newImage = pyCopy(pic, targetImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 2:
      print 'Working on picture: %d' % (i,)
      #pic = makePicture("/Users/danielhowe/Desktop/Desert/1000x/heart.jpg")
      newImage = pyCopy(pic, targetImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 3:
      print 'Working on picture: %d' % (i,)
      #pic = makePicture("/Users/danielhowe/Desktop/Desert/1000x/portrait.jpg")
      newImage = pyCopy(pic, targetImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
    elif i == 4:
      print 'Working on picture: %d' % (i,)
      #pic = makePicture("/Users/danielhowe/Desktop/Desert/1000x/flags.jpg")
      newImage = pyCopy(pic, targetImage, lastX, lastY)
      lastX = getWidth(pic) + lastX
  print 'Completed collage will now save..' 
  #repaint(newImage)
  #writePictureTo(newImage, "/Users/danielhowe/Desktop/collageOutput.jpg")
  return newImage

def talkingSnowMan():
  filename = pickAFile()
  pic = makePicture(filename)
  pic = snowMan(pic)
  pic = insertText(pic, green)
  repaint(pic)
  writePictureTo(pic, pickAFile())
  
def patricksDayCard():
  # Start with the base image
  filename = pickAFile()
  card = makePicture(filename)
  #card = makePicture("/Users/danielhowe/Desktop/Desert/source.jpg")
  #dimensions for the collage
  rectWidth = 4000
  rectHeight = 1000
  rectYPadding = 80
  startX = (getWidth(card) - rectWidth) / 2
  #check to make sure image is correct width
  while (getWidth(card) < rectWidth):
    print 'Image is not at least 4000 pixels wide.  Please select a new image:'
    filename = pickAFile()
    card = makePicture(filename)
  addOvalFilled(card, rectWidth / 2, rectHeight + rectYPadding, 30, 30, white)
  addOvalFilled(card, rectWidth / 2 + 30, rectHeight + rectYPadding + 30, 10, 10, white)
  card = makeCollage(card, int(startX), int(rectYPadding))
  card = insertText(card, white)
  writePictureTo(card, pickAFile())  
  show(card)