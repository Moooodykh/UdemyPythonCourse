# ------------------------ Section 16 : Section 16: Advanced Python Objects and Data Structures is from part 102 to 108   -----------------------------

# # # # # # # # # #  part 102 ( Advanced Numbers) # # # # # # # # #

""" 
#####    Hexadecimal
# Using the function hex() you can convert numbers into a hexadecimal format:
print(hex(12))
print(hex(200))

#####    Binary
# Using the function hex() you can convert numbers into a hexadecimal format:
print(bin(128))
print(bin(127))

#####    Exponentials
# The function pow() takes two arguments, equivalent to x^y. 
print(pow(2,4))
print(pow(4,4))

# With three arguments it is equivalent to (x^y)%z, 
print(pow(2,4,3))

#####    Absolute Value
# The function abs() returns the absolute value of a number. 
# The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.
print(abs(-3.15))
print(abs(-3))

#####    Round
# The function round() will round a number to a given precision in decimal digits (default 0 digits). It does not convert integers to floats.
print(round(3,2))
print(round(1395,-3))
print(round(395,-2))
print(round(3.14233321,2))

# Python has a built-in math library that is also useful to play around with in case you are ever in need of some mathematical operations.
#  Explore the documentation here!
#### https://docs.python.org/3/library/math.html
"""

# # # # # # # # # #  part 103 ( Advanced Strings) # # # # # # # # #

""" 
s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())

# Remember, strings are immutable. None of the above methods change the string in place, they only return modified copies of the original string.
s = s.upper()
print(s)
s= s.lower()


#####     Location and Counting
print(s.count('o')) # returns the number of occurrences, without overlap
print(s.find('o')) # returns the starting index position of the first occurence

#####     Formatting
# The center() method allows you to place your string 'centered' between a provided string with a certain length.
#  Personally, I've never actually used this in code as it seems pretty esoteric...

print(s.center(20,'z'))

# The expandtabs() method will expand tab notations \t into spaces:
print(
'hello\thi'.expandtabs()
)

#####     is check methods
s = 'hello'
### isalnum() will return True if all characters in s are alphanumeric
print(s.isalnum())
### isalpha() will return True if all characters in s are alphabetic
print(s.isalpha())
### islower() will return True if all cased characters in s are lowercase and there is at least one cased character in s, False otherwise.
print(s.islower())
# isspace() will return True if all characters in s are whitespace.
print(s.isspace())

# istitle() will return True if s is a title cased string and there is at least one character in s, i.e.
# uppercase characters may only follow uncased characters and lowercase characters only cased ones. It returns False otherwise.
print(s.istitle())

# isupper() will return True if all cased characters in s are uppercase and there is at least one cased character in s, False otherwise.
print(s.isupper())

# nother method is endswith() which is essentially the same as a boolean check on s-1
print(s.endswith('o'))

print(s.isidentifier())
print(s.isascii())

# Built-in Reg. Expressions

###### Strings have some built-in methods that can resemble regular expression operations.
###  We can use split() to split the string at a certain element and return a list of the results.
print(s.split('e')) # ['h', 'llo']
###  We can use partition() to return a tuple that includes the first occurrence of the separator sandwiched between 
# the first half and the end half.
print(s.partition('l')) # ('he', 'l', 'lo')
"""

# # # # # # # # # #  part 104 ( Advanced Sets) # # # # # # # # #
# # # # # # # # # #  part 105 ( Advanced Dictionaries) # # # # # # # # #
# # # # # # # # # #  part 106 ( Advanced Lists) # # # # # # # # #
# # # # # # # # # #  part 107 ( Advanced Python Objects Assessment Test) # # # # # # # # #
# # # # # # # # # #  part 108 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
