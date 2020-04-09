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

print(lesser_of_evens(5,11))
 """
# ------------------------------------------------------------------------------------

### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

""" 
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
print('---------------------------------------------')