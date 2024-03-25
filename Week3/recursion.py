def find_factorial_by_looping(n):
    if n<0:
        return 0
    else:
        factorail = 1
        for i in range(1, n+1):
            factorail = factorail*i
        return factorail
print(find_factorial_by_looping(5))


def find_factorial_recursive(n):
    if n ==1 :
        return 1
    else:
        return n * find_factorial_recursive(n-1)

print (find_factorial_recursive(5))  

def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)