#Jason Tse
#Lab 10

#WARM UP - PART A
def namePlease():
  name = requestString("What's your name")
  print name


#WARM UP - PART B
def tellMeWhenToStop():
  inputString = requestString("Enter word:")
  inputString = inputString.lower() 
  while inputString != "stop":
    inputString = requestString("Enter word:")
    inputString = inputString.lower()


#HANGMAN GAME
#A game where players guess letters to form a certain word within a given amount of guesses
def hangman():
  #--PRE-GAME INITIALIZATION--
  answer = 'Maple tree'
  #convert answer to uppercase and remove leading/trailing spaces
  answer = answer.upper().strip()
  guesses = 6
  currentWord = '_' * len(answer) #create a blank version of the answer
  guessHistory = '' #an empty string to hold incorrect guesses
  #adjust currentWord for multiple words by replacing spaces
  for i in range(len(answer)):
    if answer[i] == ' ':
      currentWord = currentWord[:i] + ' ' + currentWord[i+1:]
      
  
  #--MAIN IN-GAME LOOP--
  while True:
    #--DISPLAY GAME UI-- 
    print 'Word so far: ', 
    for i in currentWord:
        print i + ' ',
    print '\nGuesses remaining: %d' %(guesses)
    print 'Incorrect guesses: ' + guessHistory + '\n'
    
    #--USER INPUT + VALIDATION LOOP-- 
    while True:
      #prompt player for letter
      guessLetter = requestString("Guess a letter")
      #loop until it is a verified single letter
      while len(guessLetter) != 1 or guessLetter.isalpha() == false:
        guessLetter = requestString("Guess A LETTER!")
      #convert to uppercase
      guessLetter = guessLetter.upper()
      #if letter is repeated, repeat user input loop. else, continue.
      if guessLetter in guessHistory or guessLetter in currentWord:
        print 'You already guessed this letter. Try again.\n'
      else:
        break
        
    #--UPDATE VARIABLES--
    #check if guess was correct
    if guessLetter in answer:
      print 'Correct!'
      #if correct, update current word
      for i in range(len(answer)):
        if answer[i] == guessLetter:
          currentWord = currentWord[:i] + guessLetter + currentWord[i+1:]
    else:
      print 'Incorrect.'
      #if incorrect, add to history of guess letter and decrease guess chances
      guessHistory = guessHistory + guessLetter
      guesses = guesses - 1
      
    #--GAME OVER CHECKS--
    if guesses == 0:
      print 'GAME OVER. Better luck next time!'
      break
    elif currentWord == answer:
      print 'Yes, the answer was ' + currentWord
      print 'YOU WIN! Congratulations!'
      break