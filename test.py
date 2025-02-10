user_name = input("What is your username: ")

if user_name:
    print(f"Thank you we got it {user_name}")
else:
    print("You need to enter a username")

user_age = input("How old are you: ")

if user_age is int:
    print(f"Thanks so much you are {user_age}")
else:
    print("This is not a valid age.")