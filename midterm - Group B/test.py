def main():
  pic= makePicture( pickAFile() )
  show(pic)
  newPic= makeOutline(pic )
  show(newPic)

def makeOutline(pic ):
  picEdge=makeEmptyPicture(getWidth(pic),getHeight(pic))
  for x in range (0, getWidth(pic)-1):
    for y in range (0, getHeight(pic)-1):
      here=getPixel(picEdge,x,y)
      down = getPixel(pic,x,y+1)
      right = getPixel(pic, x+1,y)
      hereL=(getRed(here)+getGreen(here)+getBlue(here))/3
      downL=(getRed(down)+getGreen(down)+getBlue(down))/3
      rightL=(getRed(right)+getGreen(right)+getBlue(right))/3
      if abs (hereL-downL)>100 and abs(hereL-rightL)>100:
        setColor(here,black)
      if abs (hereL-downL)<=100 or abs(hereL-rightL)<=100:
        setColor(here,white)
  warholizedPic=warholize(picEdge)
  return warholizedPic

def warholize(picEdge):
  w= getWidth( picEdge )
  h= getHeight( picEdge )
  picNew= makeEmptyPicture( w, h )
  for x in range(0,w/2):
    for y in range (0,h/2):
      px=getPixel(picEdge,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,blue)
      else:
        setColor(pxNew,yellow)
  for x in range (w/2,w):
    for y in range (h/2,h):
      px=getPixel(picEdge,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,yellow)
      else:
        setColor(pxNew,blue)

  for x in range(0,w/2):
    for y in range (h/2,h):
      px=getPixel(picEdge,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,green)
      else:
        setColor(pxNew,red)
  for x in range (w/2,w):
    for y in range (0,h/2):
      px=getPixel(picEdge,x,y)
      r=getRed(px)
      pxNew=getPixel(picNew,x,y)
      if r >0:
        setColor(pxNew,red)
      else:
        setColor(pxNew,green)


  return picNew

    
