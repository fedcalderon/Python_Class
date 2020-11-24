users = []
user_counter = 0

user = {
    'first_name':'',
    'last_name':'',
    'age':0,
    'location': '',
    'weight':0
}

def collect_userdata():
    """
    This Function collects User data
    :return: none
    """

    exit = 0
    while (exit == 0):
        

        first_name = input("Hello! Type first name: ")
        print(first_name)
        last_name = input("Hello! Type last name: ")
        print(last_name)
        age = input("Hello! Type age: ")
        print(age)


        user['first_name'] = first_name
        user['last_name'] = last_name
        user['age'] = age

        if int(age) >= 18:
            user['can_vote'] = 'Yes'
        else:
            user['can_vote'] = 'No'

        for k,v in user.items():
            print(f"First name: {user['first_name']}")
            print(f"Last name: {user['last_name']}")
            print(f"Age: {user['age']}")
            print(f"can vote? {user['can_vote']}")
        message = input("want to quit? (Y, N):")
        if message == 'Y':
            exit = 1
            print("Exiting Program.")

def While_Loops_Priniciples():

    exit = 0

    while (exit != 1) :
        message = input("tell me your name: ")
        print(f"hello {message}!")

        message = input("tell me your age: ")
        print(f"you are {message}!")

        message = input("want to quit? (Y, N):")
        if message == 'Y':
            exit = 1
            print("Exiting Program.")




def show_help():
    print("Thank you for using this product.")
    print("We are learning about user input and while loops.")

collect_userdata()