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
      #break (checking the behaviour of break statement)
      print "End Game"
      break
    elif (comTypeCode == 1):
      dispLocation(location)
    elif (comTypeCode == 2):
      execMovement(location, command) 
    elif (comTypeCode ==3):
      dispHelp()
    
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
  

def execMovement(location, command):  #Rocky Moreno
  ticketGate = 'ticket gate'
  circusTent = 'circus tent'
  spectatorSeats = 'spectator seats'
  stagingArea = 'staging area'
  backStage = 'back stage'
  newLocation = ''
  
  #Location is Ticket Gate
  if (location == ticketGate): 
    if(command == 'n' or command == 'north'):
      newLocation = circusTent
      
  #Location is Circus Tent    
  elif (location == circusTent):
    if(command == 's' or command == 'south'):
      newLocation = ticketGate
    elif(command == 'n' or command == 'north'):
      newLocation = backStage
    elif(command == 'w' or command == 'west'):
      newLocation = spectatorSeats
    elif(command == 'e' or command == 'east'):
      newLocation = stagingArea
      
  #Location is Specator Seats
  elif (location == spectatorSeats):
    if(command == 'se' or command == 'southeast'):
      newLocation = ticketGate
    elif(command == 'e' or command == 'east'):
      newLocation = circusTent
  
  #Location is Staging Area
  elif (location == stagingArea):
    if(command == 'w' or command == 'west'):
      newLocation = circusTent
    elif(command == 'nw' or command == 'northwest'):
      newLocation = backStage
      
  #Location is Back Stage
  elif (location == backStage):
    if(command == 's' or command == 'south'):
      newLocation = circusTent
    elif(command == 'se' or command == 'southeast'):
      newLocation = stagingArea
      
  #if not valid direction print cant go thisway
  #else
  #display and return newLocation
  #dispLocation(newLocation) 
  if (newLocation == ''):
    print 'can\'t go this way'
    dispLocation(location)                  
    return location
  else:
    dispLocation(newLocation)              
    return newLocation

#For yelling action. Only useful at ticket gate.        
def yell(location): #Jason Tse
  if location == "ticket gate":
    print "The clown seems to ignore you."
  else:
    print "Now is not the time for that."