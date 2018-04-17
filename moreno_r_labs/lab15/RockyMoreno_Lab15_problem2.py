#Rocky Moreno
#Lab 15 Problem 2

import calendar
from calendar import setfirstweekday, prmonth, weekday, day_name, month_name
from datetime import *


#PROBLEM 2 -----------------------------

########################################
#   print out calendar of month born   #
########################################

year = requestInteger("Enter the year born")
month = requestInteger("Enter the month") 
showInformation(calendar.month(1979, 11, 0, 0))
print (calendar.month(year, month, 7, 1))




#########################################
#   How many days until next birthday   #
#########################################

todaysDate = datetime.today()
year = requestInteger("Enter the birth year")
month = requestInteger("Enter the birth month") 
day = requestInteger("Enter the birth day")

currentYear =  datetime.now() #get now date
currentYear = currentYear.year # extract year
currentYear = currentYear - year # get year difference
currentYear = currentYear + year # add year different to birth year

#print currentYear 

birthDate = date(currentYear, month, day)

#print todaysDate
#print birthDate

daysTilBirthday = (birthDate - todaysDate)
showInformation ("You have " + str(daysTilBirthday.days) + " days until your birthday")

###################################
#   Declaration of Independence   #
###################################

showInformation ("The Declartion of Independence was ratified on: " )
#Monday July 4th, 1776
declaration = date(1776, 7, 4)  # Independence Day.
declarationDay = day_name[declaration.weekday()]
declarationMonth = month_name[declaration.month]
declarationYear = declaration.year
print declarationDay + ", " + declarationMonth, str(declaration.day) + ", " + str(declarationYear)



