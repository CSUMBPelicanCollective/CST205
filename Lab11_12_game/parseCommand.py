def test():
  isCode = 99
  while (isCode > 0):
    userCommand = requestString("")
    newUserCommand = ""
    newIsCode = 0
    newUserCommand, newIsCode = parseCommand(str(userCommand), int(isCode))
    print 'userCommand:'+newUserCommand
    print 'isCode:'+str(newIsCode)
  

def parseCommand(userCommand, isCode):
  # Check user commands for matching program status code
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
    acceptableDirections = "east,west"
    wordLength = 4
    newCommand4 = acceptableDirections
    newCommand4, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      return newCommand4, isCode
      
    goodDirection = false
    acceptableDirections = "east"
    wordLength = 4
    newCommand = acceptableDirections
    newCommand, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      return acceptableDirections, isCode
    
    goodDirection = false
    acceptableDirections = "southeast,northeast,southwest,northwest"
    wordLength = 9
    newCommand8 = acceptableDirections
    newCommand8, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      return newCommand8, isCode
    
    goodDirection = false
    acceptableDirections = "north,south"
    wordLength = 6
    newCommand5 = acceptableDirections
    newCommand5, goodDirection = commandCheck(newCommand, acceptableDirections, wordLength)
    if (goodDirection == true):
      isCode = 2
      return newCommand5, isCode
      
  print 'returning default values'
  return "",99
    

########
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