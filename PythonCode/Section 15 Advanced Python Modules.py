# ------------------------ Section 15 : Advanced Python Modules is from part 87 to 95   -----------------------------

# # # # # # # # # #  part 87 ( Collections Module - counter) # # # # # # # # #

""" 
# The collections module is a built-in module that implements specialized container data types 
# providing alternatives to Python’s general purpose built-in containers. 
# We've already gone over the basics: dict, list, set, and tuple.
# Now we'll learn about the alternatives that the collections module provides.

### ------ Counter -------
from collections import Counter

#counter with LIST

lst = [1,23,2,3,2,2,2,2,3,4,6,1,11]

# counter will count how many time the item shows up and then return the item as key and how many times as value
print(Counter(lst))

#counter with string
name = 'aaasdcsdssxsddvsds'
print(Counter(name))

#Counter with words in a sentence
s = 'How many times does each word show up in this sentence word times each each word'

print(Counter(s.split()))

c = Counter(s.split())

print(c.most_common(3))
# give you the most common three elements

c.update({'sara':1})
# this is just adding a new element(key,value) to the existing dictionary 

c.update({'each':3})
# added each by thre extra more times 


print(c)

d = Counter(s.split())

# total of all counts
print(sum(d.values()))

# reset all counts
# d.clear()
# print(sum(d.values()))

# list unique elements
print(list(d))
# convert to a set
print(set(d))
# convert to a regular dictionary
print(dict(d))

# convert from a list of (elem, cnt) pairs
print(d.items())

# c.most_common()[:-n-1:-1]       # n least common elements
print(d.most_common(2))
print(d.most_common()[::-1])

# remove zero and negative counts
d += Counter()
print(d)
###### Common patterns when using the Counter() object ######

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts
"""

# # # # # # # # # #  part 88 ( Collections Module - defaultdict) # # # # # # # # #

""" 
# defaultdict is a dictionary which did not throw any error if we  apply a key which is not exist or has a value

from collections import defaultdict

d = {'key1':1}
print(d['key1'])
# print(d['key2']) # KeyError: 'key2'

c = defaultdict(lambda  : 0)
c['key1'] = 5
c['key2'] # this will make a default key to 0 withour throwing an error

for key,item in c.items():
    print(key)
    print(item)



e  = defaultdict(object)

e['one']

for key,item in e.items():
    print(key)
    print(item)

### examples
word = 'mississippi'

defdict = defaultdict(int) # default items are created using int(), which will return the integer object 0
defdict['k1']
for k,v in defdict.items():
    print(k,v)

ver = defaultdict(int)
for letter in word:
    ver[letter] += 1 # this will add that the letter is exist 

print(ver.items())

#
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d2 = defaultdict(list) #default items are created using list(), which returns a new empty list object.

for k,v in s:
    d2[k].append(v)
print(d2.items())

somedict = {}
# print(somedict[3]) # KeyError

someddict = defaultdict(int)
print(someddict[3]) # print int(), thus 0
"""

# # # # # # # # # #  part 89 ( Collections Module - OrderedDict) # # # # # # # # #
# # # # # # # # # #  part 90 ( Collections Module - namedtuple) # # # # # # # # #
# # # # # # # # # #  part 91 ( Datetime ) # # # # # # # # #
# # # # # # # # # #  part 92 ( Python Debugger - pdb) # # # # # # # # #
# # # # # # # # # #  part 93 ( Timing your code - timeit) # # # # # # # # #
# # # # # # # # # #  part 94 (  Regular Expressions -re) # # # # # # # # #
# # # # # # # # # #  part 95 ( StringIO ) # # # # # # # # #         