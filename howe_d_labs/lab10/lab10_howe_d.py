#############
#  Hangman  #
#############
def hangman():
  # Number of chances the user will have to guess the string
  chances = 6
  # String to be guessed by user
  guessMe = 'pirate'
  # Make sure the string is all lower case in the event it gets changed
  guessMe = guessMe.lower()
  # Store guesses in a string with similar length, but first fill up string with empty guesses consisting of underscore chars
  guessedCorrectString = makeStringWithUnderScore(len(guessMe))
  # Store whether they won or fail at the game
  won = false
  ################
  #    User      #
  # Instructions #
  ################
  print 'You will have %d chances to guess the characters from the word that I am thinking.  It is %d characters long.' % (chances,len(guessMe))
  print "But if you can\'t guess the word, you lose.  I win."
  print 'Begin:'
  print ''
  printStringWithSpaces(guessedCorrectString)
  
  ###############
  #    User     #
  #   Input     #
  ###############
  # Get user input and count against the guessed integer if it is not a good guess
  for i in range (0, chances):
    # Get user input and if not an alpha character request input again
    if (i > 0):
      print 'You have guessed '+str(i)+' out of '+str(chances)+' incorrectly.  You have '+str(chances - i)+' more chances to guess the word'
    continueStep = true
    while (continueStep):
      userInput = requestString("Enter a character:")
      # Check to see if more than one character or if not alpha
      if (userInput.isalpha() and len(userInput) == 1):
        # User entered the character correctly
        print ''
        userInput = userInput.lower()
        guessedCorrectString, correctBool = stringCheck(userInput, guessedCorrectString, guessMe)
        # If the user guesses correctly, they can guess again, it doesn't count against total guesses
        if (correctBool):
          print 'Good guess!'
          print ''
          printStringWithSpaces(guessedCorrectString)
          continueStep = true
          if (guessedCorrectString == guessMe):
            # Change won so for loop can be exited
            won = true
            print ''
            print 'You won!  This time.'
            print ''
            # Break out of the while loop
            continueStep = false
        else:
          # Character input not found in string
          print 'Sorry, nope.'
          print ''
          printStringWithSpaces(guessedCorrectString)
          print ''
          continueStep = false
      else:
        # User did not enter correctly
        print 'Please do not use symbols or numbers..please re-enter one character'
        print ''
    if (won):
      # User has won game. this time.
      break
  if (won != true):
    print 'You lose..'

####################
#      Create      #
# Formatted String #
####################
def makeStringWithUnderScore(length):
  newString = ''
  for i in range (0, length):
    newString = newString + '_'
  return newString

####################
#      Prints      #
# Formatted String #
####################          
def printStringWithSpaces(stringToPrint):
  newString = ''
  for i in range (0, len(stringToPrint)):
    newString = newString + ' ' + stringToPrint[i]
  print newString

######################
#  Checks & Stores   #
#      String        #
######################        
def stringCheck(userInput, userStringHistory, stringToCheck):
  newString = ''
  scoreBool = false
  for i in range (0, len(stringToCheck)):
    if (userInput[0] == stringToCheck[i] and userStringHistory[i] != userInput[0]):
      # The character matches the string and the user has not already entered something for this index
      newString = newString + userInput[0]
      scoreBool = true
    elif (userStringHistory[i].isalpha() == true):
      # Theres already a character that is not an underscore
      newString = newString + userStringHistory[i]
    else:
      # No match for this character
      newString = newString + '_'
  return newString, scoreBool

#############
#  Warm up  #
#############
def warmUp():
  stop = false
  while (stop != true):
    userName = requestString("Please enter your name: ")
    if (userName == 'stop'):
      print 'quitting'
      stop = true
    else:
      print userName