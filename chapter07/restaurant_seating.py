party_size = input('\nWelcome to the restaurant! Please input the amount of people in your group:\n')
party_size = int(party_size)


def can_be_seated():
    if party_size  <=8:
        print("Your table is ready!")
    else:
        print("Your party is bigger than 8 people. You'll have to wait for a table.")


can_be_seated()