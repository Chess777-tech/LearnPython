#variables 
x = 1
x = x + 2
print(x)


#strings 
x = "abc"
y = "de"
z = x = y 
z 
#taking a slice
z = z[1:3]
z

#functions 
def f(x):
    y = x + 2 #added 2 to 5 
    return y 
f(5)

#if statements 
x = 2
if x + 1 == 3: #is this going to be true??
    print(x)


#loops 
for i in range(1,100):
    if i % 2 == 0: #fancy way of saying i is even
        print(i)

