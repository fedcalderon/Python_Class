sandwich_orders = ['ham', 'turkey', 'sub', 'beef', ]
finished_sandwiches = []
print(sandwich_orders)
for sandwich in sandwich_orders:
    sandwich_orders.pop()
    sandwich_orders.pop()
    print(f"\nmaking your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
for finished_sandwich in finished_sandwiches:
    print(f"\nHere is your {finished_sandwich} sandwich.")
