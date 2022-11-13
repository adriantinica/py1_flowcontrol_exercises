# to draw an triangle with while function  from kb

layers = int( input("triangle_layers : "))

n = 0

if layers > 20 :
    print ("ERROR")
else:
     while n < layers:
        print (" " * (layers-n) , "#" * (2*n+1) )
        n += 1
