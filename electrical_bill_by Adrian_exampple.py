
# INPUT DATA
Consummer_name    = input ( " your name: " )
Consummer_adress  = input ( "your adress: ")

Initial_data_bill       = int ( input ( "initial data: "))    # sunt date introduse de user si vom opera cu ele ca numere intregi
month1_contor      = int ( input (" First month: "))
month2_contor      = int ( input (" Second month: "))
month3_contor      = int ( input (" Third month: "))
month4_contor      = int ( input (" Forth month: "))



import time
time.sleep(3)

electrical_index_kwh_mdl    = 5

# LOGIC DATA

consum_mth1 = month1_contor - Initial_data_bill
consum_mth2 = month2_contor - month1_contor
consum_mth3 = month3_contor - month2_contor           # consumul lunar de kwh 
consum_mth4 = month4_contor - month3_contor

total_consum  = month4_contor - Initial_data_bill

first_month_pay   = electrical_index_kwh_mdl * consum_mth1       
second_month_pay  = electrical_index_kwh_mdl * consum_mth2      # costul lunar al kwh
third_month_pay   = electrical_index_kwh_mdl * consum_mth3
fourth_month_pay  = electrical_index_kwh_mdl * consum_mth4

# variabile pentru grafic 

coloana_1 = int (100 * consum_mth1 / total_consum )
coloana_2 = int (100 * consum_mth2 / total_consum )
coloana_3 = int (100 * consum_mth3 / total_consum )
coloana_4 = int (100 * consum_mth4 / total_consum )

# OUTPUT DATA

print ( "kw consumati luna 1: " , consum_mth1 )
print ( "kw consumati luna 2: " , consum_mth2 )
print ( "kw consumati luna 3: " , consum_mth3 )
print ( "kw consumati luna 4: " , consum_mth4 ) 

print ( "total spre achitare mth1: " , first_month_pay )
print ( "total spre achitare mth2: " , second_month_pay)
print ( "total spre achitare mth3: " , third_month_pay)
print ( "total spre achitare mth4: " , fourth_month_pay)

print ( "consum total KWh: " , total_consum )

print ("GRAFICUL DE CONSUM ")

print ("#"* coloana_1 )
print ("#"* coloana_2 )
print ("#"* coloana_3 )
print ("#"* coloana_4 )


pass
