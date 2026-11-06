print("create an account")
while True:
    user_name = input("Pick a user name : ")
    if not user_name.isalpha():
        print("username can contian only letters")
    elif len(user_name) < 4:
        print("username can only contain 4 or more letters")
    else:
        break

while True:
    age =input("Enter your age : ")
    if not age.isdigit() :
        print("age can only contain number")
        continue
    ag = int(age)
    if ag >= 18 :
        print("Done") 
        break
    elif ag >= 12 :
        print("You are  currently creating a junior account")
        break
    elif ag >= 99:
        print("oops you are too old , you cannot create an account")
    else:
        print("oops you are too young, you cannot create an account ")
        exit()
while True:
    password = input("Create a password :")
    if len(password) >= 6:
        break
    else:
        print("password can only contain more than 6 charaters")
        print("try again")
else:
    print("Account created successful")

print("Login to you account")

name = input("Enter your username : ")
passkey = input("Enter your password : ")

while passkey != password :
    print("incorrect password")
    print("try again")
    passkey = input("Enter your password : ")

while user_name !=name:
    print("invaild username")
    print("try again")
    name = input("Enter your username : ")

print("Login successful")