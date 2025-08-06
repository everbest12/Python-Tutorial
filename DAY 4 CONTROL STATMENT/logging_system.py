#DAY4 LOGGIN SYSTEM
print("========================")
print("WELCOME TO EMX PORTAL")
print("========================")

username = ("Emmanuel")
password = ("1234rty6")
attempts = 3

while attempts > 0:
    user_name = str(input("Please Enter your username:   ")).strip()
    pass_word = input("Enter your password:   ").strip()

    successful_login = (" You have successfully logged in")
    failed_login = ("Incorrect Password")
    username_not_found = ( " username not found ")
    
    if user_name.lower() != username.lower():
        print(username_not_found)
    elif pass_word != password:
        print(failed_login)
    else:
        print(successful_login,f"{username}" )
        break
    
    attempts -= 1
    if attempts > 0:
        print(f"Remaining attempts: {attempts}")
    else:
        print(" You’ve been locked out after 3 failed attempts.")
