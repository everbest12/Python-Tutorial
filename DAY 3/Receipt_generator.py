# DAY 3 Receipt Generator
from datetime import datetime
name = str(input("Please Enter your correct name:  "))


first_item = str(input(" Enter name of first item:  "))
first_item_price = int(input(" ₦{Price:  "))
second_item = str(input(" Enter name of second item:  "))
second_item_price = int(input(" ₦{Price:  "))
third_item = str(input(" Enter name of third item:  "))
third_item_price = int(input(" ₦{Price:  "))

total = (first_item_price + second_item_price + third_item_price )

print("\n============= EMMEX SHOP RECEIPT =============")
print(f"Customer Name: {name}")
print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
print("----------------------------------------------")
print(f"{'Item':<20}{'Price':>15}")
print("----------------------------------------------")
print(f"{first_item:<20}₦{first_item_price:>13,.2f}")
print(f"{second_item:<20}₦{second_item_price:>13,.2f}")
print(f"{third_item:<20}₦{third_item_price:>13,.2f}")
print("----------------------------------------------")
print(f"{'Total':<20}₦{total:>13,.2f}")
print("==============================================")
print(f"Thank you for shopping with us, {name}!\n")