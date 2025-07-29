#DAY2

bill_amount = int(input("Enter Your bill Amount:  "))
Tip_percentage = int(input("Enter Tip percentage: "))

Tip = (bill_amount* Tip_percentage/100)
Total = (bill_amount + Tip)
print(f"Tip : {Tip}, Total: {Total}")