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

if int(user_age) < 15:
    print("your age is less that 15 years")
if int(user_age) == 15:
    print("your age 15 years old")
else:
    print("you are over 15 years old")

if int(user_age) < 23:
    print("your age is less that 23 years")
if int(user_age) == 23:
    print("your age 23 years old")
else:
    print("you are over 23 years old")

if int(user_age) < 13:
    print("your age is less that 13 years")
if int(user_age) == 13:
    print("your age 13 years old")
else:
    print("you are over 13 years old")

server_data = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum! Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum libero enim natus! Cum, corrupti ad "
text = (server_data.split(" "))

while "ad" in text:
    i = (text.index("ad"))
    del text[i]
# print(text)

while "Lorem" in text:
    x = (text.index("Lorem"))
    text[x] = "Hey you"
#print(text)
print(" ".join(text))