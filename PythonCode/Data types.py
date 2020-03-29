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
my_string = "Hello world"

""" Indexing """

# print(my_string[8])  # my_string[1]: indexing is calling the string with specific character position
# We have two method to calling the indexing 
# 1. normal indexing 0 1 2...etc, i want to call the r
print(my_string[8])
# 2. reverse indexing 0 -5... -1 etc              [-1] is the last letter in that string
print(my_string[-3])

""" Slicing """
# we need to put three parts (start:stop(excluding this position):step)
mystring = "abcdefghi"
print (mystring[1:6:2]) #(start:stop(excluding this position):step)
print (mystring[:4]) # showing from start to this position
print (mystring[3:6]) # showing a specific part
print (mystring[4:7]) # showing a specific part
print (mystring[::2]) # showing the whole string with step 2
print (mystring[::-1]) # reversing the string 