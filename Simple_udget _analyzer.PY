print (" Simple Budget Analyzer ")

name = str(input("Please Enter Your name:  "))
monthly_income = int(input("Please Enter Your monthly income:  "))

rent = int(input("Enter how much you spend on rent:  "))
food = int(input("Enter how much you spend on food:  "))
transport = int(input("Enter how much you spend on transport:  "))
utilities = int(input("Enter how much you spend on utilities:  "))
miscellaneous = int(input("Enter how much you spend on miscellaneous:  "))

total_expenses = (rent + food + transport + utilities + miscellaneous)
remaining_savings = (monthly_income - total_expenses)
percentage_spent = (total_expenses / monthly_income)* 100


print(f"""
----------------------------------------------
Hi {name}! Here's your budget breakdown:
Your income is : {monthly_income:.2f} 
Your expenses are:  
    - Rent:  {rent:.2f}
    - Food:  {food:.2f} 
    - Transport:  {transport:.2f} 
    - Utilities:  {utilities:.2f} 
    - Miscellaneous: {miscellaneous:.2f} 
    
    - Total Expenses: {total_expenses:.2f} 
    - Remaining Savings:  {remaining_savings:.2f} 
    - Income spent {percentage_spent:.1f}% of your income this month.
    """)

if total_expenses > monthly_income:
    print("⚠️ Warning: You're spending more than you earn!")
else:
    print(" Youre spending Wisely")