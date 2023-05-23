"""
immutable vs mutable

immutable = cannont change

mutable = can change
"""

#immutable types=
str
int
float
bool
bytes
tuple

#mutable types 
list 
set 
dict


#immutable example

x = (1,2)
y = x

x = (1,2,3)

print(x,y)


#mutable example

x = [1,2]
y = x

x[0] = 100

print(x,y)



#mutable example
def get_largest_numbers(numbers,n):
    numbers.sort() #side effect

    return numbers[-n:]

nums = [2,3,4,5,1,24,25,29,73]

print(nums)
largest = get_largest_numbers(nums, 2)
print(nums)



#list comprehension
x = [i for i in range(10)] #for loop inside of a list 

print(x)



x = [[] for i in range(10)]

print(x)



x = [[j for j in range(5)]for i in range(10)]

print(x)



x = [i for i in range(10) if i % 2 == 0]

print(x)



#function arguements and Parameter Types
#Example 1
def complicated_function(x,y): #postional parameters (in order)
    pass

complicated_function(1,2) #arguements 

#Example 2
def complicated_function(x,y):
    pass

complicated_function(y = 3, x = 7)



