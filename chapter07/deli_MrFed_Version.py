
"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names
of various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order,
such as I made your tuna sandwich. As each sandwich is made, move it to
the list of finished sandwiches. After all the sandwiches have been made,
print a message listing each sandwich that was made.
"""


sandwich_orders = ['ham', 'turkey', 'sub', 'beef' ]
finished_sandwiches = []

print(f"\nsandwich orders: {sandwich_orders}")
print(f"finished sandwiches: {finished_sandwiches}\n")

list_size = len(sandwich_orders)
while list_size != 0:
    print(f"making your {sandwich_orders[0]} sandwich.")
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.pop(0)
    list_size = len(sandwich_orders)

print(f"\nsandwich orders: {sandwich_orders}")
print(f"finished sandwiches: {finished_sandwiches}\n")

for finished_sandwich in finished_sandwiches:
    print(f"Here is your {finished_sandwich} sandwich.")
