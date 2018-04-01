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
    while len(command) < 1:
      command = requestString("I didn't understand. What will you do?")
      command = command.lower().strip()
    
    #parse input into command
    command, comTypeCode = parseCommand(command)
  
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
    print "The turnstyles are locked and looks difficult to climb over.\nTo the NORTH you see a big tent. The tent has smaller entrance NORTHEAST.\nThrough the gate bars you spot a clown in the distance. Maybe you can YELL out to them.\n"
  elif location.lower() == "circus tent":
    print "The insides are strung with dim holiday lights. Doesn't look like there have been any shows recently.\nThe spectator seats are to the EAST. There is an opening in the tent NORTH, SOUTH, and WEST.\n"
  elif location.lower() == "spectator seats":
    print "The seats are littered with old tickets, discarded cups, and candy wrappers.\nFrom the seats you can see the all of the main stage to the EAST and an exit to the SOUTHEAST.\n"
  elif location.lower() == "staging area":
    print "The equipment for the shows are kept here, including empty animal cages.\nThere are entrances to the WEST and NORTHWEST.\n"
  elif location.lower() == "backstage":
    print "It's a small backstage area. The counters along the outside are cluttered with junk.\nThere are entrances to the SOUTH and SOUTHEAST.\n"

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
    return newLocation

#For yelling action. Only useful at ticket gate.        
def yell(location): #Jason Tse
  if location == "ticket gate":
    print "The clown seems to ignore you."
  else:
    print "Now is not the time for that."

def parseCommand(command):
  #If more than 2 words, ignore command
  if command.count(' ') > 2:
    print "I didn't understand that command"
    return(command, 99)
  #check for word commands
  if command == "exit":
    return(command, 0)
  if command == "look":
    return(command, 1)
  #if first word is "go", return direction as command
  if command[:2] == "go":
    command = command[3:]
    return(command, 2)
  if command == "help":
    return(command, 3)
  if command == "yell":
    return(command, 4)
  #check for short directions only
  if command in ["n", "e", "s", "w", "ne", "nw", "se", "sw"]:
    return(command, 2)
  #check for long directions only
  if command in ["north", "east", "south", "west", "northeast", "northwest", "southeast", "southwest"]:
    return(command, 2)
  else:
    print "I didn't understand that command"
    return(command, 99)


#Call to start game
main()
