#Rocky Moreno
#execMovement function

#Rocky - execMovement Function
def execMovement(location, command):
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
    return newLocation
  else:
    #dispLocation(newLocation)
    return newLocation
  
#############################
#       FOR DEBUGGING       #
#############################
ticketGate = 'ticket gate'
location = ticketGate
command = 'n'
print execMovement(location, command)
# now in circus tent

#moving east to staging area
location = execMovement(location, command)
command = 'e'
print execMovement(location, command)
#now in staging area

#moving east still
location = execMovement(location, command)
command = 'e'
print execMovement(location, command)
#cant do taht 

#movign west back to circus tent
location = execMovement(location, command)
command = 'w'
print execMovement(location, command)
#now in circus tent


#moving east still
#location = execMovement(location, command)
#command = 'e'

