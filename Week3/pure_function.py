######

my_list = [1,2,3,4]

def add_to_list(item):
    return my_list.append(item)

add_to_list(5)

print(my_list)

######

my_list1 = [1,2,3,4]

def add_to_list(item):
    my_list1.append(item)
    return my_list1

new_list = add_to_list(5)

print(new_list)
print(my_list1)

######

my_list2 = [1,2,3,4]

def add_to_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list2 = add_to_list(my_list2,5)

print(new_list2)

print(my_list2)