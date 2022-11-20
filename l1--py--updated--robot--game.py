# de creat un joc in care un ronot R se misca stanga -- dreapta pe o harta (axa )iar directiile se inidca de la KB

from os import system

map_length       = 32
robot_place      = 6
bomb_place       = 2
bomb_place1      = 13
bomb_place2      = 7
recovery_place   = 18
recovery_place1  = 4
recovery_place2  = 9
direction        = ""
battery          = 100
Health           = 100


# LOGICAL DATA


while direction != "x":
    # startul ciclul de afisare al unei situatii
    system ("cls")
    n=1
    z=1
    print ("")
    
    
    for x in range(1, map_length+1):
        if n == robot_place:
            print ("🤖 " , end="")
        if n ==  bomb_place or n == bomb_place1 or n== bomb_place2 :    
            print ("💣", end="")
        if n == recovery_place or n == recovery_place2 or n == recovery_place1 :
            print ("⚡", end="")
        else:
            print ("-" , end="")
        n += 1
    print("")
    print ("Baterry" , battery, "%")        
    print (" Health", Health, "%")
    print ()

    # sfarsitul ciclului de afisare al unei situatii

    direction = (input("Indica directia (a/d):"))
    if direction == "a" and robot_place > 1 :
        robot_place -=1
        battery -= 1

    if robot_place == bomb_place or robot_place == bomb_place1 or robot_place == bomb_place2:
        Health -= 10  
    
    if robot_place == recovery_place or robot_place == recovery_place1 or robot_place == recovery_place2:
        Health += 10
    
        
    if direction == "d" and robot_place < map_length:
        robot_place +=1
        battery -= 1
        