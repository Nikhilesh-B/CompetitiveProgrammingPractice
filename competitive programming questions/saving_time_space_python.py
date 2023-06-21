a = [1,2,3,4]
b = ['e','c','d']


#zipping object 
for x,y in zip(a,b):
    print("a=",x)
    print("b=",y)

lst = list(zip(a,b))
print("Unosrted list=", lst)
lst.sort(key= lambda x: x[0],reverse=True) #in -place sorting 
print("Sorted lst=", lst)


#Dictionary comprehensions
from collections import Counter
#frequency 
fruits = ["Apple", "Orange", "Pear"]

fruit_freq = Counter(fruits)

print(fruit_freq)
print(dict(fruit_freq))


#letter count

fruit_word_len = {f:len(f) for f in fruits} 
print(fruit_word_len)


#List comprehensions 
#instead of 

things = ['thing1', 'thing2']
two_d_things = []

for thing in things:
    two_d_things.append(thing)

print(two_d_things)
two_d_things = [thing for thing in things]
print(two_d_things)