user_name = input("Enter your name : ")
print(user_name.lower().capitalize())

user_surname = input("Enter your surname : ")
print(" ".join(user_surname).upper())

user_age = input("How old are you ? ")
import datetime
current_yaer = datetime.datetime.now().year
print("year of your birth", int(current_yaer) - int(user_age))

if int(user_age) < 13:
    print("you are a child")
if int(user_age) > 23:
    print("you are an adult")
else:
    print("you are a teenager")

