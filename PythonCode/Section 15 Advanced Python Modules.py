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
from typing import Any

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
"""
#Namedtuple is another way of having a class/tuple with name of attributes(not only value)


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

"""
# this PYTHON Debugger will help me to debug my code.
# I need to set a trace directly when I import that 
import pdb
pdb.set_trace()


x = 5
y= 'a'
result = x+y
print(result)
"""

# # # # # # # # # #  part 93 ( Timing your code - timeit) # # # # # # # # #

""" 
#Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project.
#  Python has a built-in timing module to do this.
# This module provides a simple way to time small bits of Python code. 
# It has both a Command-Line Interface as well as a callable one. 
# It avoids a number of common traps for measuring execution times.
import timeit

### range
print('-'.join(str(i) for i in range(100)))
print(
timeit.timeit('"-".join(str(i) for i in range(100))', number = 10000) # calling the timeit(which count time execution)
    )
### Listcomprehension 
print("-".join([str(x) for x in range(100)]))
print(
timeit.timeit('"-".join([str(x) for x in range(100)])',number= 10000)
)

### MAP func
"-".join(map(str,range(100)))
print(
    timeit.timeit('"-".join(map(str,range(100)))',number= 10000)
)
x = range(5)
print(*x)
"""

# # # # # # # # # #  part 94 (  Regular Expressions -re) # # # # # # # # #

# Regular expressions are very useful functions/methods that we can use. it contains a lot of functions.

#######
# SEARCH func
#######
""" import re

patterns = ['term1', 'term2']

text = 'This is a text where you find the term1 but not the other term.'

print('FUNCTION SEARCH: ')

for pattern in patterns:
    print(f'We are seraching for "{pattern}" in \n"{text}"')
    x = re.search(pattern, text)
    if x:
        print('Match found')
        print(type(x))

    else:
        print('Match NOT found')

match = re.search('hello', 'Hi guys and hello to our club')
print(match)
print(type(match))
print(match.start())
print(match.end())
print(match.span())  # showing the start and the end index as tuple
"""

#######
# SLPIT func
#######

""" 
# this function as split function before
split_mark = '@'
statment = 'Is your email : hello@gmail.com?'
print(statment.split(split_mark))

# this is exactly the same as above function
print(re.split(split_mark, statment))
"""

#######
# FINDALL func
#######

''' 
# Returns a list of all matches
result = re.findall('match', 'We will try to find matches, here is the first match, here is another match.')
print(result)
# we use it normally with len func
print(len(result))


# This function is define to check all possible syntax.
def multi_re_find(patterns,phrase):
    """
        Takes in a list of regex patterns
        Prints a list of all matches
    """
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' % (pattern)) #%r is showing the pattern as it is without cut
        print(re.findall(pattern, phrase))
        print('\n')


print ('%r'%('hi'))
print('hi')

'''
#######
# Repetition Syntax
#######

""" 
# There are five ways to express repetition in a pattern:
#
# A pattern followed by the meta-character * is repeated zero or more times.
# Replace the * with + and the pattern must appear at least once.
# Using ? means the pattern appears zero or one time.
# For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times the
# pattern should repeat.

# Use {m,n} where m is the minimum number of repetitions and n is the maximum. Leaving out n {m,} means the value
# appears at least m times, with no maximum.



test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',  # s followed by zero or more d's
                 'sd+',  # s followed by one or more d's
                 'sd?',  # s followed by zero or one d's
                 'sd{3}',  # s followed by three d's
                 'sd{2,3}',  # s followed by two to three d's
                 ]

multi_re_find(test_patterns,test_phrase)

text_statement = 'tststt.tsss...ttt..stst.tst..ststttts....stststst.tttt.sss.sts'
test_p = [
            'st*',# this will s and then zero t or more
            'st+',# this will return s and then one t or more
            'st?',# this will return s and then zero t or more
            'st{2}',#this will return s and then TWO t's
            'st{3,4}', # this will return s and then THREE or FOUR t's
            ]

# print(*test_p)
multi_re_find(test_p,text_statement)
"""

###########
# Character Sets
##########

""" 
# Character sets are used when you wish to match any one of a group of characters at a point in the input.
#  Brackets are used to construct character set inputs. For example:
#  the input ab searches for occurrences of either a or b. Let's see some examples:

test_phrase_2 = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns_2 = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns_2,test_phrase_2)


##########
# Exclusion
##########
# We can use ^ to exclude terms by incorporating it into the bracket syntax notation. 
# For example: ^... will match any single character not in the brackets.

t_phrase = 'This is a string! But it has punctuation. How can we remove it?'

print('[^!.? ]+')
print(re.findall('[^!.? ]+',t_phrase))
print('-'*100)
print('[^!.? ]')
print(re.findall('[^!.? ]',t_phrase))
print('-'*100)
print('[^!.?]')
print(re.findall('[^!.?]',t_phrase))
print('-'*100)
print('[^!.?]+')
print(re.findall('[^!.?]+',t_phrase))
"""

##########
# Character Ranges
##########
""" 
# As character sets grow larger, typing every character that should (or should not) 
# match could become very tedious. A more compact format using character ranges lets you define
#  a character set to include all of the contiguous characters between a start and stop point.
#  The format used is start-end.

# Common use cases are to search for a specific range of letters in the alphabet.
#  For instance, a-f would return matches with any occurrence of letters between a and f.
# Let's walk through some examples:

print('*'*100)
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)



##########
# Escape Codes
##########

# You can use special escape codes to find specific types of patterns in your data, 
# such as digits, non-digits, whitespace, and more. For example:

# Code	Meaning
# \d	a digit
# \D	a non-digit
# \s	whitespace (tab, space, newline, etc.)
# \S	non-whitespace
# \w	alphanumeric
# \W	non-alphanumeric
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
        # (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
        # r"\bain"
        # r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
        # (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
        # r"\Bain"
        # r"ain\B"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# Escapes are indicated by prefixing the character with a backslash \. 
# Unfortunately, a backslash must itself be escaped in normal Python strings, 
# and that results in expressions that are difficult to read. Using raw strings,
#  created by prefixing the literal value with r, eliminates this problem and maintains readability.

# Personally, I think this use of r to escape a backslash is probably one of the things 
# that block someone who is not familiar with regex in Python from being able to read regex code at first.
#  Hopefully after seeing these examples this syntax will become clear.

print('*'*100)
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric (# and white spaces)
                ]

multi_re_find(test_patterns,test_phrase)

# You should now have a solid understanding of how to use the regular expression module in Python. 
# There are a ton of more special character instances,
#  but it would be unreasonable to go through every single use case. 
# Instead take a look at the full documentation if you ever need to look up a particular pattern.
# DOCUMENTATION:
# https://docs.python.org/3/library/re.html#regular-expression-syntax
# Other link:
# http://www.tutorialspoint.com/python/python_reg_expressions.htm
"""

####################################EXAMPLES##########################################
# these examles & a lot of tutorials comes from :
# https://www.w3schools.com/python/python_regex.asp


# Character	Description	
# []	A set of characters	"[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	    Any character (except newline character)	"he..o"	
# ^	    Starts with	"^hello"	
# $	    Ends with	"world$"	
# *	    Zero or more occurrences	"aix*"	
# +	    One or more occurrences	"aix+"	
# {}    	Exactly the specified number of occurrences	"al{2}"	
# |	    Either or	"falls|stays"	
# ()    	Capture and group	 
import re

##### []	A set of characters	"[a-m]"	
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "g":
x = re.findall("[a-g]", txt)
y = re.findall('[g-t]',txt) #finding the letters between "g" and "t"
print(x,y)

##### \	    Signals a special sequence (can also be used to escape special characters)	"\d"

txt = 'there is 69 numbers in 99'
x = re.findall('\d',txt)
y = re.findall('\d+',txt)
z = re.findall(r'\S+',txt) # same as '\S'

print(x,y,z)

                # r'\d+', # sequence of digits
                # r'\D+', # sequence of non-digits
                # r'\s+', # sequence of whitespace
                # r'\S+', # sequence of non-whitespace
                # r'\w+', # alphanumeric characters
                # r'\W+', # non-alphanumeric (# and white spaces)


##### .	    Any character (except newline character)	"he..o"	

txt = 'Hello world guys'
x = re.findall('He...',txt)
y = re.findall('He...+',txt)
print(x,y)

##### ^	    Starts with	"^hello"	

txt = 'Hello this text contains hello world'
x = re.findall('^Hello',txt)
if x:
    print('Yes, the text start with HELLO')
else:
    print('the text did not start with HELLO')

##### $	    Ends with	"world$"	

txt = 'Hello this text contains hello world'
x = re.findall('world$',txt)
if x:
    print('Yes, the text ends with world')
else:
    print('the text did not end with world')

##### *	    Zero or more occurrences	"aix*"	

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", txt)
print(x)

if x:
    print("Yes, there is at least zero match or more!")
else:
    print("No match")

##### +	    One or more occurrences	"aix+"	

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix+", txt)
print(x)

if x:
    print("Yes, there is at least one match or more!")
else:
    print("No match")

##### {}    	Exactly the specified number of occurrences	"al{2}"	

txt = 'Hello all, welcome to this club today'
x = re.findall('al{2}',txt) # a followed by two l's

if x:
    print("Yes, there is match!")
    print(x)
else:
    print("No match")

##### |	    Either or	"falls|stays"	

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall('falls|stays|rain',txt)
y = re.findall('[falls]+',txt)
z = re.findall('[stays]+',txt)

if x:
    print("Yes, there is match! X ")
    print(x)
else:
    print("No match")

if y:
    print("Yes, there is match! Y")
    print(y)
else:
    print("No match")

if z:
    print("Yes, there is match! Z")
    print(z)
else:
    print("No match")

##### \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"

txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")


##### \b	Returns a match where the specified characters are at the beginning or at the end of a word
        # (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
        # r"\bain"
        # r"ain\b"	

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt) # check if any word of the statment start with "ain"
y = re.findall(r"\brai", txt) # check if any word of the statment start with "rai"

print(x)

if x:
    print("Yes, there is a word of the statment start with 'ain'! X")
    print(x)
else:
    print("No match")

if y:
    print("Yes, there is a word of the statment start with 'rai'! Y")
    print(y)
else:
    print("No match")

##### \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
        # (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
        # r"\Bain"
        # r"ain\B"

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)

print(x)

if x:
    print("Yes, 'ain' is present, but NOT at the beginning of a word ")
    print(x)
else:
    print("No match")

##### \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

txt = "The rain in Spain"

#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)

if x:
    print("Yes, string ends with 'Spain'")
else:
    print("No match")


##### [arn]  check if the string has any a, r, or n characters:

#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



##### [a-n]  Check if the string has any characters between a and n:

#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



##### [^arn]  Check if the string has other characters than a, r, or n:

txt = "The rain in spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^\D]", txt) # ^ equals  Except
y = re.findall('^The',txt) # ^ equals start with


print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print(y)
if y:
    print("Yes, there is at least one match!")
else:
    print("No match")




##### [0123]  Check if the string has any 0, 1, 2, or 3 digits:

txt = "The rain in spain"

#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
    


##### [0-9]  Check if the string has any digits:

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


##### [0-5][0-9]  Check if the string has any two-digit numbers, from 00 to 59:

txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


##### [a-zA-Z]  #Check if the string has any characters from a to z lower case, and A to Z upper case:

txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)

print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


##### [0-5][0-9]  Check if the string has any two-digit numbers, from 00 to 59:

txt = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[+]", txt)
y = re.findall('[^ ]+',txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print(y)
if y:
    print("Yes, there is at least one match!")
else:
    print("No match")


###### Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1) #1 is split from the first occurence
print(x)

###### Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # The9rain9in Spain
print(x)

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object , <_sre.SRE_Match object; span=(5, 7), match='ai'>


#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r'\bS\w+',txt)
print(x.span())


##### match/search/group
# this tutorial comes from this website
#https://regexone.com/references/python



# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string
    
    # If we want, we can use the MatchObject's start() and end() methods 
    # to retrieve where the pattern matches in the input string, and the 
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "June 24")
    
    # This will print [0, 7), since it matches at the beginning and end of the 
    # string
    print("Match at index %s, %s" % (match.start(), match.end()))
    
    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1), match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)
    
    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")


##### -------------------------------------------------------
# Lets use a regular expression to match a few date strings.
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print("Full match: %s" % (match))

# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   June
    #   August
    #   Dec
    print("Match month: %s" % (match))

# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print("Match at index: %s, %s" % (match.start(), match.end()))



#************************** doing example ******************************
regex = r"([a-zA-Z]+) (\d+)"
dates_txt = "June 24, August 9, Dec 12"
dates = dates_txt.split(',')
for word in dates:
    x = re.search(regex,word)
    print("Full match :%s" %(x.group(0)))
    print("Month match :%s" %(x.group(1)))
    print('Day match :%s'%(x.group(2)))

# # # # # # # # # #  part 95 ( StringIO ) # # # # # # # # #
