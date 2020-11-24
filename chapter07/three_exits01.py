toppings = "\nHello there! Please input the toppings you would like on your pizza:\n"
toppings += "(Press 'Q' to quit at any time.)\n"

active = True

while active:
    requested_topping = input(toppings)

    if requested_topping == 'Q':
        active = False
    else:
        print(f"Adding {requested_topping}")
