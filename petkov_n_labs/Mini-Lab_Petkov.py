# MINI-LAB: Adding on to the HTML Lab - Nikola Petkov - April 17, 2018
# Creates an HTML file of all the words occurring in a text file.
# Different colors and font sizes are used based on word occurrence.

file = pickAFile()        # Choose a text file to process.
fin = open(file, 'r')     # Open file stream for reading.
whole = fin.read()        # Read the entire text into a string variable.
fin.close()               # Close the text file.
wordList = []             # Will hold a list of all words in the file.
wordDict = dict()         # Will hold a dictionary and count of all words (converted to lowercase).

word = ''                 # Temporarily holds each word.
for char in whole:
  if char != ' ' and char != '\n' and char != '?' and char != '!' and char != ',' and char != '.' and char != '':  # Copy only words. Ignore spaces, new lines, and punctuation.
      word = word + char
  else:
    wordList.append(word)
    word = ''                  # Reset it so it's ready to accumulate the next word.

for element in wordList:       # Remove any empty characters from the list.
  if element == '':
    wordList.remove(element)
#wordList.remove('')            # Remove the last empty character. No idea why it's still in there (for eggs.txt).

for word in wordList:          # Convert each word to lowercase and store it and its count in a dictionary.
  word = word.lower()
  if word not in wordDict:
    wordDict[word] = 1
  else:
    wordDict[word] += 1

mostCommon = str(sorted(wordDict, key=wordDict.get, reverse=True)[0])  # https://stackoverflow.com/questions/7197315/5-maximum-values-in-a-python-dictionary
count = wordDict.get(mostCommon)  # Number of times most common word occurs.

def makePage():
  style = ""
  large = "\"color:#FF0000; font-size:50px; font-weight:bold\""
  medium = "\"color:#FF8000; font-size:30px; font-weight:normal\""
  small = "\"color:#FFF000; font-size:20px; font-weight:normal\""

  file = open(pickAFile(), "wt")    # HTML file to write headlines to.
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
    Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">""")
  
  for key, value in wordDict.items():  # Determine the style and write to HTML file.
    if value < (count * 0.3):
      style = small
    elif value < (count * 0.6):
      style = medium
    else:
      style = large
    # How many times the word occurs, as the title. The word with in a particular style.
    file.write("""
    
    <html>
    <head><title>Occurs """ + str(value) + """ times.</title>
    </head>
    <body>
    <p style=""" + style + """>""" + key + """</p>
    </body>
    </html>""")
  
  file.close()