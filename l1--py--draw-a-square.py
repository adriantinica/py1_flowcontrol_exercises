
# draw a rectangle  by * with measurement given by user

rectangle_hight = int(input(" Give a hight max 20 : "))
rectangle_width  = int(input(" Give a width max 20 : "))
surface = rectangle_hight * rectangle_width

n= 1
if rectangle_hight > 20  and rectangle_width > 20:
    print ( "ERROR")
else:
    while n <= surface:
        print ( "#" , "", end = "")
        if n % rectangle_width == 0:
         print()

        n += 1
        
pass

