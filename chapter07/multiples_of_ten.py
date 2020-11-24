number = input("Welcome user! Input a number and I'll tell you if it's a multiple of ten:\n ")
number == int(number)



if int(number) % 10 == 0:
    print(f"{number} is a multiple of ten")
else:
    print(f"{number} is not a multiple of ten")

