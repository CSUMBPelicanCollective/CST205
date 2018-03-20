""" Week 1, Lab #3
Daniel Howe
Rogelio Moreno
Nikola Petkov
Jiwanjot Sandhu
Jason Tse
"""

def get_pic():
  return makePicture(pickAFile())

#filename = pickAFile()
#pic = makePicture(filename)
#pixels = getPixels(pic)

"""Warm up #1 -- TEAM
Take the code to reduce the red in an image by half and turn it into a function in the program area of JES. Name this function halfRed."""

def halfRed():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * 0.5)
  repaint(pic)

"""Warm up #2 -- TEAM
Write a new function called noBlue that removes all of the blue from an image."""

def noBlue():
  pic = get_pic()
  pixels = getPixels(pic)
  #Apply color transformation to each pixel in for loop
  for p in pixels:
    b = getBlue(p)
    setBlue(p, 0)
  repaint(pic)

"""Problem 1:
-Write a new function called lessRed. This should work a lot like halfRed, but it should take a parameter that gives the percentage by which to reduce the red in the picture. So, for example, the function call lessRed(75) would cause the function to reduce the red in the image by 75%
-Rewrite halfRed so that it calls lessRed to do the red reduction for the image."""

# Problem 1
def lessRed(percent):
  if percent < 0 or percent > 100:
    print "Value must be between 0 and 100"
    return
  percent = 1 - (percent / 100.0)
  pic = get_pic()
  pixels = getPixels(pic)
  #Apply color transformation to each pixel in for loop
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percent)
  repaint(pic)
  print "Red was reduced by " + str((1-percent)*100) + "%"

"""Problem 2: (DEMO VIDEO) 
Now write a function called moreRed that increases the red in each pixel of an image the same way that lessRed decreased red. What might be a potential problem with increasing the red in a pixel? How could you mitigate this issue? Can you tell what JES is doing?"""

# Problem 2
def moreRed(percent):
  if percent < 0 or percent > 25400:
    print "Value must be positive but less than 25400."
    return
  percent = (percent / 100.0) + 1
  pic = get_pic()
  pixels = getPixels(pic)
  #Apply color transformation to each pixel in for loop
  for p in pixels:
    r = getRed(p)
    setRed(p, r * percent)
  repaint(pic)
  print "Red was increased by " + str((percent-1)*100) + "%"

"""Problem 3:
Write a function called roseColoredGlasses that makes an image look pink. Think about how you can manipulate the RGB components of each pixel to accomplish this."""

#Problem 3
def roseColoredGlasses():
  pic = get_pic()
  pixels = getPixels(pic)
  #Apply color transformation to each pixel in for loop
  for p in pixels:
    #Get initial values before setting ignoring red as that is default
    g = getGreen(p)
    b = getBlue(p)
    #The color for pink is 255, 102, 204
    #Using this ratio we come up with 1, .4, and .8
    setGreen(p, g * 0.4)
    setBlue(p, b * 0.8)
  repaint(pic)
  print "Look at those stunner pink shades.."

"""Problem 4:
JES has a function called makeLighter that will lighten a color. It takes a color as a parameter and returns the lightened version of that color. This means that if my function call looks like this:
newColor = makeLighter(oldColor)
newColor will contain the lightened version of oldColor
Write a function called lightenUp that uses a for loop to lighten each pixel in a picture. Remember that you can use getColor and setColor to access the color of a pixel"""

def lightenUp():
 pic = get_pic()
 #Apply color transformation to each pixel in for loop
 for p in getPixels(pic):
   color = getColor(p)
   newColor = makeLighter(color)
   setColor(p, newColor)
 repaint(pic)


"""Problem 5:
Write a function called makeNegative that creates the negative of an original picture. This means you will want to create the opposite value for the red, green and blue of that pixel. How might you get the opposite?
-Remember that for each or R, G, and B, the range of acceptable values is 0 to 255
-That means the opposite of 0 is 255 and the opposite of 255 is 0
-What about for a value in the middle? How might you get the opposite?
-Remember that you will need to separately get the opposite for the R, G, and B values"""

def makeNegative():
  pic = get_pic()
  pixels = getPixels(pic)
  #Apply color transformation to each pixel in for loop
  for p in pixels:
    r = getRed(p)
    r = 255 - r
    setRed(p, r)    
    g = getGreen(p)
    g = 255 - g
    setGreen(p, g)    
    b = getBlue(p)
    b = 255 -  b
    setBlue(p, b)
  repaint(pic)

"""Problem 6:
You can simulate a black and white image by converting your color image to gray-scale. It turns out that gray colors occur when the R G and B values for a pixel are all the same. e.g. 0, 0, 0 or 1, 1, 1 ... and so on. To go from a color image to a black and white image, you want to capture the intensity or luminance of a pixel. A rough estimate of luminance is the average of the R, G, and B values for a pixel.

-Create a function called BnW that converts each pixel to gray-scale by computing the average of the R G and B values for each pixel and then using that average as the new RGB values for that pixel.
-What do you think of the resulting image?
-It turns out that to make a really good black and white image, you actually want to weight each of the RG and B slightly differently to account for how the human eye sees each color differently. A better formula for luminace is: R*0.299 + G*0.587 + B*0.114
-Write a new function called betterBnW that uses the formula above to convert each pixel to gray-scale."""

def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for i in pixels:
    average_intensity = (getRed(i) + getBlue(i) + getGreen(i)) / 3
    setRed(i, average_intensity)
    setBlue(i, average_intensity)
    setGreen(i, average_intensity)
  repaint(pic)
  
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for i in pixels:
    luminosity = ((getRed(i)*0.299) + (getBlue(i)*0.114) + (getGreen(i)*0.587))
    setRed(i, luminosity)
    setBlue(i, luminosity)
    setGreen(i, luminosity)
  repaint(pic)