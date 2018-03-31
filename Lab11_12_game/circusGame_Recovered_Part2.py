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
    command, comTypeCode = parseCommand(command, location, comTypeCode)
  
    if (comTypeCode == 0):#Jiwanjot Sandhu
      #break (checking the behaviour of break statement)
      print "End Game"
      break
    elif (comTypeCode == 1):
      dispLocation(location)
    elif (comTypeCode == 2):
      execMovement(location, command) 
    elif (comTypeCode ==3):
      dispHelp()
    elif (comTypeCode == 4):
      yell(location)
    
def dispLocation(location): #Nikola Petkov
  print "You are currently at the " + location
  if location.lower() == "ticket gate":
    print "The turnstyles are locked and looks difficult to climb over.\n To the NORTH you see a big tent. The tent has smaller entrance NORTHEAST.\n Through the gate bars you spot a clown in the distance. Maybe you can YELL out to them."
  elif location.lower() == "circus tent":
    print "The insides are strung with dim holiday lights. Doesn't look like there have been any shows recently.\n The spectator seats are to the EAST. There is an opening in the tent NORTH, SOUTH, and WEST."
  elif location.lower() == "spectator seats":
    print "The seats are littered with old tickets, discarded cups, and candy wrappers.\n From the seats you can see the all of the main stage to the EAST and an exit to the SOUTHEAST."
  elif location.lower() == "staging area":
    print "The equipment for the shows are kept here, including empty animal cages.\n There are entrances to the WEST and NORTHWEST."
  elif location.lower() == "backstage":
    print "It's a small backstage area. The counters along the outside are cluttered with junk.\n There are entrances to the SOUTH and SOUTHEAST."

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
  backStage = 'backstage'
  newLocation = ''
  
  #Location is Ticket Gate
  if (location == ticketGate): 
    if(command == 'n' or command == 'north'):
      newLocation = circusTent
    elif(command == 'nw' or command == 'northwest'):
+      newLocation = spectatorSeats

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

def parseCommand(userCommand, userLocation, isCode):
  userCommand = userCommand.lower()
  newLocation = ''
  newTempStatus = ''
  if (userCommand == 'exit'):
    # Exit
    isCode = 0
  elif (userCommand == 'help'):
    # Print Help
    isCode = 3
    dispHelp()
    response = requestString("Press any key to continue")
    printPadding()
  elif (userCommand == 'go'):   
    # Move
    isCode = 2
    where = requestString("Where do you want to GO ?\nExamples: north,south,east,west")
    acceptableDirections = "north,south,east,west"
    # Not sure if up, down, left, and right are acceptable
    # print 'should we execute movement now?\n'
    # print containsString(where, acceptableDirections)
    if (containsString(where, acceptableDirections)):
      lewLocation = execMovement(userLocation, where)
      return newLocation, isCode
    printPadding()
    
  elif (userCommand == 'look'):
    isCode = 1
    where = requestString("Where do you want to LOOK ?\nExamples: here,north,south,east,west")
    acceptableDirections = "here,north,south,east,west"
    # Not sure if up, down, left, and right are acceptable
    if (containsString(where, acceptableDirections)):
      # Assigning new location to check ahead
      newTempStatus = execMovement(newLocation, where)
      dispLocation(newTempStatus, isCode)
      printPadding()
      return userLocation, isCode
      
  else:
    dispLocation(userLocation, isCode)
    printPadding()
  return userLocation, isCode

def containsString(searchTerm, searchString):
  if (searchString.find(searchTerm) > 0):
    return true
  return false

def printPadding():
  print '\n\n'

#Call to start game
main()
