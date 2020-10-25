# ------------------------ Section 20  Advanced Python Objects and Data Structures is from part 138 to 144   -----------------------------

# # # # # # # # # #  part 138 ( Advanced Numbers) # # # # # # # # #

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

# # # # # # # # # #  part 139 ( Advanced Strings) # # # # # # # # #

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
print(s.count('o')) # returns the number of occurrences, without overlap , COUNT HOW MANY 'O' in that string
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
print(s.partition('l')) # ('he', 'l', 'lo') #FRONT-SEPERATOR-END
"""

# # # # # # # # # #  part 140 ( Advanced Sets) # # # # # # # # #

"""
s = set()
s.add(1)
s.add(2)
s.add(1)#even if it is duplicated it will show ONCE
print(s)
# clear the ser
s.clear()
print(s)

#Copy of the set
q = {1,2,3}
sc =q.copy()
print(sc)
sc.add(4)

#difference method
#  between two sets
print(sc.difference(q))

#difference update 
# method is deleting the matching objects between two sets
# s1.difference_update(s2)
s1 = {1,2,3}
s2 = {1,4,6}
s1.difference_update(s2)
print(s1) # once is the common element and it is deleted from S1 but it remained in S2
print(s2)

#DISCARD
# is discarding the element itself from the set
s2.discard(4)#4 will be deleted 
s2.discard(9)#9 will not affect the set because it is not a member of the set
print(s2)

#INTERSECTION
#COMMON between all sets
s1 = {1,2,3}
s2 = {1,2,4,6}
print(s1.intersection(s2))

#INTERSECTION UPDATE
#will make the first set is equals to the intersection 
s1.intersection_update(s2)
print(s1)

dic1 = {'fruit':'orange','numbers':2}
print(dic1['fruit'])

#ISDISJOINT 
#will return TRUE and FALSE based on the sets if there is not any intersection in between
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2))#FALSE , there is intersection in between these two sets
print(s1.isdisjoint(s3))#TRUE, there is not an intersection in between these two sets

#ISSUBSET
#will check if the first SET is a SUBSET from the SECOND SET
s1 = {1,2}
s2 = {1,2,4}
print(s1.issubset(s2))

#ISSUPERSET
#reverse of ISSUBSET
print(s2.issuperset(s1))

#SYMMETRIC_DIFFERENCE
#giving the elements that not in between two sets
print(s1.symmetric_difference(s2))

#UNION
# is returning the union of two sets
print(s1.union(s2))

#UPDATE
#return union between the two set 
s1.update(s2)
print(s1) 
"""

# # # # # # # # # #  part 141 ( Advanced Dictionaries) # # # # # # # # #
""" 
dic1 = {'k1':1,'k2':2}

# DICTIONARY COMPREHENS METHOD
print({x:x**2 for x in range(10)}) #means ,key is x ,value is x^2
#key names based on values
# this is for X which realtes in the equation

#for NONE realted equation
#key names based NONE values
print({k:v**2 for k,v in zip(['a','b'],range(2))})
print(*zip(['a','b'],range(2))) 
"""

# # # # # # # # # #  part 142 ( Advanced Lists) # # # # # # # # #
"""
l=[1,2,3]

##APPEND
l.append(4)
print(l)

##COUNT
#which show you how many times that element shows up in that list
print(l.count(1))

##EXTEND
# will add each element in the list as a member to the head list
x = [1,2,3]
x.append([4,5]) #[1, 2, 3, [4, 5]]
print(x)

x = [1,2,3]
x.extend([4,5]) #[1, 2, 3, 4, 5]]
print(x)

##INDEX
#  return the index of the passed value
l = [1,2,3,4]
print(l.index(2))

### INSERT
# will insert that value for specific index
l.insert(2,'inserted')
print(l)


### POP
# will delete the last element in that list
del_element = l.pop()
del_element
print(l)
# you can delete by referring to the index
l.pop(3)
print(l)

### REMOVE
# will remove the first input value that match that value
l.remove('inserted')
print(l)  

s = [1,2,3,4,3]
s.remove(3)
print(s)   # notice that the second 3 is not deleted

### REVERSE
#will reverse the list
s = [1,2,3,4]
s.reverse()
print(s)

### SORT
#will sort incrementally
a = ['a','c','b','z','f']
b = [2,5,3,1,8]
a.sort()
b.sort()
print(a)
print(b)

"""


# # # # # # # # # #  part 143 ( Advanced Python Objects Assessment Test) # # # # # # # # #
# # # # # # # # # #  part 144 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
