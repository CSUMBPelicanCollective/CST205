#Rocky Moreno
#execMovement function

#Rocky - execMovement Function
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
  #dispLocation(newLocation) 
  if (newLocation == ''):
    print 'can\'t go this way'                 
    return location
  else:
    #dispLocation(newLocation)              
    return newLocation
    
#############################
#       FOR DEBUGGING       #
#############################

choice = ''
#Starting location always ticket gate
location = 'ticket gate'
inventory = ' keys clown nose '

while (choice != 'yes'):
  command = requestString('Type a command: ')  
  #print execMovement(location, command)
  location = execMovement(location, command, inventory)
  #print location
  print 'This is current location ' + str(location)
