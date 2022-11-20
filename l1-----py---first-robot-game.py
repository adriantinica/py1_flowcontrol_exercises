# de creat un joc in care un ronot R se misca stanga -- dreapta pe o harta (axa )iar directiile se inidca de la KB

from os import system

map_lenght = 15
robot_place = 3
direction = ""
# LOGICAL DATA


while direction != "x":
    # startul ciclul de afisare al unei situatii
    system ("cls")
    n=1
    print ("")
    while n <= map_lenght:
        if n == robot_place:
            print ("R", end="")
        else:
            print ("-", end="")
        n += 1
    print ("")

    # sfarsitul ciclului de afisare al unei situatii

    direction = (input("Indica directia (a/d):"))
    if direction == "a":
        robot_place -=1
    if direction == "d":
        robot_place +=1





