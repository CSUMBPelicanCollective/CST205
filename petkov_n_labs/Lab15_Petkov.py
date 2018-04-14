# Lab 15 - April 17, 2018 - Nikola Petkov

# Problem 1 - a game of Craps.
from random import randint

def die():
  roll = randint(1, 6)
  return roll

def problem1():
  showInformation("Let's play Craps! Click OK to roll the dice.")
  thePoint = 0   # The roll on first run becomes the point.
  rollNum = 1    # Keeps count of the number of rolls.
  while True:
    rolled = die() + die()    # Get the total of 2 rolled dice.
  
    if ((rolled == 7 or rolled == 11) and rollNum == 1) or (rolled == thePoint and rollNum > 1): # 7 or 11 on first roll. The point on subsequent rolls.
      showInformation("You won! You rolled " + str(rolled))
      print("You won! You rolled " + str(rolled) + " on run " + str(rollNum))
      break
    elif ((rolled == 2 or rolled == 3 or rolled == 12) and rollNum == 1) or (rolled == 7 and rollNum > 1): # 2, 3, or 12 on first roll. 7 on subsequent rolls.
      showInformation("You lost! You rolled " + str(rolled))
      print("You lost! You rolled " + str(rolled) + " on run " + str(rollNum))
      break
    elif rollNum == 1:    # The number rolled on the first run becomes the point.
      thePoint = rolled
      showInformation("You rolled " + str(rolled) + ". The point is " + str(thePoint))
      print("You rolled " + str(rolled) + ". The point is " + str(thePoint))
    else:
      showInformation("You rolled " + str(rolled) + ". Roll again.")
      print("You rolled " + str(rolled) + ". Roll again.")
  
    rollNum += 1


# Problem 2 - Prints the calendar of the month in the year you were born; How many days left until your next birthday; Day of the Declaration of Independence.
def problem2():
  from calendar import setfirstweekday, prmonth, weekday, day_name, month_name
  from datetime import date

  setfirstweekday(6)       # Set the week to start on Sunday.
  prmonth(1988, 2, 5, 1)   # Prints the month in a given year (with optional spacing).

  today = date.today()
  birthday = date(2019, 2, 13)        # Enter the date of your upcoming birthday to calculate how many days left.
  print str((birthday - today).days) + " days left until your birthday."

  independenceDay = date(1776, 7, 4)  # Independence Day.
  independenceDayD = day_name[independenceDay.weekday()]
  independenceDayM = month_name[independenceDay.month]
  independenceDayY = independenceDay.year
  print "Independence was declared on " + independenceDayD + ", " + independenceDayM, str(independenceDay.day) + ", " + str(independenceDayY)