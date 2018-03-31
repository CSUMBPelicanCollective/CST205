#Rocky Moreno
#execMovement function

#Rocky - execMovement Function
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
  if (newLocation == ''):
    print 'You CANNOT go this way!\n\n'
    #dispLocation(location)                  
    return location
  else:
    return location
#comment

#############################
#       FOR DEBUGGING       #
#############################

choice = ''
#Starting location always ticket gate
location = 'ticket gate'

while (choice != 'yes'):
  command = requestString('Type a command: ')
  #print execMovement(location, command)
  location = execMovement(location, command)
  print location
  print 'This is current location ' + str(location)
  
  #choice = requestString('Do you want to quit: ')
  