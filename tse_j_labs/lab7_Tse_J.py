#Jason Tse
#Nikola Petkov
#Lab 7

#WARM UP
def addSnowman(startX, startY):
  desert = makePicture(pickAFile())
  #check if snowman fits
  if getWidth(desert) < 270 or getHeight(desert) < 230:
    print("Warning: This desert is not big enough for a snowman. Operation aborted!")
    return
  if startX + 270 > getWidth(desert):
    print("Warning: The snowman is too wide to fit there. Operation aborted!")
    return
  if startY + 230 > getHeight(desert):
    print("Warning: The snowman is too tall to fit there. Operation aborted!")
    return
  #begin drawing snowman
  #draw puddles
  addOvalFilled(desert, startX + 25, startY + 179, 52, 17, makeColor(40, 170, 230))
  addOvalFilled(desert, startX + 72, startY + 166, 165, 46, makeColor(40, 170, 230))
  addOvalFilled(desert, startX + 36, startY + 179, 165, 46, makeColor(40, 170, 230))
  addOvalFilled(desert, startX + 48, startY + 208, 52, 17, makeColor(40, 170, 230))
  addOvalFilled(desert, startX + 172, startY + 203, 82, 27, makeColor(40, 170, 230))
  addOvalFilled(desert, startX + 150, startY + 212, 52, 17, makeColor(40, 170, 230))
  #draw snowman
  addOvalFilled(desert, startX + 65, startY + 96, 141, 116, black)
  addOvalFilled(desert, startX + 66, startY + 97, 139, 114, white)
  addOvalFilled(desert, startX + 85, startY + 47, 101, 76, black)
  addOvalFilled(desert, startX + 86, startY + 48, 99, 74, white)
  addOvalFilled(desert, startX + 91, startY + 0, 81, 69, black)
  addOvalFilled(desert, startX + 92, startY + 1, 79, 67, white)
  #draw charcoal
  addOvalFilled(desert, startX + 147, startY + 24, 9, 9, black)
  addOvalFilled(desert, startX + 160, startY + 82, 9, 9, black)
  addOvalFilled(desert, startX + 149, startY + 113, 9, 9, black)
  addOvalFilled(desert, startX + 172, startY + 170, 9, 9, black)
  addOvalFilled(desert, startX + 106, startY + 216, 9, 9, black)
  addOvalFilled(desert, startX + 132, startY + 56, 4, 4, black)
  addOvalFilled(desert, startX + 135, startY + 50, 4, 4, black)
  addOvalFilled(desert, startX + 140, startY + 45, 4, 4, black)
  addOvalFilled(desert, startX + 146, startY + 48, 4, 4, black)
  addOvalFilled(desert, startX + 151, startY + 52, 4, 4, black)
  #draw branches
  addRectFilled(desert, startX + 0, startY + 182, 51, 3, makeColor(140, 42, 42))
  addRectFilled(desert, startX + 12, startY + 172, 2, 10, makeColor(140, 42, 42))
  addRectFilled(desert, startX + 8, startY + 184, 2, 7, makeColor(140, 42, 42))
  addRectFilled(desert, startX + 204, startY + 187, 65, 4, makeColor(140, 42, 42))
  addRectFilled(desert, startX + 255, startY + 179, 3, 10, makeColor(140, 42, 42))
  addRectFilled(desert, startX + 254, startY + 190, 2, 9, makeColor(140, 42, 42))
  #draw sweat
  addOvalFilled(desert, startX + 100, startY + 24, 5, 15, gray)
  addOvalFilled(desert, startX + 161, startY + 33, 4, 12, gray)
  addOvalFilled(desert, startX + 108, startY + 75, 2, 7, gray)
  addOvalFilled(desert, startX + 164, startY + 63, 5, 15, gray)
  addOvalFilled(desert, startX + 134, startY + 102, 5, 15, gray)
  addOvalFilled(desert, startX + 74, startY + 156, 3, 10, gray)
  addOvalFilled(desert, startX + 95, startY + 133, 5, 15, gray)
  addOvalFilled(desert, startX + 98, startY + 145, 3, 11, gray)
  addOvalFilled(desert, startX + 114, startY + 166, 5, 15, gray)
  addOvalFilled(desert, startX + 148, startY + 144, 5, 15, gray)
  addOvalFilled(desert, startX + 161, startY + 185, 5, 15, gray)
  addOvalFilled(desert, startX + 176, startY + 131, 2, 8, gray)
  addOvalFilled(desert, startX + 178, startY + 134, 5, 15, gray)
  
  addOvalFilled(desert, startX + 101, startY + 22, 5, 15, white)
  addOvalFilled(desert, startX + 162, startY + 31, 4, 12, white)
  addOvalFilled(desert, startX + 109, startY + 73, 2, 7, white)
  addOvalFilled(desert, startX + 165, startY + 60, 5, 15, white)
  addOvalFilled(desert, startX + 135, startY + 99, 5, 15, white)
  addOvalFilled(desert, startX + 75, startY + 154, 3, 10, white)
  addOvalFilled(desert, startX + 96, startY + 131, 5, 15, white)
  addOvalFilled(desert, startX + 99, startY + 143, 3, 11, white)
  addOvalFilled(desert, startX + 115, startY + 164, 5, 15, white)
  addOvalFilled(desert, startX + 149, startY + 142, 5, 15, white)
  addOvalFilled(desert, startX + 162, startY + 183, 5, 15, white)
  addOvalFilled(desert, startX + 177, startY + 129, 2, 8, white)
  addOvalFilled(desert, startX + 179, startY + 132, 5, 15, white)
  #repaint, save, return
  repaint(desert)
  writePictureTo(desert, pickAFile())
  return desert
  
  
#PROBLEM 1

#copy source into target if color does not match chromakey
def cutPasteColor(source, Xoffset, Yoffset, target, chromakey):
  #check fit
  if Xoffset + getWidth(source) > getWidth(target):
    print("Warning: Source image is too wide to fit here!")
  if Yoffset + getHeight(source) > getHeight(target):
    print("Warning: Source image is too tall to fit here!")
    
  #initialize source coordinates
  sourceX = 0
  sourceY = 0
  #paste source into target
  for x in range (Xoffset, Xoffset + getWidth(source)):
    for y in range (Yoffset, Yoffset + getHeight(source)):
      inputPixel = getPixel(source, sourceX, sourceY)
      outputPixel = getPixel(target, x, y)
      if distance(getColor(inputPixel), chromakey) > 115:
        setColor(outputPixel, getColor(inputPixel))
      sourceY = sourceY + 1
    sourceX = sourceX + 1
    sourceY = 0
  return target

#swap red with green value
def greenRedSwap(pic):
  pixels = getPixels(pic)
  for i in pixels:
    if distance(getColor(i), white) > 20:
      greenLumin = getGreen(i)
      setGreen(i, getRed(i))
      setRed(i, greenLumin)
  return pic

#compiles images into holiday card
def holidayCard():
  #set folder path to images
  print("Select folder of images.")
  setMediaFolder()
  #create new canvas
  card = makePicture("shamrock.jpg")
  
  #import rainbow image
  rainbow = makePicture("rainbow.jpg")
  card = cutPasteColor(rainbow, 113, 314, card, white)
  #import mug image
  mug = makePicture("mug.jpg")
  card = cutPasteColor(mug, 675, 0, card, black)
  #import cat image
  cat = makePicture("cat.jpg")
  card = cutPasteColor(cat, 0, 116, card, blue)
  #import hat image
  hat = greenRedSwap(makePicture("hat.jpg"))
  card = cutPasteColor(hat, 33, 124, card, white)
  #insert text
  addTextWithStyle(card, 201, 111, "Happy St. PatrrRR", makeStyle(sansSerif, plain, 72), white)
  addTextWithStyle(card, 200, 110, "Happy St. PatrrRR", makeStyle(sansSerif, plain, 72), yellow)
  addTextWithStyle(card, 571, 712, "Drink responsibly.", makeStyle(sansSerif, bold, 24), white)
  addTextWithStyle(card, 570, 711, "Drink responsibly.", makeStyle(sansSerif, bold, 24), yellow)
  #repaint, save, return
  repaint(card)
  writePictureTo(card, pickAFile())
  return card
