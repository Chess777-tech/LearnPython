#step 3

#f-strings 

name = "larry"
print(f"My name is {name}")


#in operator 
a = [1,2,3,4] # more efficent way to iterate thru arrays, list, etc...

for x in a:
    print(x)


#list comprehension 
a = [1,2,3,]
[3*x for x in a] #for each x in a it will multiply by 3 

#exponents, divisons
5**2
5/2
5//2

#iterator through dictionary 
d = {1:5,2:10}
for k in d:
    print(k) #print the keys

for k in d.keys():
    print(k)

for v in d.values():
    print(v)



