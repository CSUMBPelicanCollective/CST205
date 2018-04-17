#Rocky Moreno
#Lab 16



#################################
#   SCRAP AND PARSE HEADLINES   #
#################################

from urllib import *

page = urlopen("https://www.huffingtonpost.com/")
readFile = page.read()

#Headline list
headlines = []

#Story words found?        
storyWords = ''
storyFound = False

#Iterate through file to print Story headline
for x in range(0, len(readFile)):
  if readFile[x:x+32] == '<div class="card__headline__text':
    #print x
    storyFound = True
 
  if readFile[x:x+2] == "<d" and storyFound == True:
    #print 'found d'
    x = x + 34
    #Parse between div headline text and append to headline list
    while readFile[x:x+1] != "<":  
      storyWords = storyWords + readFile[x]
      x = x + 1
      #print storyWords
    
    headlines.append(storyWords)
    storyWords = ''     
    storyFound = False

#print headlines
#print "*** Huffington Post Headlines ***" 
#for x in range(10): 
 # print headlines[x]
  
  
################
#   WEB PAGE   #
################


file = open(pickAFile(), "wt")

def addText():
  string = ''
  for x in range(10):
    string = string + '<h2>' + headlines[x] + '</h2><br>' 
  return string


def makePage():
  #replace the directory in the line below with the path to your file
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  
  <body>
  
  <h1>HEADLINES FROM HUFFINGTON POST</h1>
  """
  
  +
 
  addText() 
  +
  
  """
  </body>
  </html>""")
  
makePage()
file.close()