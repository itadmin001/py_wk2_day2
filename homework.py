
#====================================== Exercise 1 ==========================================================#

# Using the given list, print out a filtered version of the list with only the numbers that are less than ten

alist = [1,11,14,5,8,9]

def filter_it(list):
    return ([num for num in list if num < 10])

print(filter_it(alist))


#====================================== Exercise 2 ==========================================================#

# Merge and sort the two lists below

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_sort():
    for num in l_2:
        l_1.append(num)

    return sorted(l_1)

print(merge_sort())




#====================================== Exercise 3 ==========================================================#

# Square every number from 1 to 15
from math import sqrt
def square():
    return [int(sqrt(x)) for x in range(0,16)] ##### int'd for brevity - would just have to remove for actual squares

print(square())



#====================================== Exercise 4 ==========================================================#

# Using List Comprehension and the given list, print out a 
# filtered list with only the names that start with the letter 'a'. 
# The names in the outputted list should be title cased and have no whitespace.
# Hint: There is an empty string at the end of the list you will need to account for.
names_list = ['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']
#expected output = ['Amy', 'Alex']

def comp(list):
    return [x.strip().title() for x in list if x.strip().startswith('A') or x.strip().startswith('a')]
print(comp(names_list))





#====================================== Exercise 5 ==========================================================#


# Print all Prime numbers from 1 to 100
# Hint: A Prime # is any # that is ONLY divisible by 1 and itself. So think 
# how you can iterate through the list of #s from 1 to 100 and check to see if its divisible by ANY # below it.
# The For/Each might be very helpful for this question. 
# https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/

# x = target number
# y is going to loop thru the factors
# f is going to store the factors
# if the factor count is 2 then x is prime


def is_prime():
    prime_numbers = []
    for x in range(2,101):
        f = 0
        for y in range(1,x+1):
            if x % y == 0:
                f+=1
        if f == 2:
            prime_numbers.append(x)

    return prime_numbers

print(is_prime())