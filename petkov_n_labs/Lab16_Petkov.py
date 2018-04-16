# Lab 16 - April 17, 2018 - Nikola Petkov
# Extracts headlines or similar information provided a URL and writes it to an HTML file.
# Adjust lines 8 and 16 for different websites.

import urllib

opener = urllib.FancyURLopener({})
website = opener.open("http://www.dailymail.co.uk/ushome/index.html")
whole = website.read()

headlineFound = False  # Indicates that a headline is coming.
headlines = []         # Holds all the headlines found.
temp = ''              # Temporary string to hold each headline.

for char in range(0, len(whole)):
  if whole[char:char+22] == "class=\"articleHeadline":  # Indicates that a headline was found.
    headlineFound = True
  if whole[char:char+1] == ">" and headlineFound == True:  # If it was found, look for a HTML heading.
    char += 1  # Increment the counter to skip the heading opening.
    while whole[char:char+1] != "<":  # Add chars to temporary string until the closing heading is found.
      temp = temp + whole[char]
      char += 1
    headlines.append(temp)
    temp = ''              # Reset temp and headlineFound to start looking for the next headline.
    headlineFound = False

def makePage():
  file = open(pickAFile(), "wt")    # HTML file to write headlines to.
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
    Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">""")
  
  for h in range(len(headlines)):  # Write all the headlines found.
    file.write("""
  
    <html>
    <head><title>Headline """ + str(h) + """</title>
    </head>
    <body>
    <h2>""" + headlines[h] + """</h2>
    </body>
    </html>""")
  
  file.close()