

start_n  = int (input(" Input the start n :"))
end_n    = int (input (" Input the end n :"))




if start_n < end_n:
    
    for n in range(start_n , end_n+1):
        print(n)
        
elif start_n > end_n:

   for n in range(start_n , end_n-1, -1):
        print (n)


    