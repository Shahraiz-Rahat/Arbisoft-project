menu = ['Espresso','Latte','Cappuccino','Micchato','Americano','Decaf','cortado']

def find_coffees(coffee):
    if coffee[0] == 'C' or coffee[0] == 'c':
        return coffee

# Map allow to apply a function on whole list
map_coffee = map(find_coffees, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

#Filter do the same but it takes the result and create a new list 
filter_coffee = filter(find_coffees, menu)
print(filter_coffee)
for x in filter_coffee:
    print (x)