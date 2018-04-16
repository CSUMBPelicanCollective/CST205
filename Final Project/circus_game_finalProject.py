# PELICAN COLLECTIVE - Group A/2 + Group B = Daniel Howe, Nikola Petkov, Rogelio Moreno, Jiwanjot Sandhu
# Final Project - Circus Game

def main(): #Jason Tse
  #initialize game variables
  location = "ticket gate"
  locationHistory = ['ticket gate']    # Records the path the player has taken.
  command = "none"
  comTypeCode = 99
  inventory = []
  progress = 0 #This variable is used to determine game endings
  player = ''  # Holds the player's name.
  

#########################################
#             SOUND EFFECTS             #  
#########################################
  
  dir = __file__                 # Full directory for the .py file
  dir = dir.rsplit("\\", 1)      # Remove file name.
  dir = dir[0] + "\\Game Data\\" # Add directory for game files.
  setMediaPath(dir)
  
  background=makeSound("background.wav")
  for sample in getSamples(background):
      value = getSampleValue(sample)
      value = value * 0.1
      setSampleValue(sample, value)
  play(background)
  door = makeSound("dooropen.wav") 
  for sample in getSamples(door):
      value = getSampleValue(sample)
      value = value * 5.0
      setSampleValue(sample, value)
  movement = makeSound("footsteps.wav")
  for sample in getSamples(movement):
    value = getSampleValue(sample)
    value = value * 5.0
    setSampleValue(sample, value)



	
  #initStory: start user UI
  showInformation("You suddenly awoke on the hard ground outdoors. As your eyes adjust to the dimly moon-lit surroundings, you find yourself inside the front gates of an old abandoned circus. " \
                  "In the wind you could hear faint giggling.\nClick OK to play. Click Stop to exit the game.")
  player = requestString("Enter your name:")
  if len(player) == 0:
    player = 'Player'
  dispLocation(location, inventory)
  
	
  #main game loop
  while True:
    #prompt player for command
    command = requestString("What will you do?")
    command = command.lower().strip()
    while len(command) < 1:
      command = requestString("I didn't understand. What will you do?\nType 'help' for more information.")
      command = command.lower().strip()
    
    #parse input into command
    command, comTypeCode = parseCommand(command)
    
    #calls the appropriate function based on the comTypeCode
    #also prints the progress of the game
    if (comTypeCode == 0):  #Jiwanjot Sandhu
      #break (checking the behaviour of break statement)
      stopPlaying(background)
      print "End Game"
      break
    elif (comTypeCode == 1):
      dispLocation(location, inventory)
    elif (comTypeCode == 2):
      location = execMovement(location, command, inventory, locationHistory, door, movement)
    elif (comTypeCode == 3):
      dispHelp()
    elif (comTypeCode == 4):
      progress = yell(location, inventory)
    elif (comTypeCode == 5):
      inventory = getItem(location, inventory, command)
    elif (comTypeCode == 6):
      dispInventory(inventory)
    elif (comTypeCode == 7):
      progress = useItem(location, inventory, command, progress)
    
    #prints if game is a win or loss
    if (progress == 1):
      showInformation("Good End! Congratulations, " + player + ", you WON!")
      print "The path you took: " + str(locationHistory)
      stopPlaying(background)
      break
    elif (progress == 2):
      showInformation("Bad End! Sorry, " + player + ", you LOST!")
      print "The path you took: " + str(locationHistory)
      stopPlaying(background)
      break

    
  
  
  

    
    
    ################################################  
    #       TESTING FOR LOCATION HISTORY, MAP       #
    ################################################  
    #print locationHistory
    #open map
    #angleMovement = []
   # if (location == 'spectator seats' or location == 'ticket gate') and (command == 'northwest' or command == 'southeast'):
      
     # angleMovement.append('specttoticket')
    #print "this is the current location from main towards bottom of main " + currentLocation
    #print " this is the location variable from main " + location 
    show (map(location, locationHistory))
    
def dispLocation(location, inventory): #Nikola Petkov
  print "You are currently at the " + location
  if location.lower() == "ticket gate":
    print "The turnstyles are locked and looks difficult to climb over.\nTo the NORTH you see a big tent. The tent has smaller entrance NORTHWEST.\nThrough the gate bars you spot a clown in the distance. Maybe you can YELL out to them.\n"
  elif location.lower() == "circus tent":
    print "The insides are strung with dim holiday lights. Doesn't look like there have been any shows recently.\nThe spectator seats are to the WEST. There is an opening in the tent NORTH, SOUTH, and EAST.\n"
    if "clown nose" not in inventory:
      print "There is a CLOWN NOSE on the ground in the middle of the tent.\n"
  elif location.lower() == "spectator seats":
    print "The seats are littered with old tickets, discarded cups, and candy wrappers.\nFrom the seats you can see all of the main stage to the EAST and an exit to the SOUTHEAST.\n"
  elif location.lower() == "staging area":
    print "The equipment for the shows are kept here, including empty animal cages.\nThere are entrances to the WEST, NORTHWEST, and SOUTH.\n"
  elif location.lower() == "backstage":
    print "It's a small backstage area. The counters along the outside are cluttered with junk.\nThere are entrances to the SOUTH and SOUTHEAST.\n"
    if "keys" not in inventory:
      print "Among the clutter you spot a big ring of KEYS.\n"
  elif location.lower() == "security room":
    print "The room is filled with monitors. Mostly static, but one monitor shows the ticket gate.\nThere are doors to the NORTH and SOUTH.\nLooks like the SOUTH door also need KEYS.\n"
  elif location.lower() == "trailer":
    print "The trailer is dark, and it doesn't look like anybody is home.\nThere is a path to the SOUTH.\n"

def dispHelp(): #Nikola Petkov
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - H E L P - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
  print "exit - exits the game    help (h) - displays this menu."
  print "look (l) - look around the current location."
  print "go - move in a given direction.    yell - you can yell but who will hear you?"
  print "Directions: north (n), south (s), east (e), west (w),"
  print "                     northwest (nw), northeast (ne), southeast (se), southwest (sw)."
  print "get - pick up an item at the current location.    use - use an item from your inventory."
  print "inventory (i) - display the items currently in your inventory."
  print "ex. \"go north\" or \"go n\" will move you north of current location (if it exists)."
  print "ex. \"use 'item'\" will attempt to use an 'item' from your inventory."
  print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def dispInventory(inventory):  #Nikola Petkov
  print "Inventory: ",
  print inventory
  
def getItem(location, inventory, command):  #Nikola Petkov
  if (command in inventory):  # item is already in the inventory
    print "No " + command + " can be seen at " + location
  elif (location == "circus tent") and ("clown nose" in command):
    print "You picked up a clown nose."
    inventory.append(command)
  elif (location == "backstage") and ("keys" in command):
    print "You picked up some keys."
    inventory.append(command)
  else:
    print "There's no such item in " + location
  return inventory

def useItem(location, inventory, command, progress):  #Nikola Petkov
  if (command not in inventory):
    print "No such item is in your inventory."
  elif (location == "security room") and ("keys" in inventory) and ("keys" in command):
    progress = 1	# Good End
    print "The door unlocked."
  elif (location == "security room") and ("clown nose" in command):
    print "Haha, you can't unlock a door using a " + command
  else:
    print command + " is of no use in " + location
  return progress
  
  
  
  
#########################################
#          EXEC MOVEMENT FUNCTION       #  
#########################################

def execMovement(location, command, inventory, locationHistory, door, movement):  #Rocky Moreno
  ticketGate = 'ticket gate'
  circusTent = 'circus tent'
  spectatorSeats = 'spectator seats'
  stagingArea = 'staging area'
  backStage = 'backstage'
  trailer = 'trailer'
  securityRoom = 'security room'
  newLocation = ''
     
  #Location is Ticket Gate
  if (location == ticketGate): 
    if(command == 'n' or command == 'north'):
      newLocation = circusTent
      locationHistory.append('ticketToCircus')
    elif(command == 'nw' or command == 'northwest'):
      newLocation = spectatorSeats
      locationHistory.append("ticketToSpectator") 

  #Location is Circus Tent    
  elif (location == circusTent):
    if(command == 's' or command == 'south'):
      newLocation = ticketGate
      locationHistory.append('circusToTicket')
    elif(command == 'n' or command == 'north'):
      newLocation = backStage
      locationHistory.append('circusToBack')
    elif(command == 'w' or command == 'west'):
      newLocation = spectatorSeats
      locationHistory.append('circusToSpectator')
    elif(command == 'e' or command == 'east'):
      newLocation = stagingArea
      
  #Location is Specator Seats
  elif (location == spectatorSeats):
    if(command == 'se' or command == 'southeast'):
      newLocation = ticketGate
      locationHistory.append('spectatorToTicket')
    elif(command == 'e' or command == 'east'):
      newLocation = circusTent
      locationHistory.append('spectatorToCircusTent')
  
  #Location is Staging Area
  elif (location == stagingArea):
    if(command == 'w' or command == 'west'):
      newLocation = circusTent
      locationHistory.append('stagingToCircus')
    elif(command == 'nw' or command == 'northwest'):
      newLocation = backStage
      locationHistory.append('stagingToBack')
    elif(command == 'n' or command == 'north'):
      newLocation = trailer
    elif(command == 's' or command == 'south') and ('keys' in inventory):
      newLocation = securityRoom
    elif(command == 's' or command == 'south'):
      print 'The door to the south is locked'
      return location
      
  #Location is Back Stage
  elif (location == backStage):
    if(command == 's' or command == 'south'):
      newLocation = circusTent
      locationHistory.append('backToCircus')
    elif(command == 'se' or command == 'southeast'):
      newLocation = stagingArea
      locationHistory.append('backToStaging')
      
  #Location is Trailer
  elif (location == trailer):
    if(command == 's' or command == 'south'):
      newLocation = stagingArea
      
  #Location is Security Room
  elif (location == securityRoom):
    if(command == 'n' or command == 'north'):
      newLocation = stagingArea
    elif(command == 's' or command == 'south'):
      print 'Door to the south is locked'
      newLocation = location
      
          
  #if not valid direction print cant go thisway
  #else
  #display and return newLocation
  if (newLocation == ''):
    print 'can\'t go this way'                 
    return location
  else:
    dispLocation(newLocation, inventory)
    if newLocation <> location:
      play(door)
      play(movement)
      locationHistory.append(newLocation)    # Add new location to history.
    return newLocation
    
   

#########################################
#       END EXEC MOVEMENT FUNCTION      #  
#########################################


###################
#   Map Painter   #
###################

def mapPainter(source, target, targetX, targetY):   
  #canvas = makeEmptyPicture(305, 305, white)
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      pic_pixel = getPixel(source, x, y)
      pic_pixel_color = getColor(pic_pixel)  
      setColor(getPixel(target, x + targetX ,y + targetY), pic_pixel_color)
      
  #show (canvas)
  return target



###########################
#       map function      #  
###########################

def map(location, locationHistory):
  #print "This is from map function"
  #print len(locationHistory)
  #print locationHistory
 # print "this is the location from map function " + location
  
  
  
  #canvas = makeEmptyPicture(305, 305)
  #Game starts at ticket gate
  #addRectFilled(canvas, 115, 210, 75, 75, gray)#ticket gate
  #addText(canvas,120, 215, 'ticket Gate', black)
  filename = ("backgroundCanvas")
  mapBackground = makePicture(filename)
  #show(picture)
  filename = ("ticketgate")
  ticketGate = makePicture(filename)
  canvas = (mapPainter(ticketGate, mapBackground, 115, 210))
  
  
  if 'circusToTicket' in locationHistory:    
    #addRectFilled(canvas, 115, 115, 75, 75, gray)#Ticket
    #addText(canvas,120,120, 'Circus Tent', white)  
    addLine(canvas, 153, 210, 153, 190, white) ######line Circus Tent to Ticket Gate
    filename = ("ticketgate")
    ticketGate = makePicture(filename)
    canvas = (mapPainter(ticketGate, mapBackground, 115, 210))
    addText(canvas,120, 215, 'ticket Gate', white)
    
    
    
  if 'circusToSpectator' in locationHistory:    
    #addRectFilled(canvas, 115, 115, 75, 75, gray)#spectator
     
    addLine(canvas, 95, 152, 115, 152, white) ######line Circus Tent to Spectator Seats
    filename = ("spectatorseats")
    spectatorSeat = makePicture(filename)
    canvas = (mapPainter(spectatorSeat, mapBackground, 20, 115))
    addText(canvas,25,120, 'Spectator Seats', white)
     
  if 'circusToBack' in locationHistory:    
    #addRectFilled(canvas, 115, 20, 75, 75, gray)#backstage  
    addLine(canvas, 153, 115, 153, 95, white) ######line Circus Tent to Backstage
    filename = ("backstage")
    backStage = makePicture(filename)
    canvas = (mapPainter(backStage, mapBackground, 115, 20))
    addText(canvas,120,25, 'Backstage', white)
     
  
 # if 'spectator seats' in locationHistory: 
    #addRectFilled(canvas, 20, 115, 75, 75, gray)#spectator seats
    #addText(canvas,25,120, 'Spectator Seats', black)
  
  if 'spectatorToCircusTent' in locationHistory:    
    #addRectFilled(canvas, 115, 115, 75, 75, gray)#circus Tent
    #addText(canvas,120,120, 'Circus Tent', black)  
    addLine(canvas, 95, 152, 115, 152, white) ######line Spectator Seats to Circus Tent
    filename = ("circustent")
    circusTent = makePicture(filename)
    canvas = (mapPainter(circusTent, mapBackground, 115, 115))
    addText(canvas,120,120, 'Circus Tent',white)  
    
  if 'spectatorToTicket' in locationHistory:    
    #addRectFilled(canvas, 115, 210, 75, 75, gray)#ticket gate
    addLine(canvas, 115, 210, 95, 190, white) ######line Ticket Gate to Spectator Seats
    filename = ("ticketgate")
    ticketGate = makePicture(filename)
    canvas = (mapPainter(ticketGate, mapBackground, 115, 210))
    addText(canvas,120, 215, 'ticket Gate', white)
    
  
  
  
  if 'staging area' in locationHistory:
    #addRectFilled(canvas, 210, 115, 75, 75, gray)#staging area
    #addText(canvas,215,120, 'Staging Area', black)
    addLine(canvas, 190, 152, 210, 152, white) ######line Circus Tent to Staging Area
    filename = ("stagingarea")
    stagingArea = makePicture(filename)
    canvas = (mapPainter(stagingArea, mapBackground, 210, 115))
    addText(canvas,215, 120, 'Staging Area', white)
    
    

  if 'stagingToBack' in locationHistory:
    #addRectFilled(canvas, 115, 20, 75, 75, gray)#backstage
    #addText(canvas,120,25, 'Backstage', black)
    addLine(canvas, 190, 95, 210, 115, black) ######line Backstage to Staging Area
    filename = ("backstage")
    backStage = makePicture(filename)
    canvas = (mapPainter(backStage, mapBackground, 115, 20))
    addText(canvas,120,25, 'Backstage', white)
    


  if 'stagingToCircus' in locationHistory:
    addRectFilled(canvas, 115, 115, 75, 75, gray)#circus Tent
    addText(canvas,120,120, 'Circus Tent', black)  
    #addLine(canvas, 95, 152, 115, 152, black) ######line staging to Circus Tent
     
      
   
  if 'ticketToSpectator' in locationHistory:
    addLine(canvas, 115, 210, 95, 190, white) ######line Ticket Gate to Spectator Seats
    #addRectFilled(canvas, 20, 115, 75, 75, gray)#spectator seats   
    filename = ("spectatorseats")
    spectatorSeats = makePicture(filename)
    canvas = (mapPainter(spectatorSeats, mapBackground, 20, 115))
    addText(canvas,25,120, 'Spectator Seats', white)
    
    
    
  if 'ticketToCircus' in locationHistory:    
    #addRectFilled(canvas, 115, 115, 75, 75, gray)#circus Tent   
    addLine(canvas, 153, 210, 153, 190, white) ######line Ticket Gate to Circus Tent
    filename = ("circustent")
    circusTent = makePicture(filename)
    canvas = (mapPainter(circusTent, mapBackground, 115, 115))
    addText(canvas,120,120, 'Circus Tent',white)  

  
  if 'backToCircus' in locationHistory:  
    addRectFilled(canvas, 115, 20, 75, 75, red)#backstage
    addText(canvas,120,25, 'Backstage', white)
    addLine(canvas, 153, 115, 153, 95, white) ######line Circus Tent to Backstage
    filename = ("backstage")
    backStage = makePicture(filename)
    canvas = (mapPainter(backStage, mapBackground, 115, 20))
    addText(canvas,120,25, 'Backstage', white)
    
  if 'backToStaging' in locationHistory:  
    #addRectFilled(canvas, 210, 115, 75, 75, gray)#staging area
    #addText(canvas,215,120, 'Staging Area', black)
    addLine(canvas, 190, 95, 210, 115, white) ######line Backstage to Staging Area
    filename = ("stagingarea")
    stagingArea = makePicture(filename)
    canvas = (mapPainter(stagingArea, mapBackground, 210, 115))
    addText(canvas,215, 120, 'Staging Area', white) 
    
     
  
  if 'trailer' in locationHistory:  
    #addRectFilled(canvas, 210, 20, 75, 75, gray)#trailer
    #addText(canvas,220,25, 'Trailer', black)
    addLine(canvas, 248, 115, 248, 95,white) ######Staging Area to Trailer
    filename = ("trailer")
    trailer = makePicture(filename)
    canvas = (mapPainter(trailer, mapBackground, 210, 20))
    addText(canvas,220, 25, 'Trailer', white)
    
    
  if 'security room' in locationHistory:  
    #addRectFilled(canvas, 210, 210, 75, 75, gray) #security room
    #addText(canvas,215,215, 'Security Room', black)
    addLine(canvas, 247, 210, 247, 190, white)  ######line Security Room to Staging Area
    filename = ("securityroom")
    security = makePicture(filename)
    canvas = (mapPainter(security, mapBackground, 210, 210))
    addText(canvas,215, 215, 'Security Room', white)
    
  
  ############ you are here ################################  
  if location == 'backstage':
    addRect(canvas, 122, 27, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas,122, 48, 'You Are', red)  # 7 and 28
    addText(canvas,130, 60, 'Here', red)  #add 8 and 12
    
  if location == 'circus tent':
    addRect(canvas, 122,122, 61, 61, red) #Tracker
    addText(canvas,130, 150, 'You Are', red)  
    addText(canvas,138, 162, 'Here', red)
    
  if location == 'staging area':
    addRect(canvas, 217, 122, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas,224, 150, 'You Are', red)  # 7 and 28
    addText(canvas,232, 162, 'Here', red)  #add 8 and 12
    
  if location == 'trailer': 
    addRect(canvas, 217, 27, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas,224, 55, 'You Are', red)  # 7 and 28
    addText(canvas,232, 67, 'Here', red)  #add 8 and 12 
    
  if location == 'security room':     
    addRect(canvas, 217, 217, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas,224, 245, 'You Are', red)  # 7 and 28
    addText(canvas,232, 257, 'Here', red)  #add 8 and 12
    
  if location == 'ticket gate':       
    addRect(canvas, 122, 217, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas, 129, 245, 'You Are', red)  # 7 and 28
    addText(canvas, 137, 257, 'Here', red)  #add 8 and 12
    
  if location == 'spectator seats':          
    addRect(canvas, 27, 122, 61, 61, red) #Tracker  add 7 and 7
    addText(canvas, 34, 150, 'You Are', red)  # 7 and 28
    addText(canvas, 42, 162, 'Here', red)  #add 8 and 12
       
  return canvas


###############################
#       End map function      #  
###############################


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
    print "I didn't understand that command. Type 'help' for more information."
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
  #check for yell
  if command == "yell":
    return(command, 4)
  #if first word is "get", return item as command
  if command[:3] == "get":
    command = command[4:]
    if command == '':
      command = requestString("Get what?")
    if command in ["clown nose", "keys"]:
      return(command, 5)
    else:
      print "There's no such item."
      return(command, 99)
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
    else:
      print "No such item is in your inventory."
      return(command, 99)
  #check for short directions only
  if command in ["n", "e", "s", "w", "ne", "nw", "se", "sw"]:
    return(command, 2)
  #check for long directions only
  if command in ["north", "east", "south", "west", "northeast", "northwest", "southeast", "southwest"]:
    return(command, 2)
  else:
    print "I didn't understand that command. Type 'help' for more information."
    return(command, 99)


#Call to start game
main()
