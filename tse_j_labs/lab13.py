#Lab 13

#replace certain words of article with user's input
#article source: 
def madlib():
  #make a list of lists of strings using format: ["definition", "answer"]
  libBank = [
    ["an object (plural)", ""],                   #index 0
    ["a type of natural disaster", ""],           #index 1
    ["an common object (singular)", ""],          #index 2
    ["a place", ""],                              #index 3
    ["your favorite food", ""],                   #index 4
    ["something that can fly", ""],               #index 5
    ["something hollow", ""],                     #index 6
    ["a nickname", ""],                           #index 7
    ["a number", ""],                             #index 8
    ["a side effect symptom of medication", ""],  #index 9
    ["something that is annoying", ""],           #index 10
    ["a powdery substance", ""],                  #index 11
    ["a thing that is disgusting", ""],           #index 12
    ["a -ing verb", ""],                          #index 13
    ["the name of a magazine", ""],               #index 14
    ["an occupation (plural)", ""],               #index 15
    ["a -ing verb", ""],                          #index 16
    ["a living thing (plural)", ""],              #index 17
    ["a liquid", ""],                             #index 18
    ["a number", ""]                              #index 19
  ]
  
  #make a list of article strings
  article = [
    "A new study has revealed that",                                                                                          #index 0
    "may be part of a \'",                                                                                                    #index 1
    "\' that can trigger childhood",                                                                                          #index 2
    "allergies.\n\nResearchers from",                                                                                         #index 3
    "say that a combination of",                                                                                              #index 4
    ",",                                                                                                                      #index 5
    "in",                                                                                                                     #index 6
    ",",                                                                                                                      #index 7
    "choices, and the effects of",                                                                                            #index 8
    "on the skin are all part of a package that triggers allergies.\n\n\'It\'s a major advance in our understanding of how",  #index 9
    "allergy starts early in life,\' lead author",                                                                            #index 10
    "said in a news release.\n\nThe researchers found that up to",                                                            #index 11
    "percent of children with",                                                                                               #index 12
    "allergies experience",                                                                                                   #index 13
    "that may be caused by",                                                                                                  #index 14
    "that reduce the skin\'s barrier against allergens.\n\n",                                                                 #index 15
    "says the top skin layer is made of",                                                                                     #index 16
    "and the",                                                                                                                #index 17
    "disrupt that barrier.\n\nThe allergy-immunology professor explains that",                                                #index 18
    "leave",                                                                                                                  #index 19
    "on the skin that alters a child\'s skin absorbency. \'They may not be",                                                  #index 20
    "",                                                                                                                       #index 21
    "allergens as a newborn, but they are getting them on their skin.\'\n\nThe report, which will be published in the",       #index 22
    ", urges",                                                                                                                #index 23
    "or anyone working with children to wash their hands before",                                                             #index 24
    "",                                                                                                                       #index 25
    ".\n\nThe team from",                                                                                                     #index 26
    "also advises adults to use",                                                                                             #index 27
    "sparingly and to rinse off the excess",                                                                                  #index 28
    "those",                                                                                                                  #index 29
    "leave behind with",                                                                                                      #index 30
    ".\n\nAccording to the CDC, four to six percent of children in the U.S. suffer from",                                     #index 31
    "allergies. From 1997 to 2007",                                                                                           #index 32
    "allergy cases rose by",                                                                                                  #index 33
    "percent among children in the country.\n\n"                                                                              #index 34                                     
  ]
  
  #prompt user for input
  for item in libBank:
    while item[1] == "": #ensures something is entered by user
      item[1] = requestString("I need " + item[0])
      item[1] = item[1].upper()
      
  #print result
  libIndex = 0     #tracks current lib index
  articleIndex = 0 #tracks current article index
  for line in article:
    print line,
    if articleIndex in [8, 17, 18, 27, 29]: #catches repeated libs
      print libBank[0][1],
    elif articleIndex in [7, 9, 12, 21, 31, 32]: #catches repeated libs
      print libBank[2][1],
    elif articleIndex == 26: #catches repeated libs
      print libBank[3][1],
    elif articleIndex == 15: #catches repeated libs
      print libBank[7][1],
    elif articleIndex == 28: #catches repeated libs
      print libBank[12][1],
    elif articleIndex == 34: # catches end of article 
      break
    else:
      print libBank[libIndex][1],
      libIndex += 1
    articleIndex +=1