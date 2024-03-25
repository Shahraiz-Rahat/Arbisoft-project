# class Recipe():

#     def __init__(self, dish, items, time) -> None:
#         self.dish = dish
#         self.items = items
#         self.time = time

#     def contents(self):
#         print("The " +self.dish + " has " + str(self.items) + \
#             " and takes " + str(self.time) + " mins to prepare")

# pizza = Recipe("Pizza", ['cheese','bread','tomato'], "45")
# pasta = Recipe("Pasta", ['penne','sauce'], "55")

# print(pizza.contents())


# # Define class MyFirstClass
# class MyFirstClass():
#     print("who wrote this")

#     # Define string variable called index
#     index = "Aurthor of the book"
#     # Define function hand_list()
#     def hand_list(self, philosopher, book):
#         # variable + “ wrote the book: ” + variable
#         print(self.index + " " + philosopher + " wrote the book: " + book)        
        

# # Call function handlist()
# whodunnit = MyFirstClass()
# whodunnit.hand_list("Sun Tzu", "The Art of War")

a = 5
class A:
      a = 7
      pass

class B(A):
      pass

class C(B):
      pass

c = C()
print(c.a())