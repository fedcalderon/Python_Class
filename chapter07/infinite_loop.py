age = input("Hello there, please enter your age:\n")
age = int(age)
while True:
    if age <= 3:
        print("Your movie ticket is free.")
    elif (age > 3) and (age < 12):
        print("Your ticket is 10$")
    elif age > 12:
        print("Your ticket is 15$")
