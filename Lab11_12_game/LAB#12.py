#PELICAN COLLECTIVE
#LAB 11 AND LAB 12
#GAME

def main(): #Jason Tse
  #initialize game variables
  location = "ticket gate"
  command = "none"
  comTypeCode = 99
  inventory = ""
  progress = 0 #This variable is used to determine game endings
	
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
    
    #calls the appropriate function based on the comTypeCode
    #also prints the progress of the game
    if (comTypeCode == 0):  #Jiwanjot Sandhu
      #break (checking the behaviour of break statement)
      print "End Game"
      break
    elif (comTypeCode == 1):
      dispLocation(location)
    elif (comTypeCode == 2):
      location = execMovement(location, command, inventory) 
    elif (comTypeCode == 3):
      dispHelp()
    elif (comTypeCode == 4):
      progress = yell(location, inventory)
    elif (comTypeCode == 5):
      getItem(location, inventory, command)
    elif (comTypeCode == 6):
      dispInventory(inventory)
    elif (comTypeCode == 7):
      useItem(location, inventory, command, progress)
    #prints if game is a win or loss
    if (progress == 1):
      print "Good End, congratulations you WON"
      break
    elif (progress == 2):
      print "Bad End, Please try again"
      break
    
def dispLocation(location): #Nikola Petkov
  print "You are currently at the " + location
  if location.lower() == "ticket gate":
    print "The turnstyles are locked and looks difficult to climb over.\nTo the NORTH you see a big tent. The tent has smaller entrance NORTHEAST.\nThrough the gate bars you spot a clown in the distance. Maybe you can YELL out to them.\n"
  elif location.lower() == "circus tent":
    print "The insides are strung with dim holiday lights. Doesn't look like there have been any shows recently.\nThe spectator seats are to the WEST. There is an opening in the tent NORTH, SOUTH, and EAST.\n"
  elif location.lower() == "spectator seats":
    print "The seats are littered with old tickets, discarded cups, and candy wrappers.\nFrom the seats you can see all of the main stage to the EAST and an exit to the SOUTHEAST.\n"
  elif location.lower() == "staging area":
    print "The equipment for the shows are kept here, including empty animal cages.\nThere are entrances to the WEST and NORTHWEST.\n"
  elif location.lower() == "backstage":
    print "It's a small backstage area. The counters along the outside are cluttered with junk.\nThere are entrances to the SOUTH and SOUTHEAST.\n"

def dispHelp(): #Nikola Petkov
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - H E L P - - - - - - - - - - - - - - - - - - - - - - - - - - -"
  print "exit - exits the game        help (h) - displays this menu."
  print "look (l) - look around the current location."
  print "go - move in a given direction."
  print "Directions: north (n), south (s), east (e), west (w),"
  print "                     northwest (nw), northeast (ne), southeast (se), southwest (sw)."
  print "get - pick up an item at the current location.		use - use an item from your inventory."
  print "inventory (i) - display the items currently in your inventory."
  print "ex. \"go north\" or \"go n\" will move you north of current location (if it exists)"
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def dispInventory(inventory):  #Nikola Petkov
  print "Inventory: " + inventory
  
def getItem(location, inventory, command):  #Nikola Petkov
  if (location == "circus tent") and ("clown nose" in command):
    inventory = inventory + ", " + command
  if (location == "backstage") and ("keys" in command):
    inventory = inventory + ", " + command
  return inventory

def useItem(location, inventory, command, progress):  #Nikola Petkov
  if (location == "security room") and (keys in inventory):
    progress == 1	# Good End
  if (location == "ticket gate") and (clownNose in inventory) and (command == 4):
    progress == 2	# Bad End
  return progress


def execMovement(location, command, inventory):  #Rocky Moreno
  ticketGate = 'ticket gate'
  circusTent = 'circus tent'
  spectatorSeats = 'spectator seats'
  stagingArea = 'staging area'
  backStage = 'backstage'
  trailer = 'trailer'
  securityRoom = 'security room'
  newLocation = ''
   
  #check if keys are in inventory
  hasKeys = 'no'

  for index in range(len(inventory)-1):
    if inventory[index:index+4] == 'keys':
      hasKeys = 'yes'
  
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
    elif(command == 'n' or command == 'north'):
      newLocation = trailer
    elif((command == 's' and hasKeys == 'yes') or (command == 'south' and hasKeys == 'yes')):
      newLocation = securityRoom
    elif((command == 's' and hasKeys == 'no') or (command == 'south' and hasKeys == 'no')):
      print 'The door to the south is locked'
      return location
      
  #Location is Back Stage
  elif (location == backStage):
    if(command == 's' or command == 'south'):
      newLocation = circusTent
    elif(command == 'se' or command == 'southeast'):
      newLocation = stagingArea
      
  #Location is Trailer
  elif (location == trailer):
    if(command == 's' or command == 'south'):
      newLocation = stagingArea
      
  #Location is Security Room
  elif (location == securityRoom):
    if(command == 'n' or command == 'north'):
      newLocation = stagingArea
      
  #if not valid direction print cant go thisway
  #else
  #display and return newLocation
  if (newLocation == ''):
    print 'can\'t go this way'                 
    return location
  else:
    dispLocation(newLocation)              
    return newLocation

#For yelling action. Only useful at ticket gate.        
def yell(location, inventory): #Jason Tse
  if location == "ticket gate" and "clown nose" in inventory:
    print "The clown thinks you stole its nose! The last thing you remember is the clown grabbing ahold of you ... "
    return 2
  elif location == "ticket gate":
    print "The clown seems to ignore you. It's looking for something."
  else:
    print "Now is not the time for that."
  return 0

def parseCommand(command):
  #If more than 3 words, ignore command
  if command.count(' ') > 2:
    print "I didn't understand that command"
    return(command, 99)
  #check for exit
  if command == "exit":
    return(command, 0)
  #check for look or l
  if command == "look" or command == "l":
    return(command, 1)
  #if first word is "go", return direction as command
  if command[:2] == "go":
    command = command[3:]
    if command == '':
      command = requestString("Which direction?")
      command = command.lower().strip()
    if command in ["n", "e", "s", "w", "ne", "nw", "se", "sw", "north", "east", "south", "west", "northeast", "northwest", "southeast", "southwest"]:
      return(command, 2)
  #check for help
  if command == "help" or command == "h":
    return(command, 3)
  #if first word is "get", return item as command
  if command[:3] == "get":
    command = command[4:]
    if command == '':
      command = requestString("Get what?")
    if command in ["clown nose", "keys"]:
      return(command, 5)
  #check for inventory or i
  if command == "inventory" or command == "i":
    return(command, 6)
  #if first word is "use", return use as command
  if command[:3] == "use":
    command = command[4:]
    if command == '':
      command = requestString("Use what?")
    if command in ["clown nose", "keys"]:
      return(command, 7)
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
