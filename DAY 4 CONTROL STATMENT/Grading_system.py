#DAY 4: GRADING SYSTEM
print ("+===============================+")
print ("WELCOME TO MILDIVE COLLEGE")
print ("+===============================+")

name = str(input("Please Enter your name:  "))
age = int(input("Please Enter your age:  "))
exam_score = int(input("Please Enter your exam score (from 0-100):  "))

max_score = 100
min_score = 0
if exam_score > max_score or exam_score < min_score :
    message = ("Please enter a valid score from 0-100")
    print (message)
    exit() 
    
print(".....................................................................")
print(f"Hi {name}! Your entered score is {exam_score}, and your grade is: ")


if  90 <=  exam_score  <= max_score :
    print("EXCELLENT (A)")
elif  80 <= exam_score <= 89:
    print("VERY GOOD (B)")
elif 70 <= exam_score <= 79:
    print("GOOD (C)")
elif 60 <= exam_score  <= 69:
    print("FAIR (D)")
elif 50 <= exam_score  <= 59:
    print("POOR (E)")
else:
    print ("FAIL(F)")