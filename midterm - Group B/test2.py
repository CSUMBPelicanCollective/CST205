def Warhol(inputname,outputname,c1,c2,c3,c4,c5,c6,c7,c8):

temp=getMediaPath("\\"+inputname)
original = makePicture(temp)

w=getWidth(original)
h=getHeight(original)
  
final=makeEmptyPicture(2*w,2*h,white)

for x in range(0,w):
for y in range(0,h):
pxin=getPixelAt(original,x,y)
pxout=getPixelAt(final,x,y)
if getColor(pxin)==black:
setColor(pxout,c1)
else:
setColor(pxout,c2)
# show image and write it as a file
show(final)
writePictureTo(final,getMediaPath("\\"+outputname))