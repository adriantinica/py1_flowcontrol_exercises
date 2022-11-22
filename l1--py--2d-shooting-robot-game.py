# to create a game in witch a robot will shoot a target ant it randomly reappears
from os import system
import random
from time import sleep

# INPUT DATA

rx=4    #  robot cords
kb_comands =""
bx = -1   # bullet cords
by = -1   # bullet cords

tx = 4    # target cords
ty = 3    # target cords

score = 0

while kb_comands != "x":
######### draw the map ###############
    system("cls")
    for y in range(1,11):
        for x in range (1,11):
            if x== rx and y == 10:
                print("🤖 ", end="")
            elif x == bx and y == by:
                print(" 🔥", end="") 
            elif x == tx and y == ty:
                print( "🎯 ", end="")
            else: print (" . ", end="")
        print()
    print("\nscore:", score)
    sleep(0.2)
######### draw the map ###############

######### fire comand ##############
    if by != -1:
        by -=1
        if bx ==tx and by == ty:
            ty = random.randint(1,7)
            tx = random.randint(1, 10)
            by = -1
            score += 10

        continue
######### fire comand ##############

######### comand controls ############
    
    kb_comands = input("Introdu directia a/d : ")
    if kb_comands == "a" and rx > 1:
        rx -=1 
    if kb_comands == "d" and rx < 10:
        rx +=1 
    if kb_comands == "s" :
        bx = rx 
        by = 10-1
    

######### comand controls ############