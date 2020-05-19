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

""" # Ordered dict is a dictionary with ordered items in it
from collections import OrderedDict

d1 = {}
d1['a'] = 1
d1['c'] = 3
d1['b'] = 2
d1['e'] = 5
d1['d'] = 4

for k,v in d1.items():
    print(k,v) # here the items does not need to be ordereded in the correct way as it entered because a dictionary is like a place 
    # to hold despite the order


d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
d2['c'] = 3
d2['d'] = 4
d2['e'] = 5

for k,v in d2.items():
    print(k,v)

# you can see when you print boths of dicts , it is not the same order the items is placed inside of them.
print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print(d1==d2)
"""

# # # # # # # # # #  part 90 ( Collections Module - namedtuple) # # # # # # # # #

#Namedtuple is another way of having a class/tuple with name of attributes(not only value)

"""
from collections import namedtuple
# normal classic wat
t = (1,2,3)
print(t[0])

dog = namedtuple('Dog','name breed age')
sam = dog(name ='Sammy',breed=88, age=9)
print(sam.age,sam.breed,sam.name)
# or as normal tuples
print(sam[0],sam[1],sam[2])
"""

# # # # # # # # # #  part 91 ( Datetime ) # # # # # # # # #

"""
import datetime
##### TIME

# specifying datetime.time(hour,minute,second,microsecond)
t = datetime.time(11,22,55) # this will throw a value error if you enter a wrong time stamp(hour,min,sec...etc)
print(t)
print(t.hour)
print(t.min)
print(t.second)
print(t.isoformat())# HH:MM:SS:mmmmmmm
print(t.tzinfo)
print(t.utcoffset())
print(t.dst())
print(t.min) # calling the minimum value of time 
print(datetime.time.min)
print(datetime.time.max)# calling the maximum value of time 


print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)
##### DATE

print('*'*100)
today = datetime.date.today()
ts = datetime.date(19,5,29)
print(today)
print(today.isoweekday())
print(today.day)
print(today.month)
print(today.year)
print(today.timetuple())
print(today.replace(month=9))
print(today.ctime()) #ctime(DAY NAME , MONTH, DAY NUMBER , HOURS, YEAR ) 
                        #IS THIS FORMAT : Tue May 19 00:00:00 2020

print(ts.isoformat())# This is 'YYYY-MM-DD'.
print(today.toordinal())
print(today.fromordinal(737564))
print(today.fromordinal(7)) # manipulate this number to see the differences

print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)


import time,calendar

d = datetime.datetime.now()
print(d.ctime())
print(d.timetz())
print(d.tzinfo)
print(d.resolution)
print (time.mktime(d.timetuple()))

s = datetime.datetime.utcnow()
print(s.ctime())
print (calendar.timegm(s.timetuple()))


print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)


y = datetime.date.today()
u = datetime.date(2020,3,19)
print(y-u)
print(datetime.timedelta(5555,6))
"""
# # # # # # # # # #  part 92 ( Python Debugger - pdb) # # # # # # # # #
# # # # # # # # # #  part 93 ( Timing your code - timeit) # # # # # # # # #
# # # # # # # # # #  part 94 (  Regular Expressions -re) # # # # # # # # #
# # # # # # # # # #  part 95 ( StringIO ) # # # # # # # # #