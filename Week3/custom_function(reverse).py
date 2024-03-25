coffees = ['Espresso','Latte','Cappuccino','Micchato','Americano','Decaf']

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)