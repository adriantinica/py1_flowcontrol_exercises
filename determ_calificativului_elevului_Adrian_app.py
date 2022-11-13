#  de identificat calificativul notei elevului in 3 intervale
#   Excelent, Satisfacator, Rau

# INPUT DATA

nota_elevului = int ( input (" Indica nota reala "))

from os import system
system ("cls")

from time import sleep
sleep (3)

# LOGICAL DATA

if nota_elevului >=1 and nota_elevului <= 4 :
    print ( "Rau")
elif nota_elevului >=5 and nota_elevului <= 7 :
    print ( "Satisfacator")
elif nota_elevului > 7 and nota_elevului <= 10:
    print ("Excelent")
else :
     print ( " Error , datele introduse nu se incadreaza in intervalul 1 - 10 ")