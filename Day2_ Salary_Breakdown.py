# DAY 2- SALARY BREAKDOWN
print ("WELCOME ")

name = str(input("Please enter your name: "))
Monthly_Salary = int(input("Please Enter your Monthly salary. eg $20,000 :  "))
Gross_Annual_Salary = Monthly_Salary * 12
Tax = (Gross_Annual_Salary * 10) / 100
Net_Annual_Salary = Gross_Annual_Salary - Tax

print (f" Your Monthly Salary is: {Monthly_Salary} \n Your Yearly Tax is: {Tax} \n your Gross Annual Salary is: {Gross_Annual_Salary} \n Your Net Annual Salary is: {Net_Annual_Salary} ")
