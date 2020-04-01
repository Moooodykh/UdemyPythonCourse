from decimal import Decimal

# # # # # # # # #  part  number 11 and 12   # # # # # # # # #

""" 
 x = 2 + 1
y = 21 - 3
z = 100.3 / 5.2
umber = 0.1 + 0.2
# mod
q = 7 % 4

# power
w = 5 ** 3

print(Decimal(2.765))
# notice the power of different operators
e = 2 + 10 * 10 + 2
r = (10+2) * (10+3)
p = 0.1+0.2-0.3

print(umber)
# this is a link to floating number description
#  https://docs.python.org/2/tutorial/floatingpoint.html
#  https://docs.python.org/2/contents.html

 """

# # # # # # # # #  part  number 13 and 14   (Variable Assignments and Introduction to Strings ) # # # # # # # # #

""" 
a = 5
b = "sami"
c = 10.3
type(a)
a = a + a
# print(type(c))
word = "Hello"
w = 'world'
stat = "'this is a string'"
mixed = "I'm going on a run " # show' signal
test = "hello \nwolrd" # adding escape sequnce
test1 = "hello \twolrd" # adding escape sequnce
print(test1)
print(len(mixed))  # LEN function is to count how many characters in a string

 """

# # # # # # # # #  part 15 (Indexing and Slicing with Strings ) # # # # # # # # #

""" 
my_string = "Hello world"

 ###Indexing 

# print(my_string[8])  # my_string[1]: indexing is calling the string with specific character position
# We have two method to calling the indexing 
# 1. normal indexing 0 1 2...etc, i want to call the r
print(my_string[8])
# 2. reverse indexing 0 -5... -1 etc              [-1] is the last letter in that string
print(my_string[-3])

 ###Slicing 
# we need to put three parts (start:stop(excluding this position):step)
mystring = "abcdefghi"
print (mystring[1:6:2]) #(start:stop(excluding this position):step)
print (mystring[:4]) # showing from start to this position
print (mystring[3:6]) # showing a specific part
print (mystring[4:7]) # showing a specific part
print (mystring[::2]) # showing the whole string with step 2
print (mystring[::-1]) # reversing the string 

 """
 
# # # # # # # # #  part 16-17 (String Properties and Methods ) # # # # # # # # #

"""  
# string are immutable type(can not be change later on )
# name = "sam" and it giving an error if you make name[0]='P'

x = "Hello World"
y= ' it is beautiful outside'
z = x + y
q = x * 10
w = '2'+ '3' # result here will be a string , not an intenger
#### when you call a function do not ever forget to add () ####
x.upper()
x.lower()
x.capitalize()
x.split() # split the string based on spaces and return that as a LIST
t ='Hi this is a string'
t.split('i') # this will split the string based on 'i' not a white spaces
print(t.split('i'))

"""

# # # # # # # # #  part 18-19 (Print Formatting with Strings ) # # # # # # # # #

######1  .format method
"""  
### a. STRING

x = 'This is a string {}'
y = x.format('INSERTED')
r = 'the {} {} {}'
r1 = 'the {2} {1} {0}' # you can manipulate which word you want to put based on the order of the word
r2 = 'the {0} {0} {0}'
o = r1.format('fox','brown','quick')

# this is another way to manipulate the data by assigning them to variables
t = 'the {q} {b} {f}'
t1 = 'the {f} {f} {f}'
p = t1.format(b='brown',q='quick',f='fox')
print(p)

### b. FLOAT
# FLOAT formatting value follows "{value:width.precision f}"
# width is how many digits that the number reserve when it shows upp in the result, try 1 and 10 to see the differnces
# 3f that means we need to take the number with three digits after. and the fourth one rounded

result = 100 / 777
maniR =" the result is {r}".format(r=result) # showing the result without any styling
manR =" the result is {r:1.7f}".format(r = result) #{value:width.precision f}
man0 =" the result is {0:1.5f}".format(result) #{value:width.precision f} 0 is intrepreted to result
print(man0)
""" 

######2 f-strings(formatted string literals)
"""
name = 'Josef&"#'
age = 35
salary = 123.5678223
print(f'Hi {name} which is {age} years old and salary {salary:1.4f}\n')
print(f'Hi {name!r} which is {age} years old and salary {salary:1.4f}\n') # adding !r which shows the whole string as it is
# this is the  Hi 'Josef&"#' which is 35 years old and salary 123.5678

# {value:10.4f}, with f-strings this can become {value:{10}.{6}}
num = 23.123456789
print(f"\nMy 10 character, four decimal number is:{num:{1}.{5}}\n") # 5 is representing the total number of digits
# OR 
print(f"\nMy 10 character, four decimal number is:{num:1.3f}\n")
######3 old method


statment = 'First %s second %1.5f third %d '%('Sam',23.555235523,11.33)
print(statment)

 """

###### examples : Alignment, padding and precision with .format() 
### HERE IS AN AWESOME SOURCE FOR PRINT FORMATTING: https://pyformat.info/ 

# the source of this is coming from 
# notebooks : Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\ # 03-Print Formatting with Strings
# By default, .format() aligns text to the left, numbers to the right. 
# You can pass an optional <,^, or > to set a left, center or right alignment


""" 
print('{0:8}|{1:10}'.format('Fruits','Qunatity')) 
print('{0:8}|{1:10}'.format('Orange','10'))  # aligned to the left by default
print('{0:8}|{1:<10}'.format('Orange','10'))  # aligned to the left
print('{0:8}|{1:>10}'.format('Orange','10'))  # aligned to the right
print('{0:8}|{1:^10}'.format('Orange','10'))  # aligned to the center
# Alignment with Autofill
print('{0:8}|{1:10}'.format('Jobs','Applied'))
print('{0:+<8}|{1:>10}'.format('100','2536')) # autofill the left side of 100 with ++++++
print('{0:8}|{1:*>10}'.format('100','2536')) # autofill the left side of 2536 with *****
print('{0:-^8}|{1:+^10}'.format('100','2536')) # autofill the left and right side of 100  by ------ and 2536 with +++++

 """

# # # # # # # # #  part 20-21 ( Lists in Python ) # # # # # # # # #

""" 
mylist = [1,2,3]
mixedList=['sring',100,23.3]
lenght = len(mixedList) # lenth of the list
sliced = ['one','two','three']
sliced[0]
sliced[1:]
another_list = [4,5]
together = mylist + another_list
together[0] = 'ONE all caps' # CHANGING THE FIRST ELEMENT
together.append('six') # add an element to the end of the list
together.insert(3,'mark') #insert an element before index
st = together.pop(3) # reomve and return the element at index 
together.remove('six') # remove the value from the list
stringList =[1,5,6,33,3]
stringList.sort() # sort the list , NO VALUES WILL BE SAVED, IT IS OPERATION THAT IS DONE TO THE LIST
X = stringList.sort() # THIS IS WRONG (X WILL BE NONE OBJECT)
# None  is a OBJECT THAT CONTAINS NOTHING

stringList.pop()# without adding any index , this will delete the last object

new_list = ['a','x','c','b','e']
Num_list= [1,33,4,2,555]
new_list.sort() # no need to save any thing the result will stay to the list object

# you can use this if you want to save the sorted list
new_list.sort()
New_sortedList = new_list

# REVERSE LIST
Num_list.reverse()
print(Num_list)
# print(st) 

"""

# # # # # # # # #  part 22-23 ( Dictionaries in Python ) # # # # # # # # #

"""
# the dictionary is calling the key and you get the vaule despite in which ordere is located (unordered and can not be sorted)
#KEYS should be strings
#{'Key1':'value1','Key2':'value2',....etc}

my_dict ={'key1':'value1','key2':'value2'} # Dic
my_dict['key1'] # calling the dictionary
print(my_dict['key1'])
Prices_dict = {'Apple':2.85,'Orange':5.99,'Milk':3.67} # MAIN exampleis to have a paired things LIKE SUPERMARKET
print(Prices_dict['Apple'])
# the dictionary is so flex, it can contain LIST, dictionary,strigs,floats ....etc
d= {'k1':123.44,'k2':[1,2,3],'k3':{'age':35}}
d['k3']

d['k3']['age'] # this call is to grap the content of the second dictionary
d['k2'][1] # this call is to grap the content of the second object in the list
print(d['k2'][1])


print('---------------------')
dic={'key1':['a','b','c']}
print(dic['key1'][2].upper()) # this call wil bring  c value and then make it UPPER CASE
new_dec ={'k1':100,'k2':200}
# if I want to add an elemnt to this dictionary
new_dec['k3']= 300
# modify existing value
new_dec['k1']= 'NEW VALUE'
new_dec ={'k1':100,'k2':200,'k3':300}
new_dec.keys() # Shows all dictionary keys
new_dec.values() # Shows all dictionary values
new_dec.items() # Shows all pairing(keys and values)
print(new_dec.values())
"""

# # # # # # # # #  part 24( Tuples in Python ) # # # # # # # # #

"""
# List content can be changed based on the index
# Tuples are very useful when u pass and object and need to be supervised that will 
# not be changed through the program

mylist = [1,2,3]
mylist[0] = 'Ali'
# print(mylist)

# Tuples content CAN NOT be changed based on the index (Tuples are immutable)
T = (1,2,3)
mylist = [1,2,3,1,1]
mylist.count(1) # counts how many time the object counted
mylist.index(3)# showing the first time the value appears in a list
type(mylist)
type(T)
len(T)
t = (1,'two',3)
t[0] # calling the elements from Tuples
t[-1] # calling the last element from Tuples
# print(t[0])
# print(f'length of Tuples {len(T)}')
tou =('a','a','b')
tou.count('a') # counts how many 'a' is repeated
tou.index('b') # showing the first time the value appears in a Tuple
print(mylist.index(3))
# tou[0] = 'f' # TUPLES ARE IMMUTABLE AND does not support item assignment
""" 
# # # # # # # # # #  part 25 ( Sets in Python ) # # # # # # # # #

""" 
#SETS are unordered collections of unique elements
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(1) # this will not be excuted because it is already added
mlist = [1,23,4,1,3,4,2,3,2,2,3,4,5,6,7,7]
# If I want to get the unique values from that list I will cast it to a SET
newSet = set(mlist) # casting a list
print(newSet)
"""

# # # # # # # # # #  part 26 ( Booleans in Python ) # # # # # # # # #

""" 
True
False #Need to be written in Capital letter
type(True)
print(type(True))
b = None  # We use None as a place holder to this object that it will be used later on 
# c NameError: name 'c' is not defined
 """

 # # # # # # # # # #  part 27-28 (  I/O with Basic Files in Python ) # # # # # # # # #

"""  
 # We creat a text file to deal with
 # we will work to deal with this file

# myfileerror = open('whoops.txt', mode='r') # this will show an error "No such file or directory: 'whoops.txt'"

with open('my_new_file.txt',mode='w') as f:
    f.write('One is First')
# this will open a file and then write(rewrite existing) new file

Readfile = open('my_new_file.txt')
text = Readfile.read()
text = Readfile.read() # this will read the last cursor point and when I read before it was at the end of the file, 
#this will read the end of file cursor which is empty string and for that I need to reset the counter by using 
Readfile.seek(0) # this will reset the cursor
text = Readfile.read()
textLine = Readfile.readlines()
print(text)
print('--------------------------------')
otherlocation = open('E:\PROGRAMMING\PythonTutorials\myfile.txt')
textfile = open('myfile.txt')
lines = textfile.readlines() # this will return each line as a part(elemnt) of the list
otherlines = otherlocation.read()
otherlocation.seek(0)
Listotherlines = otherlocation.readlines()
print(Listotherlines)
textfile.close() # this is important to release the file and not having error that the file is still open somewhere
otherlocation.close()
Readfile.close()
print('--------------------------------')
# to avoid open and forget to close we use the next statment WITH, which means open and then close 

#READING FILE
with open('myfile.txt') as readingfile: #what ever you name it 
    content = readingfile.read()
print(content)

#Shift + tab at the start of Open , will show u the 

# Passing 'r' lets us read only the existing file
# Passing 'w' lets us  write only to the file(if there is already it will override it or Create new)
# Passing 'w+' lets us read and write to the file (if there is already it will override it or Create new)
# Passing 'r+' lets us read and write 
# Passing 'a' lets us  write to the file by appending to the end of the text file

print('********************************************')
# WRITING ONLY 'w'
with open('newfile.txt',mode='w') as f:
    f.write('This is a new file\n see you there.')
    #this will generate error if we write f.read()

#READING ONLY 'r'
with open('newfile.txt',mode='r') as re:
    print(re.read())
    #this will generate error if we write f.write('here is the extra')

# APPENDING 'a'
with open('myfile.txt',mode='a') as appendedfile:
    appendedfile.write('\nTHIS WILL BE ADDED TO THE END OF THE FILE')

# WRITING AND READING 'r+'
with open('my_new_file.txt',mode='r+') as readwritefile:
    readwritefile.write('two is SECOND\n three is THIRD') # this statement will delete the previous written text, 
    #starting from the start of the file and then adding two is second.... if the size is bigger than the old size will override that
    print(readwritefile.read())
    readwritefile.write('\nhello poopy')


# WRITING AND READING 'w+' lets us read and write to the file (if there is already it will override it or CREATE NEW
with open('lastfile.txt',mode='w+') as re_write: # the file is not exist
    re_write.write('Welcome to Sweden.')

with open('my_new_file.txt',mode='r+') as m:
    m.write('\nhere we go')

"""
 # # # # # # # # # #  part 29-30 (  I/O Assessment Test & Python Objects and Data Structures Solutions ) # # # # # # # # #
 # Check the Jupyter note for the questions and answers