#PELICAN COLLECTIVE
#LAB 11 AND LAB 12
#GAME

def main(): #Jason Tse
  #initialize game variables
  location = "ticket gate"
  command = "none"
  comTypeCode = 99
	
  #initStory: start user UI
  print "You suddenly awoke on the hard ground outdoors."
  print "As your eyes adjust to the dimly moon-lit surroundings,"
  print "you find yourself inside the front gates of an old"
  print "abandoned circus. In the wind you could hear faint giggling."
  print "Type help for more information."
  print "Type exit to give up.\n"
  dispLocation(location)
	
  #main game loop
  while True:
    #prompt player for command
    command = requestString("What will you do?")
    command = command.lower().strip()
    while len(command) < 1 or not command.isalpha():
      command = requestString("I didn't understand. What will you do?")
      command = command.lower().strip()
    
    #parse input into command
    command, comTypeCode = parseCommand(command, comTypeCode)
  
  while(comTypeCode < 5): #Jiwanjot Sandhu
    if (comTypeCode == 0):
      break
      print "End Game"
    elif (comTypeCode == 1):
      dispLocation(location)
    elif (comTypeCode == 2):
      execMovement(location, command) 
    elif (comTypeCode ==3):
      disHelp()
    break
    
    

def dispLocation(location): #Nikola Petkov
  print "You are currently at the " + location
  if location.lower() == "ticket gate":
    print "Some description"
  elif location.lower() == "circus tent":
    print "Some description"
  elif location.lower() == "spectator seats":
    print "Some description"
  elif location.lower() == "staging area":
    print "Some description"
  elif location.lower() == "backstage":
    print "Some description"

def dispHelp(): #Nikola Petkov
  print "- - - - - - - - - - - - - H E L P - - - - - - - - - - - - -"
  print "exit - exits the game            help - displays this menu."
  print "look - look around the current location."
  print "go - move in a given direction."
  print "Directions: north, south, east, west, up,"
  print "                     northwest, northeast, southeast, southwest."
  print "ex. \"go east\" will move you east of current location (if it exists)"
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"