# ------------------------ Section 6 "Methods and Functions" is from part 40 to 53   -----------------------------

# # # # # # # # # #  part 40 (Methods and the Python Documentation) # # # # # # # # #

"""
MyList = [1,2,3]
MyList.append(3)
help(MyList.insert)
#this will show what is the method doing.
#Very good link to understand different method is 
#1. https://docs.python.org/3/library/
#2. Stack overflow
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

"""
# # # # # # # # # #  part 41-42 (Functions in Python) # # # # # # # # #

"""
# function is creating a clean repeatable code which will be used in different places

# def name_of_function(ONLY LOWER CASE)("variable"):
 #   '''
 #    Docstring explains function
 #  '''
#    print("Hello" + name)

#name_of_function("Jose")
#Hello Jose

# IN FUNCTION WE RETURN VALUES NOT PRINTING THEM

def add_function(num1,num2):
    return num1 + num2

result = add_function(1,2)
print(result)

def name_function():
    '''
    DOCSTRING: INFORMATION ABOUT THE FUNCTION
    INPUT: no input
    OUTPUT: hello..
    '''
    print('Hello')
help(name_function) # this will show no thing because there is no information stored about this function


# CALLING
name_function()

def say_hello(name = 'NAME'): # ='NAME' means that has a default value if I forget to add while I am calling the function from somepoint 
    #which means if I called the function say_hello() without the argument it will be a compile error
    print(f"Hello {name}")

say_hello('Waleed')
say_hello() # calling the default value 'NAME' to avoid compilation error

def hello_say(name = 'NAME'):
    return 'Hello ' + name

result = hello_say('Jose')
print(result)

def add(nu1,nu2):
    return nu1 + nu2

answer = add(20,30)
print(answer)

#way1
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
#way 2 
# more advanced 
def check_dog(mystr):
    return 'dog' in mystr.lower()
# becase of the down statement
print('dog' in 'My Dog is running'.lower())




# PIG LATIN FUNCTION: if the word start with Vowel we add ay to the end : apple -> appleay
#  if it start with consonant we  take the consonant to the end and then add ay : word ->ordway

def pig_latin(word):
    '''
     A native method to convert the text word to pig latin language
    '''
    first_letter = word[0]
    # check the vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter.lower() + 'ay'
    
    return pig_word

print(pig_latin('orange'))


# WE NEED TO IMPLEMNT
def is_prime(num):
    ''' 
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')

is_prime(21)

import math
print(math.sqrt(25))

# another way of developing prime
import math

def is_prime2(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

"""

# # # # # # # # # #  part 43 (*args and **kwargs in Python) # # # # # # # # #

"""  
# args = arguments , kwargs = key word arguemts

### *ARGS
def myfunc(a,b):
    #return 5% of the sum of a and b
    return sum([a,b]) * 0.05

print(myfunc (60,40))
# If I want to add more arguments like c,d,e...etc I need to modify the code and add them as c=0,d=0 and override them
# when I need , but this is not so functional , *ARGS is used to be representative of many attributes and it will be as TUPLE

def my_new_func(*args): # important thing is * not args because you can change it and use another word
    #print(args)
    return(sum(args) * 0.05)

my_new_func(40,10,50,100,100)

### **KWARGS
# kwargs will return a dictionary to unlimited number of keys and values
def nfun(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of chioce is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

nfun(fruit='apple',veggie = 'lettuce')

# the function later will look like
def nfun(**kwargs):
    if 'fruit' in kwargs:
       return 'My fruit of chioce is {}'.format(kwargs['fruit'])
    else:
        return 'I did not find any fruit here'

nfun(fruit='apple',veggie = 'lettuce') # calling will be with this style

print('------------------------------')

### *ARGS & **KWARGS 

def com_func(*args,**kwargs):
    print(f'args:{args}')
    print(f'kwargs: {kwargs}')
    
    print('I would like to have to have {} {}'.format(args[0],kwargs['food']))

com_func(10,3,4,fruit='orange',food='eggs',drink='Tea')
# when we call the function we should follow that ARGS first and the KWARGS sencond (1,2,3,fruit ='apple',5) is not acceptable
# com_func(10,3,4,fruit='orange',food='eggs',drink='Tea',10,100) is not acceptable

"""


################### EXCERSISES 

""" 
#FUNCTION 10 : PICK EVEN
# define a function that take an arbitrary number of arguments and return a list containing only those arguments that are even.

#way nr 1
def pick_even(*args):
    even_list = []
    for item in args:
        if item % 2 == 0:
            even_list.append(item) 
    return even_list

# way nr 2
def p_even(*args):
    evenList = [x for x in args if x%2 == 0]
    return evenList
    
print(pick_even(1,3,5,2,3,5,6,7,8,9,2,2,3)) 
print(p_even(1,3,5,2,3,5,6,7,8,9,2,2,3)) 

#FUNCTION 10 : skyline
# define a function that takes in a string and return a matching string where every even letter is uppercase and 
#  every odd letter is lower case, assume that the string contain only letters.
print('------------------------------')


def skyline(inputString):
    letters = [x for x in inputString]
    # print(letters)
    resultList =[]
    for index, value in  enumerate(letters):

        if index %2 == 0:
            resultList.insert(index,value.upper())
        else:
            resultList.insert(index,value.lower())
    
    print (resultList)

skyline('hello')


# another exapmle

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f" {' '.join(args)} ")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam','tomate',fruit='cherries',juice='orange')


def hungry(*args,**kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like to have {' and '.join(args)}, my favorite fruit is {kwargs['fruit']}")
        print(f"May I have a {kwargs['juice']} juice, please!")

hungry('eggs','tomate',fruit='pineapple',juice='orange')

"""
### 03-Function Practice Exercises
#03-Methods and Functions / 03-Function Practice Exercises.ipynb
#http://localhost:8888/notebooks/Desktop/PythonTutorials/Complete-Python-3-Bootcamp/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

###  LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
# if both numbers are even, but returns the greater if one or both numbers are odd

""" 
def lesser_of_evens(arg1,arg2):
    if arg1 %2 == 0 and  arg2 %2 == 0:
        if arg1 > arg2:
            return arg2 #return lesser
        else:
            return arg1
    else:
        if arg1 > arg2 :
            return arg1 #return greater
        else: 
            return arg2

# Teacher_solution 
# def lesser_of_two_evens(a,b):
    # if a%2 == 0 and b%2 == 0:
        # return min(a,b)
    # else:
        # return max(a,b)

print(lesser_of_evens(5,11))
 """
# ------------------------------------------------------------------------------------

### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

''' 
# teacher solution
def animal_crackers(text):
    wordlist = text.split()
    print(wordlist[0][0]) # first word # first letter
    print(wordlist[1][0]) # second word # first letter
    # return wordlist[0][0] == wordlist[1][0]
 
 '''
""" 
animal_crackers('Levelheaded Llama')

def animal_cracker(text):
    itemList = text.split()
    resultList = []
    for item in itemList:
        resultList.append(item[0].lower())
    print(itemList)
    print(resultList)
    if str(resultList[0]) ==  str(resultList[1]):
        return True
    else:
        return False

print(animal_cracker('Crazy Kangaroo'))
"""
# ------------------------------------------------------------------------------------

### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

''' 
#teacher solution
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

'''

""" 
def makes_twenty(num1, num2):
    if num1 == 20 or num2 == 20:
        return True
    else:
        if num1 + num2 == 20 :
            return True
        else:
            return False

print(makes_twenty(10,20))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
"""

 # ------------------------------------------------------------------------------------

### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

''' 
#Teacher solution
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
'''
""" 
#way nr 1
def old_macdonald(text):
    counter = 0
    result_string = ''
    for letter in text:
        if counter == 0 or counter == 3: 
            counter +=1
            result_string += letter.upper()
        else:
            counter +=1
            result_string += letter
    return result_string  

print(old_macdonald('macdonalds'))

# way nr 2 
def mcdonaldes(text):
    resultstring = ''
    letters = [x for x in text]
    LetterList = enumerate(letters)
    for index,value in LetterList:
        if index == 0 or index == 3:
            resultstring += value.upper()
        else:
            resultstring += value
    return(resultstring)

print(mcdonaldes('macdonalds'))
 """

# ------------------------------------------------------------------------------------

### MASTER YODA: Given a sentence, return a sentence with the words reversed

""" 
# way nr 1
def master_yoda(text):
    splitted_list = text.split()
    reversedList = splitted_list[::-1]
    return ' '.join(reversedList)

print(master_yoda('I am home'))

#way nr 2
def master_yoda2(text):
    output_text =''
    splitted_text = text.split()
    reversed_text = splitted_text[::-1]
    outresult = ' '.join(reversed_text)
    return outresult

print(master_yoda2('We are ready'))
"""

# ------------------------------------------------------------------------------------

### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

''' 
#TEACHER SOLUTION
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

'''
""" 
def almost_there(num):
    if   20 >= num >= 0 or 110 >= num >= 90 or 1110 >= num >= 990:
        return True
    else:
        return False

print(almost_there(209))
 """

# ------------------------------------------------------------------------------------

### FIND 33:

''' 
#TEACHER SOLUTION
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False
'''
""" 
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def find33(listItem):
    out_text = ''
    for element in listItem:
        out_text += str(element)
   
    if '33' in out_text:
        return True
    else:
        return False

print(find33([3,1,3]))
"""

# ------------------------------------------------------------------------------------
 
### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

""" 
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    output_text=''
    for letter in text:
        output_text = output_text + 3*letter
    
    return output_text

print(paper_doll('Mississippi'))
 """
# ------------------------------------------------------------------------------------

### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 

""" 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(arg1,arg2,arg3):
    sumofints = arg1 + arg2 + arg3
    if sumofints <= 21:
        return sumofints
    elif sumofints > 21 and (arg1 == 11 or arg2 == 11 or arg3 == 11):
        newsum = sumofints - 10 
        if newsum < 21 :
            return newsum
    elif sumofints > 21:
        return 'BUST'
        
print(blackjack(5,6,7))
"""
# ------------------------------------------------------------------------------------

''' 
### SUMMER OF '69: Return the sum of the numbers in the array,

#  except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
#  Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5,6,7,8,9,11])) 
'''

# ------------------------------------------------------------------------------------

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


''' 
#TEACHER SOLUTION
def spy_game(nums):
    
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
'''
''' 
 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    empty_string=''
    for item in nums:
        if item == 0 or item == 7:
            empty_string += str(item)
    if '007' in empty_string:
        return True
    else:
        return False  
        

print(spy_game([1,0,2,4,0,5,7]))
 '''

# ------------------------------------------------------------------------------------

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up

''' 
# this is not full solution 

# to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primess(number):
    list_of_primes=[]
    for item in range(2,number):
        if number % item != 0:
            list_of_primes.append(item)
    
    print(list_of_primes)
    return len(list_of_primes)


print(count_primess(100))
'''

# ------------------------------------------------------------------------------------

# COUNT PRIMES: Write a function that returns the number of prime numbers that 
''' 
# exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))

'''

''' 
 # WE NEED TO IMPLEMNT
def is_prime(num):
    """
    Naive method of checking for primes. 
    """
    for n in range(2,num):
        if num % n == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')

is_prime(21)


# another way of developing prime
import math

def is_prime2(num):
    """ 
    Better method of checking for primes. 
    """
    listofprimes=[]
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        else:
            listofprimes.append(num)
    return listofprimes

print(is_prime2(21))
'''
# ------------------------------------------------------------------------------------

#BONUS: Here's a faster version that makes use of
#  the prime numbers we're collecting as we go!
''' 
#TEACHER SOLUTION
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
 '''

# ------------------------------------------------------------------------------------

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
''' 
TEACHER SOLUTION
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')
 '''

"""
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to
#  specific 5-line combinations of patterns. 
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):

    letter_dict = {'a':'  *  \n * * \n*****\n*   *\n*   *\n','b':'**** \n*   *\n* *  \n*   *\n**** \n',
    'c':'   **\n *   \n*    \n*    \n   **\n','d':'**   \n*  * \n*   *\n*  * \n**   \n',
    'e':'*****\n*    \n***  \n*    \n*****\n','f':'*****\n*    \n***  \n*    \n*    \n'}
    # print(letter_dict['b'])
    if (letter == 'a'):
        return letter_dict['a']
    elif (letter == 'b'):
        return letter_dict['b']
    elif (letter == 'c'):
        return letter_dict['c']
    elif (letter == 'd'):
        return letter_dict['d']
    elif (letter == 'e'):
        return letter_dict['e']
    else:
        return letter_dict['f']
''' 
*****
*  
*** 
* 
**** 
 '''
print(print_big('e'))
"""

print('********************************************************')

# ------------------------------------------------------------------------------------


# # # # # # # # # #  part 49 ( Lambda Expressions, Map, and Filter Functions in Python) # # # # # # # # #

### MAP FUNCTION

"""
# map function is defined to applt aruguments to a specific function.
# MAP IS CALLING THE FUNCTION WITHOUT () BECAUSE IT IS LATER ON CALL AND EXCUTE THE FUNCTION
def sequre(number):
    return number ** 2

Numbers_list = [1,2,3,4,5]

# MAP WIll apply to each memeber of the NUMBER_LIST to be ran into square function
result = list(map(sequre,Numbers_list))
print(result)
# OR

for item in map(sequre,Numbers_list):
    print(item)

def splicer(string):
    if len(string) %2 == 0:
        return 'EVEN'
    else:
        return string[0]

Name_list= ['Andy','Sam','Vally']

result2 = list(map(splicer,Name_list))
#map object at 0x000001BE4E077F08             WE NEED TO CALL LIST CASTING TO PUT THE RESULT AS LIST
# MAP IS CALLING THE FUNCTION WITHOUT () BECAUSE IT IS LATER ON CALL AND EXCUTE THE FUNCTION
print(result2)
"""



### FILTER FUNCTION

"""  
# FILTER function is APPLING THE ARGUMENTS TO SOME FUNCTION HAS A TRUE OR FALSE (RETURN VALUES)

def is_even(num):
    return num%2 == 0

num_list= [1,2,3,4,5,6]
# this will apply the list to that function and return the values who apply TRUE returning value. 
res =  list(filter(is_even,num_list))
print(res)
# or
for item in filter(is_even,num_list):
    print(item)
"""

### LAMBDA EXPRESSION
""" 
#LAMBDA is a anonymous typ of converting functions which will be used once to this STYLE to have less space in the code.

# converting square function         def sequre(number):
                                     #return number ** 2
lambda num : num **2 # this is exactly the same of sequare
# we use LAMBDA with MAP and filter function
num_list= [1,2,3,4,5,6]

print(list(map(lambda num: num**2 ,num_list))) #MAP
print(list(filter(lambda num: num%2 == 0 ,num_list)))# FILTER

Name_list= ['Andy','Sam','Vally']
print(list(map(lambda name: name[0] ,Name_list))) #MAP
print(list(map(lambda name: name[::-1] ,Name_list))) #MAP

"""

# # # # # # # # # #  part 50 ( Nested Statements and Scope in Python) # # # # # # # # #
"""
x = 25
def printer():
    x=50
    return x

print(x) # x value will be 25
print(printer()) # x value will be 50

### LOCAL
lambda num : num ** 2 # num is local

### ENCLOSING FUNCTION LOCCAL

# Global variable
name = 'THIS IS A GLOBAL STRING' #Global variable
def greet():
    # enclosing function variable
    name= 'Sammy' 
    
    def hello():
        #Local variable
        name = 'I am local'
        print('Hello ' + name)
    
    hello()

greet()
# 1. try to find it locally no result , move to  enclosing function variable which is = 'Sammy'
#2. if I comment #name= 'Sammy' it will jump up to level 3 which is global varable
# 3. GLOBAL 
# 4. defined word like len ..... help(len)


### GLOBAL VARIABLE

#GLOBAL VARIABLE
x = 50

def func(x):
    print(f'X is {x}')

    # LOCAL ASSIGNMENT
    x = 'NEW VALUE'
    print(f"I just changed x TO {x}")

print(x)
func(x)
print(x) # NOTICE THIS WILL NO AFFECT THE GLOBAL VARIABLE
### ----- We need to add a global keyword to the function and 
# delete x from calling inside of the function.

print('---------------------------------------------')

y = 50
def funct():
    global y # that means bring it from global declaration and update it throw the code
    print(f'Y is {y}')

    # LOCAL ASSIGNMENT
    y = 'NEW VALUE' # local assignment will affect the global variable
    print(f"I just changed y TO {y}")

print(y)
funct()
print(y) # this will show that


# YOU NEED TO AVOID TO USE A GLOBAL VARIABLE AND OVERRIDE IT 
# BECAUSE IT WILL MAKE A HARDED TO DEUG.

# YOU CAN DEFINE GLOBAL IN OTHER WAY
z = 50
def funct(z):
    
    print(f'Z is {z}')

    # LOCAL ASSIGNMENT
    z = 'NEW VALUE' # local assignment will affect the global variable
    print(f"I just changed z TO {z}")
    return z

print(z)
z = funct(z)# HERE MAKING THE GLOBAL variable overridding 

print(z) # this will show that

"""

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------


# # # # # # # # # #  part 51 (Functions and Methods - Homework Assignment) # # # # # # # # #
# # # # # # # # # #  part 52 ( Hints and Tips for Functions and Methods Assignment) # # # # # # # # #

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------


### 1. Write a function that computes the volume of a sphere given its radius.

""" 
#The volume of a sphere is given as $$\frac{4}{3} πr^3$$
import math

def vol(rad):
    return (4/3) * math.pi * rad**3
    # return (4/3) * 3.14 * rad**3 

res = vol(2)
print(f'{res:1.3f}')
"""
# ------------------------------------------------------------------------------------
### 2. Write a function that checks whether a number is in a given range (inclusive of high and low)

'''
TEACHER SOLUTION
if num in range(low,high+1):
'''
""" 
# way 1 : return that the number is in the range
def ran_check(num,mini,maxi):
    if num > mini and num < maxi :
        return 'Number {n} is in range between {mi} and {ma}'.format(n=num, mi =mini,ma= maxi)
    else:
        return 'Number {n} is out of range between {mi} and {ma}'.format(n=num, mi =mini,ma= maxi)

print(ran_check(1,3,9))

# way 2 : boolean function
def ran_bol_Check(num,minimum,maximum):
    return num > minimum and num < maximum

print(ran_bol_Check(5,3,9))
 """
# ------------------------------------------------------------------------------------
### 3. Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
'''
TEACHER SOLUTION:
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
'''
""" 
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!

import collections
import string 
def upper_lower(text):
    lower_counter = 0
    upper_counter = 0
    alphabet = string.ascii_lowercase
    for letter in text:
        if letter.lower()in alphabet:
            if letter.isupper():
                upper_counter += 1
            else:
                lower_counter += 1
    
    orginal_text = 'Orginal text: ' + text + '\n'
    upper_text = 'No. of Upper case characters: ' + str(upper_counter) + '\n'
    lower_text = 'No. of Upper case characters: ' + str(lower_counter) + '\n'
    return orginal_text + upper_text + lower_text

    # print(f"Orginal text: {text}\nNo. of Upper case characters : {upper_counter}\nNo. of Upper case characters : {lower_counter}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(upper_lower(s)) 

"""


# ------------------------------------------------------------------------------------
### 4.Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''
TEACHER SOLUTION
 x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
'''
""" 
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(input):
  
     return (list(set(input)))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])    

"""
 # ------------------------------------------------------------------------------------
### 5.Write a Python function to multiply all the numbers in a list.

""" 
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply_list(numList):
    result = 1
    for item in numList:
        result *= item 
    
    return result

print(multiply_list([1, 2, 3, -4]))

 """

# ------------------------------------------------------------------------------------
### 6.Write a Python function that checks whether a passed in string is palindrome or not.

""" 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(text):
    s = text.replace(' ','') # replace a special character(old) in text with another(new):::: White spaces to none white space
    print(s) 
    return s == s[::-1]

print(palindrome('nurses run'))

 """
# ------------------------------------------------------------------------------------
### 6.Write a Python function that checks whether a passed in string is palindrome or not.
'''
TEACHER SOLUTION
def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  
'''

""" 

# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module
#string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'


# WAY nr 1
import string
def pangram(text):
    alphabet = list(string.ascii_lowercase)
    
    for letter in text:
        if letter in alphabet:
            alphabet.remove(letter)
    return len(alphabet) == 0
 #    change the output(return value not Bool or write more explaning) 
print(pangram("The quick brown fox jumps over the lazy dog"))


# WAY nr 2
def ispangram(str1, alphabet=string.ascii_lowercase):
# exactly the same but change the output(return value to Bool)   
"""

# ------------------------------------------------------------------------------------
### 6.Write a Python function that checks whether a passed in string is palindrome or not.

print('---------------------------------------------')
