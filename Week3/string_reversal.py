
# #str[start:stop:step]


# trial= "reversal"
# new_trial = trial[::-1]

# print(new_trial)



numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)