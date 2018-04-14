#Lab 16

import urllib
import os
import re

def htmlScraper():
  #load website into string
  url = "https://hackaday.com/"
  htmlSource = urllib.urlopen(url)
  htmlString = htmlSource.read()
  
  #prepare htmlstring
  htmlList = re.split("<|>", htmlString) #delimits using '<' and '>'
  
  #get empty html file to hold scraped data
  scrapedSite = open(pickAFile(), "wt")
  
  #start writing scraped version of site
  listIndex = 0
  scrapedSite.write("<!DOCTYPE HTML><html><head><title>Scraped Hackaday.com</title></head><body>")
  
  #1. get title
  while htmlList[listIndex] != "title":    #find opening tag
    listIndex += 1
  titleString = htmlList[listIndex +1]     #get what's in the tag
  scrapedSite.write("<h1>" + titleString + "</h1><br>\n")
  
  #2. get twitter handle
  while "twitter:site" not in htmlList[listIndex]:   #find containing tag
    listIndex += 1
  sliceStart = htmlList[listIndex].find("@")         #find handle @
  sliceEnd = htmlList[listIndex].rfind("\"")         #find end of field
  twitterHandle = htmlList[listIndex][sliceStart:sliceEnd]
  scrapedSite.write("<i>Twitter: "+ twitterHandle + "</i><br><br>\n")
    
  #3. get recent headlines - 4. get author - 5. get publish date - 6. get article short description
  for i in range(7):                                  #there are 7 articles on the homepage
    while "entry-intro" not in htmlList[listIndex]:   #move to entry
      listIndex += 1
    while "h2" not in htmlList[listIndex]:            #move to headline
      listIndex += 1
    headline = htmlList[listIndex + 3]                #get headline
    while "By" not in htmlList[listIndex]:            #move to author
      listIndex += 1
    author = htmlList[listIndex + 2]                  #get author
    while "post-date" not in htmlList[listIndex]:     #move to publish date
      listIndex += 1
    publishDate = htmlList[listIndex + 1]             #get publish date
    while htmlList[listIndex]!= "p":                  #move to description
      listIndex += 1
    while htmlList[listIndex] == "p" or htmlList[listIndex] == "":  #clear extra paragraph tags
      listIndex += 1
    articleDesc = htmlList[listIndex]                 #get description
    
    scrapedSite.write("<b>" + headline + "</b><br>\n<i>" + author + " ---- " + publishDate + "</i><br>\n")
    scrapedSite.write(articleDesc + "<br><br>\n")
  scrapedSite.write("<br><br>\n")  #extra spacing for next section
  
  #7. get featured projects - 8. get project's author 
  scrapedSite.write("<h3>FEATURED PROJECTS</h3>\n")
  for i in range(2):                                      #there are 2 featured projects
    while "featured-project" not in htmlList[listIndex]:  #move to a project
      listIndex += 1
    while "h2" not in htmlList[listIndex]:                #move to project title
      listIndex += 1
    projectTitle = htmlList[listIndex + 1]                #get project title
    while "by" not in htmlList[listIndex]:                #move to project author
      listIndex += 1
    projectAuthor = htmlList[listIndex + 2]               #get project author
    
    scrapedSite.write("<b>" + projectTitle + "</b> by " + projectAuthor + "<br><br>\n")
  scrapedSite.write("<br><br>\n")  #extra spacing for next section
    
  #9. get recent store items - 10. get item price
  scrapedSite.write("<h3>STORE</h3>\n")
  for i in range(6):                                      #there are 6 featured store items
    while "store-item" not in htmlList[listIndex]:        #move to a store item
      listIndex += 1
    while "h2" not in htmlList[listIndex]:                #move to name of item
      listIndex += 1
    itemName = htmlList[listIndex + 1]                    #get item name
    while "store-price" not in htmlList[listIndex]:       #move to price
      listIndex += 1
    itemPrice = htmlList[listIndex + 1]                   #get item price
    
    scrapedSite.write("<b>" + itemName + "</b> <i>" + itemPrice + "</i><br><br>\n")
  
  scrapedSite.write("</body></html>")
  
  #close files
  htmlSource.close()
  scrapedSite.close()
  
  
