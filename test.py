while True:
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")

    # Check if age is a valid number
    if not age.isdigit():
        print("Invalid age. Please enter a valid number for age.")
        continue

    # Check if name is not empty
    if not name:
        print("Invalid name. Please enter a valid name.")
        continue

    # If inputs are valid, break out of the loop
    break

print(f"Hello {name}, you are {age} years old.")
