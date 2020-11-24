groceries = "\nHello there! Please enter the groceries you would like in your cart:\n"
groceries += "(Press 'Q' to quit at any time.)\n"

while True:
    requested_topping = input(groceries)

    if requested_topping == 'Q':
        break
    else:
        print(f"Adding {requested_topping}")
