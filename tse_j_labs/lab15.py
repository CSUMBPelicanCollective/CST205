#Lab 15

#PROBLEM 1
import random

#returns random integer from 1 to 6
def rollDice():
  return random.randint(1,6)

#runs instance of game of craps    
def craps():
  firstRollWin = [7,11]
  firstRollLose = [2,3,12]
  isFirstTurn = true

  while True:
    dice1 = rollDice()
    dice2 = rollDice()
    print "You rolled a %d and a %d." % (dice1, dice2)
  
    diceSum = dice1 + dice2
    print str(diceSum) + ",",
  
    if isFirstTurn:
      if diceSum in firstRollWin:
        print "you win!"
        break
      elif diceSum in firstRollLose:
        print "you lose!"
        break
      else:
        print "roll another %d to win.\n" % (diceSum)
        point = diceSum
        isFirstTurn = false
    else:
      if diceSum == point:
        print "you win!"
        break
      elif diceSum == 7:
        print "you lose!"
        break
      else:
        print "roll again.\n"
  

#PROBLEM 2
import datetime 
import calendar 

#prints out calendar of birth month during birth year
def birthMonth():
  try:
    year = input("What year were you born? : ")
  except:
    print "Numeric values for year only."
    return
    
  month = raw_input("What month were you born? : ") 

  try:
    if not month.isdigit():
      month = list(calendar.month_abbr).index(month[:3]) #if month is written out, convert to number 
  except:
    print "What month was that?"
    return 
 
  try:
    print(calendar.month(year, int(month)))
  except:
    print "When was that?"
    return 
    
    
    
#Prints how many days till birthday
def birthdayCountdown():
  month = raw_input("What month were you born? : ") 
  day = input("What day were you born? : ")
  
  try:
    if not month.isdigit():
      month = list(calendar.month_abbr).index(month[:3]) #if month is written out, convert to number 
  except:
    print "What month was that?"
    return 
    
  #determine year
  nextBday = datetime.date((datetime.date.today()).year, int(month), day)
  if nextBday < datetime.date.today():                   #if date passed this year, add a year
    nextBday += datetime.timedelta(days=365)
    
  print str((nextBday - datetime.date.today()))[:-9] + " until your birthday."
  
  
  
#Prints out full date of Declaration of Independence ratification
def independenceDate():
  independenceDay = datetime.date(1776, 7, 4)
  weekDay = independenceDay.weekday()
  
  print calendar.day_name[weekDay] + " July 4th, 1776"