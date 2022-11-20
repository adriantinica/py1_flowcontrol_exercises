
# show a robot position in a definit space and his sensors area.

cx = 5   # coordonata pe axa x
cy = 4   # coordonata pe axa y

for y in range (1,11):
    for x in range(1,11):
        if x == cx and y ==cy:
            print ("R" , end=" ")
        elif x == cx+1 and y == cy:
            print ("#", end=" ")
        elif x == cx-1 and y == cy:
            print ("#", end=" ") 
        elif x == cx and y == cy+1:
            print ("#", end=" ")  
        elif x == cx and y == cy-1:
            print ("#", end=" ")  
        elif x == cx+1 and y == cy:
            print ("#", end=" ")  
        elif x == cx+1 and y == cy+1:
            print ("#", end=" ")
        elif x == cx+1 and y == cy-1:
            print ("#", end=" ")
        elif x == cx-1 and y == cy-1:
            print ("#", end=" ") 
        elif x == cx-1 and y == cy+1:
            print ("#", end=" ")
        else:
            print ( ".", end=' ')
    print ()
print()



