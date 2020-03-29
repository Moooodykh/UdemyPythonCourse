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

# # # # # # # # #  part 20 (Print Formatting with Strings ) # # # # # # # # #