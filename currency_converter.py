name = str(input("Enter your name:  "))
print (f"Hi {name}, WELCOME TO EMMEX CONRENCY CONVERTER")

amount = int(input(" enter amount to convert:  "))
usd_rate = 1500    
eur_rate = 1600    
gbp_rate = 1800    

converted_amount_to_usdt = amount/ usd_rate
converted_amount_to_eur = amount/ eur_rate 
converted_amount_to_gbp = amount/ gbp_rate

print( f"Hi{name}! Your Entered Amount to convert is ₦{amount:.2f} \n The converted amount is approximately: \n ${converted_amount_to_usdt:.2f} USD \n €{converted_amount_to_eur:.2f} EUR \n £{converted_amount_to_gbp:.2f} GBP" )