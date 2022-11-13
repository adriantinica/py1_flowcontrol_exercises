# to create an short app that allow us to by a tiket to the cinema

# INPUT DATA
from os import system

movie_1 = " Terminator "
movie_2 = " Titanic "
movie_3 = " The Dark Waters "

movie_time_1 = " 18:00"
movie_time_2 = " 20:00"
movie_time_3 = " 17:00"
movie_time_4 = " 15:00"
movie_time_5 = " 12:00"
movie_time_6 = " 16:00"

movie_price_1 = 100
movie_price_2 = 130
movie_price_3 = 120
movie_price_4 = 150
movie_price_5 = 90
movie_price_6 = 170





system ("cls")
# Movie Board

print (
 f"""
 1. {movie_1} 
   a. {movie_time_1}
   b. {movie_time_2}
 2. {movie_2}
   a. {movie_time_3}
   b. {movie_time_4}
 3. {movie_3}
   a. {movie_time_5}
   b. {movie_time_6}
"""
)


  # logica data

movie_number = (input ( "Choose a movie: "))

if movie_number == '1':
    print (f" you have chosen ,  '{movie_1}' ")
    time= input (" Alege timpul: ")
    if time  == 'a':
      print (f" you choose {movie_time_1} , tiket cost {movie_price_1} lei" )
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_1
      print (f"Total spre achitare : {total} ")
    elif time == 'b':
      print (f" you choose {movie_time_2} , tiket cost {movie_price_2} lei" )
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_2
      print (f"Total spre achitare : {total} ")

elif  movie_number == '2' : 
    print (f" you have chosen , '{movie_2}' ")
    time= input (" Alege timpul: ")
    if time  == 'a':
      print (f" you choose {movie_time_3} , tiket cost {movie_price_3} lei" )
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_3
      print (f"Total spre achitare : {total} ")
    elif time == 'b':
      print (f" you choose {movie_time_4} , tiket cost {movie_price_4} lei" )   
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_4
      print (f"Total spre achitare : {total} ")
    elif  movie_number == '3' : 
      print (f" you have chosen , '{movie_3}' ")
      time= input (" Alege timpul: ")
    if time  == 'a':
      print (f" you choose {movie_time_5} , tiket cost {movie_price_5} lei" )
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_5
      print (f"Total spre achitare : {total} ")
    elif time == 'b':
      print (f" you choose {movie_time_6} , tiket cost {movie_price_6} lei" ) 
      quantity = int ( input ( "how many tickets : "))
      total = quantity * movie_price_1
      print (f"Total spre achitare : {total} ")  



