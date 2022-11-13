
# determinarea virstei si incadrarea in una din categorii

# INPUT DATA

anul_curent = 2022
anul_nasterii = int (input ("Indica anul nasterii : ") )

virsta_utilizatorului = anul_curent - anul_nasterii
if virsta_utilizatorului >= 122:
    print ( "eroare diapazon")
elif virsta_utilizatorului >= 1 and  virsta_utilizatorului <= 3:
    print ( "baby" , virsta_utilizatorului , "ani" )
elif  virsta_utilizatorului <= 9 :
    print ( "kid" , virsta_utilizatorului , "ani" ) 
elif  virsta_utilizatorului <= 15:
    print ( "teen" , virsta_utilizatorului , "ani" )  
elif  virsta_utilizatorului <= 18:
    print ("young" , virsta_utilizatorului , "ani")
elif  virsta_utilizatorului <= 50:
    print ( "adult" , virsta_utilizatorului , "ani")
else :
    print ( "old" , virsta_utilizatorului, "ani")

pass