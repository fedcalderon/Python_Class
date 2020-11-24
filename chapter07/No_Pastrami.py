sandwich_orders = ['ham', 'turkey', 'sub', 'beef', 'Pastrami', 'Pastrami', 'Pastrami' ]
print("Sorry, we done run out of pastrami sandwiches.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)

