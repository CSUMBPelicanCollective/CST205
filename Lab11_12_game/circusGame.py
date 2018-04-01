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
  
    if (comTypeCode == 0):#Jiwanjot Sandhu
      #break (checking the behaviour of break statement)
      print "End Game"
      break
    elif (comTypeCode == 1):
      dispLocation(location)
    elif (comTypeCode == 2):
      location = execMovement(location, command) 
    elif (comTypeCode == 3):
      dispHelp()
    elif (comTypeCode == 4):
      yell(location)
    
def dispLocation(location): #Nikola Petkov
  print "You are currently at the " + location
  if location.lower() == "ticket gate":
    print "The turnstyles are locked and looks difficult to climb over.\nTo the NORTH you see a big tent. The tent has smaller entrance NORTHEAST.\nThrough the gate bars you spot a clown in the distance. Maybe you can YELL out to them."
  elif location.lower() == "circus tent":
    print "The insides are strung with dim holiday lights. Doesn't look like there have been any shows recently.\n The spectator seats are to the EAST. There is an opening in the tent NORTH, SOUTH, and WEST."
  elif location.lower() == "spectator seats":
    print "The seats are littered with old tickets, discarded cups, and candy wrappers.\n From the seats you can see the all of the main stage to the EAST and an exit to the SOUTHEAST."
  elif location.lower() == "staging area":
    print "The equipment for the shows are kept here, including empty animal cages.\n There are entrances to the WEST and NORTHWEST."
  elif location.lower() == "backstage":
    print "It's a small backstage area. The counters along the outside are cluttered with junk.\n There are entrances to the SOUTH and SOUTHEAST."

def dispHelp(): #Nikola Petkov
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - H E L P - - - - - - - - - - - - - - - - - - - - - - - - - -"
  print "exit - exits the game            help - displays this menu."
  print "look - look around the current location."
  print "go - move in a given direction."
  print "Directions: north (n), south (s), east (e), west (w),"
  print "                     northwest (nw), northeast (ne), southeast (se), southwest (sw)."
  print "ex. \"go north\" or \"go n\" will move you north of current location (if it exists)"
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def execMovement(location, command):  #Rocky Moreno
  print 'changing from'
  print location
  print 'changing with'
  print command
  ticketGate = 'ticket gate'
  circusTent = 'circus tent'
  spectatorSeats = 'spectator seats'
  stagingArea = 'staging area'
  backStage = 'backstage'
  newLocation = location
  
  #Location is Ticket Gate
  if (location == ticketGate): 
    if(command == 'n' or command == 'north'):
      newLocation = circusTent
    elif(command == 'nw' or command == 'northwest'):
      newLocation = spectatorSeats

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

def parseCommand(userCommand, isCode):
  # Check user commands for matching program status code
  extraVerb = "go"
  testGo = false
  extraVerb, testGo = commandCheck("go", userCommand, 2)
  
  
  if (userCommand == "exit"):
    # Exit
    isCode = 0
    print 'exit'
    return userCommand, isCode
  elif (userCommand == "help"):
    # Print Help
    isCode = 3
    print 'help'
    return userCommand, isCode
  elif (userCommand == "look"):
    isCode = 1
    print 'look'
    return userCommand, isCode
  elif (testGo):  
    # Move / Go
    # Initialization of variables
    newCommand = userCommand.strip('go')
    isCode = 66
    if (len(newCommand) < 4):
      return newCommand, isCode
    
    goodDirection = false
    acceptableDirections = "west"
    wordLength = 4
    newCommand = acceptableDirections
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print acceptableDirections
      print isCode
      return acceptableDirections, isCode
      
    goodDirection = false
    acceptableDirections = "east"
    wordLength = 4
    newCommand = acceptableDirections
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print acceptableDirections
      print isCode
      return acceptableDirections, isCode
      
    goodDirection = false
    acceptableDirections = "north"
    wordLength = 4
    newCommand = acceptableDirections
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print acceptableDirections
      print isCode
      return acceptableDirections, isCode
      
    goodDirection = false
    acceptableDirections = "south"
    wordLength = 4
    newCommand = ""
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print acceptableDirections
      print isCode
      return acceptableDirections, isCode
    
    goodDirection = false
    acceptableDirections = "southeast"
    wordLength = 9
    newCommand = ""
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print 'southeast'
      return acceptableDirections, isCode
    
    goodDirection = false
    acceptableDirections = "northeast"
    wordLength = 9
    newCommand = ""
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print 'northeast'
      return acceptableDirections, isCode
      
    goodDirection = false
    acceptableDirections = "southwest"
    wordLength = 9
    newCommand = ""
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print 'southwest'
      return "southwest", isCode
    
    goodDirection = false
    acceptableDirections = "northwest"
    wordLength = 9
    newCommand = ""
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      print 'northwest'
      return "northwest", isCode
      
  print 'returning default values'
  return "",99
    

# Checks an userInput string against stringToCheck
# Returns newString, commandFound
def commandCheck(userInput, stringToCheck, length):
  newString = ''
  commandFoundBool = false
  correctCharCountIndex = 0
  userInputStringLength = len(userInput)
  #print len(userInput)
  for i in range (0, len(stringToCheck)):
    if ( correctCharCountIndex == length ):
      # Whole string checked
      print newString
      return newString, commandFoundBool
    elif (userInput[correctCharCountIndex] == stringToCheck[i]):
      # This character matches the string
      newString = newString + userInput[correctCharCountIndex]
      correctCharCount = correctCharCountIndex + 1
      print len(newString)
      print length
      if (len(newString) <= length):
        # Matched
        commandFoundBool = true
        print newString
        return newString, commandFoundBool
    else:
      correctCharCountIndex = 0
      newString = ''
      #print 'none new:'+newString + ' state:'+str(commandFoundBool)
  return newString, commandFoundBool

def printPadding():
  print '\n\n'

#Call to start game
main()
