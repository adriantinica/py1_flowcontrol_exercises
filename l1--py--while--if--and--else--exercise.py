#Citeasca de la tastatura doua variabile start_n si end_n
#Sa se modifice codul de mai sus in asa mod incat daca utilizatorul introduce prima valoare mai mica
#  si cea de a doua mai mare (de ex: 5 si 10) ciclul sa afiseze toate valorile in ordine crescatoare de la 5 la 10, iar daca valorile se introduc invers (de ex: 10 si 5) sa se afiseze toate numerele intregi in ordine descrescatoare din acest diapazon
#Utilizati if/else pentru a solutiona acest exemplu

start_n  = int (input(" Input the start n :"))
end_n    = int (input (" Input the end n :"))




if start_n < end_n:
    n=start_n
    while n <= end_n :
        print(n)
        n += 1 
elif end_n < start_n:
    n= start_n
    while n >= end_n:
        print(n)
        n -= 1
pass