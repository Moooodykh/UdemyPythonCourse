# ------------------------ Section 13 : Python Generators is from part 83 to 85   -----------------------------

# # # # # # # # # #  part 83 ( Generators with Python) # # # # # # # # #
"""
# Generators allow us to generate as we go along, instead of holding everything in memory.

# Let's explore a little deeper. We've learned how to create functions with def and the return statement. 
# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.
#  This type of function is a generator in Python, allowing us to generate a sequence of values over time.
#  The main difference in syntax will be the use of a yield statement.

# In most aspects, a generator function will appear very similar to a normal function.
#  The main difference is when a generator function is compiled they become an object that supports an iteration protocol. 
#  That means when they are called in your code they don't actually return a value and then exit. 
#  Instead,generator functions will automatically suspend and resume their execution and state around the last point of value generation.
#   The main advantage here is that instead of having to compute an entire series of values up front, 
#   the generator computes one value and then suspends its activity awaiting the next instruction. This feature is known as state suspension

# this is the normal way that we used. we store the numbers in the list(which taking a lot of space for the whole time) and
#  then release the list object

def gen_cubes():
    result= []
    for item in range(10):
        result.append(item**3)
    return result

print(gen_cubes())

### GENERATORS: we use yield statement and each number is used once in the memory(NOT SAVING THE WHOLE LIST:- ONE BY ONE).

def gen_cubes_g():
    for item in range(10):
        yield(item ** 3 ) #we get exactly the same but with much less used memory because it is coming one element by one.
        
print(list(gen_cubes_g())) #we need to put that into list and print it



#### Generators are best for calculating large sets of results 
# (particularly in calculations that involve loops themselves) in cases where 
# we don’t want to allocate the memory for all of the results at the same time.
# Let's create another example generator which calculates fibonacci numbers:

def fibon(n):
    a = 1 
    b = 1
    for item in range(n):
        yield a
        a,b = b,a+b

print(list(fibon(10)))

def fibon_l(n):
    result = []
    a = 1
    b = 1
    for item in range(n):
        result.append(a)
        a,b = b,a+b
    return result

print(list(fibon_l(10)))
# Notice that if we call some huge value of n (like 100000) the second function 
# will have to keep track of every single result,
#  when in our case we actually only care about the previous result to generate the next one!

#------------------------------------------
# next() and iter() built-in functions
# A key to fully understanding generators is the next() function and the iter() function.

#### NEXT()
# The next() function allows us to access the next element in a sequence.

def simple_gen():
    for item in range(3):
        yield item

g = simple_gen()
print(g)
print(next(g)) #print 0
print(next(g)) #print 1
print(next(g)) #print 2
#print(next(g)) #StopIteration

# After yielding all the values next() caused a StopIteration error.
#  What this error informs us of is that all the values have been yielded.
# You might be wondering that why don’t we get this error while using a for loop?
#  A for loop automatically catches this error and stops calling next().

#### NEXT()
# Let's go ahead and check out how to use iter(). You remember that strings are iterables:

s = 'hello'
for let in s:
    print(let)

print('-'*100)
# print(next(s)) # TypeError: 'str' object is not an iterator
s_iter = iter(s) # make the object it self iterable
print(next(s_iter)) # print h
print(next(s_iter)) # print e
print(next(s_iter)) # print l
print(next(s_iter)) # print l
"""


# # # # # # # # # #  part 84 - 85(Generators Homework Overview & solutions) # # # # # # # # #
