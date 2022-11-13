
# de creat un excchange app 
# a se introduce valorile
# a se crea convertirea in USD EUR MDL

# INPUT DATA


input_sell_currency =  ( input ("Introdu valuta vinzare  EUR / USD / MDL : "))
input_buy_currency  =   ( input ("Introdu valuta cumparar EUR / USD / MDL : "))



ex_rate_EUR_USD = 1.2
ex_rate_EUR_MDL = 20.3
ex_rate_USD_MDL = 19


# LOGICAL AND OUTPUT DATA

if input_sell_currency == "EUR" and input_buy_currency == "USD" :
 amount_EURO = int (input ("Suma EUR : "))
 EUR_USD = amount_EURO * ex_rate_EUR_USD
 print  (EUR_USD, "dollars")
elif input_sell_currency == "EUR" and input_buy_currency == "MDL":
 amount_EURO = int (input ("Suma EUR : "))
 EUR_MDL = amount_EURO * ex_rate_EUR_MDL
 print  ( EUR_MDL, " lei")
elif input_sell_currency == "USD" and input_buy_currency == "MDL":
 amount_USD = int (input ("Suma USD : "))
 USD_MDL = amount_USD * ex_rate_USD_MDL
 print ( USD_MDL , "lei")
 


