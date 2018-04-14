#Rocky Moreno
#Mini Lab


##############################
#   Green Eggs and Ham Lab   #
##############################

###### OPEN FILE ######
file = 'C:\\Users\\computer1\\Documents\\GitHub2\\CST205\\moreno_r_labs\\miniLab\\eggs.txt'
#textFile = open(file, 'rt')
readFile = open(file,'rt')
readFile = readFile.read()

#Change text to lower case
readFile = readFile.lower()

#Set up dictionary
eggsDict = dict()

#Use counters to track 
counter = 0
wordIndex = 0
wordCounter = 0
word = ""

#Iterate through text
for x in readFile:  
  if x.isalpha() == false: 
    word = readFile[wordIndex:counter + 1]
    #print word
       
    if word.find('-') > 0:
      #print "yes"
      word = word[0:len(word) - 1]
      #print word
      wordCounter = wordCounter + 1
    elif word.find('\n') > 0:
      #print "yes"
      if word != ('\n'):
        word = word[0:len(word) - 1]
        #print word
        wordCounter = wordCounter + 1
    else:
      word = readFile[wordIndex:counter + 1]
      wordCounter = wordCounter + 1
     # print word
    wordIndex = counter + 1
  
  #Put words into dictionary  
  if word != ('\n') and word not in eggsDict:
    eggsDict[word] = 1
  elif word != ('\n'):
    eggsDict[word] += 1
      
  counter = counter + 1


#Print results
#print " Distinct count of how many words: " + str(wordCounter)
#print " " 

#highestNumber = 0
#highestKey = ''
#for words in eggsDict:
#  print "\'" + words + "\'" + " shows up "  + str(eggsDict[words]) + " times in the boD"
#  if eggsDict[words] > highestNumber:
 #   highestNumber = eggsDict[words]
  #  highestKey = words
#print " "
#print " "  
#print "The word with the highest count is " + "\'" + highestKey + "\'"
#print "It shows up " + str(highestNumber)  + " times!"
 
#readFile.close()
#writeFile.close()



################
#   WEB PAGE   #
################


file = open("C:\\Users\\computer1\\Documents\\GitHub2\\CST205\\moreno_r_labs\\miniLab\\greenEggs.html", "wt")

def bookWordAndCount():
  string = ''
  #for x in range(10):
   # string = string + '<h2>' + headlines[x] + '</h2><br>' 
  #return string
  
  for words in eggsDict:
    string = string + ("\'" + words + "\'" + " shows up "  + str(eggsDict[words]) + " times in the book <br>")

  return string
  
def wordFrequency():
  string0to50 = ''
  string50to150 = ''
  string150to300 = ''
  string300to350 = ''
  for words in eggsDict:
    if eggsDict[words] > 0 and eggsDict[words] < 50:
      string0to50 = string0to50 + "<p style=\"color:blue; font-size:12px; font-weight:11px\">" + words + "</p><br>"
    
    if eggsDict[words] >= 50  and eggsDict[words] < 150:
      string50to150 = string50to150  + "<p style=\"color:green; font-size:24px; font-weight:11px\">" + words + "</p><br>"
      
    if eggsDict[words] >= 150  and eggsDict[words] < 300:
      string150to300 = string150to300  + "<p style=\"color:red; font-size:48px; font-weight:11px\">" + words + "</p><br>"
      
    if eggsDict[words] >= 300  and eggsDict[words] < 350:
      string300to350 = string300to350  + "<p style=\"color:brown; font-size:72px; font-weight:11px\">" + words + "</p><br>"       
  
  
  return string0to50 + string50to150 + string150to300 + string300to350
  
def makePage():
  #replace the directory in the line below with the path to your file
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  
  <body>
  
  <h1>From Green Eggs and Ham</h1>
  
  <br>
  <h2>This is words and count from the book</h2>
  """
  +
  bookWordAndCount() 
  +
  """
  <h2>This is the word frequency</h2>
  """
  +
  wordFrequency()
  +

  """
  </body>
  </html>""")
  
makePage()
file.close()



