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
#-------------------------------------------------------------------------------------------------
# # # # # # # # # #  part 8 & 9 (Built-in Functions Assessment Test & solutions) # # # # # # # # #
#-------------------------------------------------------------------------------------------------

#### Problem 1
'''
# Use map() to create a function which finds the length of each word in the phrase (broken by spaces)
#  and returns the values in a list.
# The function will have an input of a string, and output a list of integers.

# word_lengths('How long are the words in this phrase')
# [3, 4, 3, 3, 5, 2, 4, 6]

def word_lenghts(text):
    words = text.split()
    print(list(map(len,words))) 
word_lenghts('How long are the words in this phrase')

print('*'*100)
'''
#----------------------------------------------

####Problem 2
''' 
# Use reduce() to take a list of digits and return the number that they correspond to.
# For example, [1, 2, 3] corresponds to one-hundred-twenty-three. 
# Do not convert the integers to strings!

# digits_to_num([3,4,3,2,1])
# 34321
"""
TEACHER SOLUTION:
from functools import reduce

def digits_to_num(digits):
    
    return reduce(lambda x,y:x*10 + y,digits)
"""
from functools import reduce
def digits_to_num(lst):
    return reduce(lambda x,y:f"{x}{y}",lst)

print(digits_to_num([3,4,3,2,1]))

print('*'*100)
'''

#----------------------------------------------

####Problem 3
'''
# Use filter to return the words from a list of words which start with a target letter.

# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# filter_words(l,'h')
# result = ['hello', 'ham', 'hi', 'heart']

def filter_words(lst,letter):

    return list(filter(lambda x: x[0] == letter,lst)) 
    
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

print('*'*100) 
'''
#----------------------------------------------
####Problem 4
'''
# Use zip() and a list comprehension to return a list of the same length where
# each value is the two strings from L1 and L2 concatenated together with connector between them. 
# Look at the example output below:
# concatenate(['A','B'],['a','b'],'-')
# ['A-a', 'B-b']

"""
TEACHER SOLUTION:
def concatenate(L1, L2, connector):
    
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
"""


def concatenate(lst1,lst2,connector):
    result = list(zip(lst1,lst2))
    c_result = []
    for item in result:
        print(item)
        c_result.append(connector.join(item))
    
    return c_result


print(concatenate(['A','B'],['a','b'],'-'))

print('*'*100)
'''
#----------------------------------------------

#### Problem 5
''' # Use enumerate() and other skills to return a dictionary which has the values 
# of the list as keys and the index as the value. 
# You may assume that a value will only appear once in the given list.

# d_list(['a','b','c'])
# {'a': 0, 'b': 1, 'c': 2}

"""
TEACHER SOLUTION:
def d_list(L):
    
    return {key:value for value,key in enumerate(L)}
"""

def list_to_dict(lst):
    dic = {}
    Enumerated_list = enumerate(lst)
    for i,item in Enumerated_list:
        dict(Enumerated_list)
    return Enumerated_list

print(list_to_dict(['a','b','c']))

print('*'*100)
'''
#----------------------------------------------

#### Problem 6

''' 
# Use enumerate() and other skills from above to return the count of the number of items
#  in the list whose value equals its index.

# count_match_index([0,2,2,1,5,5,6,10])
# 4

"""
TEACHER SOLUTION:
def count_match_index(L):
       
    return len([num for count,num in enumerate(L) if num==count])
"""


def count_match_index(lst):
    x = enumerate(lst)
    counter = 0
    for i, item in x:
        if i == item:
            counter += 1

    return counter

print(count_match_index([0,2,2,1,5,5,6,10]))
'''

#--------------------- Comprehension LIST with examples 1-2-3-4-5-6 -----------------------

''' 
####Problem 1 
# word_lengths('How long are the words in this phrase')
# [3, 4, 3, 3, 5, 2, 4, 6]
def word_lengths(text):
    return [len(x) for x in text.split()]

print(word_lengths('How long are the words in this phrase'))
#---------------------------

####Problem 2
# digits_to_num([3,4,3,2,1])
# 34321
from functools import reduce
def digits_to_num(lst):
    # either
    return reduce(lambda x,y:x*10 + y , lst)
    # or
    return reduce(lambda x,y:f'{x}{y}',lst)
print(digits_to_num([3,4,3,2,1]))  
#---------------------------

####Problem 3
# without using Filter func
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
def filter_words(lst,letter):
    return [x for x in lst if x[0] == letter]

# with Filter func
def filter_words_f(lst,letter):
    return list(filter(lambda x:x[0] == letter,lst))
print(filter_words(l,'h'))
print(filter_words_f(l,'h'))
#---------------------------

####Problem 4
# concatenate(['A','B'],['a','b'],'-')
# ['A-a', 'B-b']

def concatenate(item1,item2,connector):
    return [item1 + connector + item2 for (item1,item2) in zip(item1,item2)]

print(concatenate(['A','B'],['a','b'],'-'))
#---------------------------

####Problem 5
# d_list(['a','b','c'])
# {'a': 0, 'b': 1, 'c': 2}
def list_dic(lst):
    return {item:i for i,item in enumerate(lst)}

print(list_dic(['a','b','c']))
#---------------------------

####Problem 6
# count_match_index([0,2,2,1,5,5,6,10])
# 4
def  count_match_index(lst):
    return len([item for i,item in enumerate(lst) if i == item])

print(count_match_index([0,2,2,1,5,5,6,10]))
'''