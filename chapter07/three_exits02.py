toppings = "\nHello there! Please input the toppings you would like on your pizza:\n"
toppings += "(Press 'Q' to quit at any time.)\n"
message = ""
while message != 'Q':
    message = input(toppings)

    if message == 'Q':
        break
    else:
        print(f"Adding {message}")
