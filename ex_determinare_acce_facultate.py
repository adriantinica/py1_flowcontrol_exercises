# Criterii de inscriere la UNIVERSITATE


 # DATE ale problemei

admission_level    = 7.0
real_level_of_user = input ("Nota Medie Reala : ")     # condition 1
real_level_of_user = float (real_level_of_user)

taxe_pay           = 10000
real_amount        = input ("Suma detinuta : ")        # condition 2 
real_amount        = float (real_amount)
 
big_brother_power  = (input ("Are tata cumatri DA / NU : "))     # condition 3
raspuns_preconizat = "DA"

# logic datas

 
Aprobat  = real_level_of_user >= admission_level or real_amount >= taxe_pay or big_brother_power == raspuns_preconizat  # valoare boolean

# output 

print ( "Raspuns :" , Aprobat )