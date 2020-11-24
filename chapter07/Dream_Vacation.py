responses = {}

polling_active = True

while polling_active:
    name = input("What's your name?\n")

    response = input("\nWhere would you like to take a vacation?\n")
    responses[name] = response
    repeat = input("\nWould any one else like to take the poll? (Y,N)\n")
    if repeat == 'N':
        polling_active = False

    print("\n---Poll Results---")
    for name, response in responses.items():
        print(f"{name} would like to go to {response}.")