
#PARKING_PLACES = 7
#FREE_PLACE = 3

#print("#"*PARKING_PLACES*5)

#for place_index in range(1, PARKING_PLACES +1, FREE_PLACE-2):
#   if place_index == FREE_PLACE:
#       print("|   |", end="")
#    else:   
#        print("| X |", end="")
    

#print("\n","#"*PARKING_PLACES*5, sep="")

PARKING_PLACES = int(input("Total parking places : "))
FREE_PLACE = int ( input (" Indica locul liber : "))
X = int(FREE_PLACE / FREE_PLACE)

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1, X):
     if place_index == FREE_PLACE:
        print("|   |", end="")  
     else:
        print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")