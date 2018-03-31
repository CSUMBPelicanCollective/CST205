#PELICAN COLLECTIVE
#LAB 11 AND LAB 12
#GAME

def main(): #Jason Tse
  # initStory
  # initialize game variables
  location = "ticket gate"
  command = "none"
  comTypeCode = 99
  
  run = true	
  #main game loop
  while (run):
    dispLocation(location, comTypeCode)
    location, comTypeCode = parseCommand(requestString("What will you do?"), location, comTypeCode)

        
#####################
# Display and Print #
#####################

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
        
def dispLocation(location, isCode): #Nikola Petkov
  if isCode == 99:
    print "You suddenly awoke on the hard ground outdoors."
    print "As your eyes adjust to the dimly moon-lit surroundings,"
    print "you find yourself inside the front gates of an old"
    print "abandoned circus. In the wind you could hear faint giggling.\n"
    print "Type help for more information."
    print "Type exit to give up."
    printPadding()
 
  print "You are currently at the " + str(location)
  if location.lower() == "ticket gate":
    print "Some description"
    printPadding()
  elif location.lower() == "circus tent":
    print "Some description"
    printPadding()
  elif location.lower() == "spectator seats":
    print "Some description"
    printPadding()
  elif location.lower() == "staging area":
    print "Some description"
    printPadding()
  elif location.lower() == "backstage":
    print "Some description"
    printPadding()

def dispHelp(): #Nikola Petkov
  print "- - - - - - - - - - - - - H E L P - - - - - - - - - - - - -"
  print "exit - exits the game            help - displays this menu."
  print "look - look around the current location."
  print "go - move in a given direction."
  print "Directions: north, south, east, west, up,"
  print "                     northwest, northeast, southeast, southwest."
  print "ex. \"go east\" will move you east of current location (if it exists)"
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
  
#############
# Modifiers #
#############

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
  elif (newLocation == ''):
    print 'You CANNOT go this way!\n\n'
    #dispLocation(location)                  
    return location
  else:
    return location