# ------------------------ Section 9 "Built in functions" is from part 1 to 9   -----------------------------

# # # # # # # # # #  part 1 (Map Function) # # # # # # # # #
""" 
# map is used to aply iterable(list) to a function.

def ferhernheit(temp):
    return (9.0/5)*temp + 32

temp_list = [0,22,33,100]

print(list(map(ferhernheit,temp_list)))

# we can used lambda expression 
print(list(map(lambda n: (9.0/5)*n + 32, temp_list)))

print('*'*100)
##### map can be used with more than one argument:
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(list(map(lambda x,y:x+y,a,b)))# taking the a[0] adding to b[0] and so on.
print(list(map(lambda x,y,z:x+y+z,a,b,c)))# taking the a[0] adding to b[0] adding to c[0] and so on.
"""
#--------------------------------------------------------
# # # # # # # # # #  part 2 (Reduce  Function) # # # # # # # # #
""" 
# Many times students have difficulty understanding reduce() so pay careful attention to this lecture.
#  The function reduce(function, sequence) continually applies the function to the sequence. 
# It then returns a single value.

# If seq = s1, s2, s3, ... , sn , calling reduce(function, sequence) works like this:
# At first the first two elements of seq will be applied to function, i.e. func(s1,s2)
# The list on which reduce() works looks now like this: function(s1, s2), s3, ... , sn
# In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
# The list looks like this now: function(function(s1, s2),s3), ... , sn
# It continues like this until just one element is left and return this element as the result of reduce()
# Let's see an example:
from functools import reduce

lst = [32,44,25,55,10]
print(reduce(lambda x,y:x+y,lst)) # returning one singel value

def max_find(a,b):
    if a>b :
        return a
    else:
        return b

print(reduce(lambda a,b : a if a>b else b, lst)) # this lambda expression is equal max_find function
"""
#--------------------------------------------------------
# # # # # # # # # #  part 3 (Filter Function) # # # # # # # # #
""" 
# filter is used to filter a list applied to function which is having TRUE result.
lst = [1,3,43,52,63,7,8,9]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(list(filter(is_even,lst)))
print(list(filter(lambda num : num %2 == 0,lst))) # is even

print(list(filter(lambda num : num >= 9,lst))) # greater than nine
"""
#--------------------------------------------------------
# # # # # # # # # #  part 4 (Zip Function) # # # # # # # # #

'''
# Zip is joining two iterables together and the result will be TUPLE PAIRS
a = [1,2,3]
b = [4,5,6]
c= [7,8,9,10,11,12]

print(list(zip(a,b)))
print(list(zip(a,c)))# Zip gives Tuples based on the smaller size 
#(a is smaller than c so the Tuples will be based on a lenght)


# trying to find a max of zipped list
for item in zip(a,b):
    print(max(item))

# Zip with Dictionary
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}

print(list(zip(d1.items(),d2.items())))
print(list(zip(d1.keys(),d2.values()))) # swapping the values from d2 to d1 
print(list(zip(d2.keys(),d1.values()))) # swapping the values from d1 to d2 
''' 
#--------------------------------------------------------
# # # # # # # # # #  part 5 (Enumerate Function) # # # # # # # # #

''' 
# enumerate will make a counter to an iterable(list)
lst = ['a','b','c']

for item in lst:
    print(item)

for i,item in enumerate(lst):
    print(f"({i},{item})")

for i,item in enumerate(lst): # TUPLE UNPACKING , COUNTER FIRST (I or N) and then the ITEM it self
    if i >=2 :
        break
    else: 
        print(item)
'''
#--------------------------------------------------------
# # # # # # # # # #  part 6 (all() and any() Function) # # # # # # # # #

''' 
# ALL: is taking a list of booleans , if all are true i return true else it returns false
# ANY: is taking a list of booleans , if any of them is true return true else returns false
lst = [True,True,False,False]
print(all(lst))
print(any(lst))
'''
#--------------------------------------------------------
# # # # # # # # # #  part 7 (Complex Function) # # # # # # # # #

''' 
# COMPLEX Function is to make a complex number: (which contains a real and imaginary number) (e.g 2 + 5j)
# it can deals with string or numbers 

print(complex(2,3))
print(complex(2))
print(complex('2+5j'))
'''
#--------------------------------------------------------
# # # # # # # # # #  part 8 (Built-in Functions Assessment Test) # # # # # # # # #

# # # # # # # # # #  part 9 (Built-in Functions Assessment Test - Solution) # # # # # # # # #

