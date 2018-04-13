#Rocky Moreno
#Lab 15 Problem 2

import calendar
from datetime import *

"""
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
print "You have " + str(daysTilBirthday.days) + " days until your birthday"
"""
###################################
#   Declaration of Independence   #
###################################

#print "The Declartion of Independence was ratified on: " 
#Monday July 4th, 1776)
#date = datetime(1901, 7, 4)
#print "%s  %s %sth, %s" % (date.day, date.month, date.day, date.year)  
#print date.strftime("%A %B %dth, %Y")





