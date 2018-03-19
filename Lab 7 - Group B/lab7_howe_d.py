# Lab 7
# Pelican Collective Sub-Group: Daniel, Rogelio, Jiwan

def snowMan(pic):
  #filename = pickAFile()
  #pic = makePicture(filename)
  #explore(pic)
  #xCordinate = requestInteger("Where should the Snowman go? Please enter X coordinate:")
  #yCordinate = requestInteger("Where should the Snowman go? Please enter Y coordinate:")
  xCordinate = 250
  yCordinate = 850
  #snowBallSize = requestInteger("How big should the base of the Snowman be?")
  snowBallSize = 200
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
  
def insertText(pic, color):
  #filename = pickAFile()
  #pic = makePicture(filename)
  import java.awt.Font as Font
  #xCordinate = requestInteger("Where should the text go? Please enter X coordinate:")
  #yCordinate = requestInteger("Where should the text go? Please enter Y coordinate:")
  xCordinate = 500
  yCordinate = 650
  #text = requestString("Enter the text:")
  text = "I'd rather be\nat a St. Patricks Day Party"
  while (getWidth(pic) < xCordinate or xCordinate < 0):
    xCordinate = requestInteger("The text won't show in that coordinate.. Please enter new X coordinate:")
  while (getHeight(pic) < yCordinate or yCordinate < 0):
    yCordinate = requestInteger("The text won't show in that coordinate.. Please enter Y coordinate:")
  print "Adding text to image.."
  print "Length is %d" % (len(text))
  rectPadding = 10
  textSize = 40
  rectWidth = len(text) * textSize / 2 + rectPadding
  rectHeight = int(textSize * 0.5) + rectPadding * 2
  addRectFilled(pic, xCordinate - rectPadding, yCordinate - rectPadding, rectWidth + rectPadding, rectHeight + rectPadding, color)
  choiceFont = makeStyle("Chalkboard", Font.BOLD, textSize)
  addTextWithStyle(pic, xCordinate, yCordinate + rectHeight - rectPadding, text, choiceFont)
  return pic
  
def talkingSnowMan():
  filename = pickAFile()
  pic = makePicture(filename)
  pic = snowMan(pic)
  pic = insertText(pic, green)
  repaint(pic)
  writePictureTo(pic, pickAFile())
  
talkingSnowMan()