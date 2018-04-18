#Rocky Moreno, Daniel Howe, Jiwanjot Sandhu
#Lab 15 Prob 1

from random import randrange
from time import *

win = [7,11]
lose = [2, 3, 12]
playCount = 0
totalPoints = 0
firstPointTracker = 0

keepPlaying = 'y'

while keepPlaying == 'y':
  
  print "Rolling dice"
  die1 = randrange(1,6)
  die2 = randrange(1,6)
  playCount = playCount + 1
  totalDiePoints = die1 + die2

  sleep(1)

  if playCount == 1 and totalDiePoints in win:
    print "You got " + str(totalDiePoints) + " total points on that roll!" 
    print "YOU WON!"
    break  
  elif playCount == 1 and totalDiePoints in lose:
    print "You got " + str(totalDiePoints) + " total points on that roll!"
    print "YOU LOSE"
    break  
  elif playCount == 1:
    print "You got " + str(totalDiePoints) + " total points on that roll!"
    totalPoints = totalDiePoints
    firstPointTracker = totalPoints
    
    
  if playCount > 1 and totalDiePoints == firstPointTracker:
    print "YOU WIN"
    #print 'printing totalDiePoints from playcount > 1'
    #print totalDiePoints
    #print 'printing firstPointTracker from playcount > 1'
    break  
    
  elif playCount > 1 and totalDiePoints == 7:
    print "YOU LOSE!"
    #print 'printing from playcount > 1 total die points'
    #print totalDiePoints
    break  
    
  elif playCount > 1:
    totalPoints = totalPoints + totalDiePoints
    print "You have " + str(totalPoints) + " points! Keep it up!"
    
  playCount = playCount + 1
     
  
  keepPlaying = raw_input("Keep rolling? y or n: ")
  
print "Thanks for playing! " 
  
  
  
  
  
  