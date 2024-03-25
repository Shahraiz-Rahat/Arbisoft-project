# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    # Print each number multiplied by 2
    print(num * 2)


#Looping through a range of numbers
for i in range(1, 6):
    print(i)

#Looping through a list of strings
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit.capitalize())

#Looping through a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")