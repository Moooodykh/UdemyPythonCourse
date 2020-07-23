# ------------------------ Section 6 "UPDATE" is from part 42-47,57,58   -----------------------------

# # # # # # # # # #  part 42-45 (Introduction to Functions) # # # # # # # # #
""" 
def say_hello():
    print('Hello')

print(say_hello) # printing which type of function
print(say_hello()) # calling the function

def hello(name):
    print('Hello '+name)

hello("Sam")

def add_two_numbers(num1,num2):
    return num1 + num2

result = add_two_numbers(5,10)
print(add_two_numbers(5,10))
print(result)
print(add_two_numbers('One','Two')) # adding them even if they are texts



### main difference between PRINT and RETURN which is that print has no value to save just PRINTING
# while the RETURN enable saving the varibales and use them in other places


def print_num(a,b):
    print(a + b) 
def return_num(a,b):
    return(a + b) 

print('+'*100)
x = print_num(5,20)
print(x) # this will not save the result -> giving you a value of NONE
y = return_num(5,20)
print(y)
print(type(x)) # NoneTYPE
print(type(y)) # INT




def check_even(num):
    return num % 2 == 0

print(check_even(26))


### Check if any number in a list is even
def check_even_list(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
            break
        else:
          pass

print(check_even_list([1,2,3]))


def check_even_list_complete(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False



### Return all even numbers in a list
# Let's add more complexity, we now will return all the even numbers in a list,
#  otherwise return an empty list.

def list_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
        else:
            pass
    return result

print(list_even_numbers([1,2,3,4,5,6])) #return all the even numbers in a list
print(list_even_numbers([1,3,5])) # return an empty list.


# Returning Tuples for Unpacking
fruits = [('apple',200),('orange',300),('banana',250)]

for item in fruits:
    print(f'{item}')
for fruit,price in fruits:
    print(f'{fruit} has price {price}')

"""

# # # # # # # # # #  part 46 (Tuple Unpacking with Python Functions) # # # # # # # # #

""" 
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

# Make a function which print the top employee based on max hours worked

def employee_of_the_month(employees):
    emp_name = ''
    max_hours = 0
    for name,hours in employees:
        if hours > max_hours:
            max_hours = hours
            emp_name = name
        else:
            pass
    return(emp_name,max_hours)

print(employee_of_the_month(work_hours))
"""

# # # # # # # # # #  part 47 (Interactions between Python Functions) # # # # # # # # #

""" 
# CREATE A GUESS GAME

mylist = [' ','O',' ']

def shuffle_list(listItem):
    from random import shuffle
    shuffle(listItem) # you do not need to assign it to a variable
    return listItem


# print(shuffle_list(mylist))

def player_guess():
    
    guess = 9
    while guess not in [1,2,3]:
        guess = int(input('Please enter a guess between 1 and 3 \t'))
    
    return guess

# print(player_guess())

def guess_compare(guess,mylist):
    position = 0
    for index,item in enumerate(mylist):
        if item == 'O':
            position = index + 1 # this is because I asked the used between 1 and 3 NOT 0 to 2
    
    if guess == position:
        print(f'Great Job, Your guess is right and it has position nr {guess}')
    else:
        print('Oh no , worng guess, try again')
        print(mylist)


# print(guess_compare(3,[' ','O',' ']))

#--------------------------------------
#--------------------------------------
# CONNECTING ALL FUNCTIONS AS ONE GAME:

print('Hello and welcome to our guessing game')
playing = True

while  playing:
    mylist = [' ','O',' ']
    #Shuffle the list
    Shuffled_list = shuffle_list(mylist) 
    #calling the Guess
    guess = player_guess()
    #Comparing the results
    guess_compare(guess,Shuffled_list)
    
    
    playing_again = True
    while playing_again:
        user_input = input('Do you want to play again "Yes" or "No" please! \t')
        if user_input.lower() == 'yes':
            break
        elif user_input.lower() == 'no':
            playing = False
            playing_again = False
            break
        else:
            print('please type "yes" or "no"')
            continue

print('Thanks for playing with us')
"""




# # # # # # # # # #  part 48 (EXAMPLES) # # # # # # # # #

### propblem 1 
"""
 def my_func():
    print('Hello world')
"""
### propblem 2

"""
def my_func(fname,lastname):
    print('Hello {1} {0}'.format(fname,lastname))

my_func('Ahmad','Adi')
"""

### propblem 3 
"""
def my_func(arg1):
    if arg1 == True:
        print('Hello')
    else:
        print('Good by')

my_func(True)
"""
### propblem 4 

"""
def my_func(x,y,z):
    if z == True:
        return x
    else:
        return y

print(my_func(1,1000,False))
"""
### propblem 5 

"""
def my_func(a,b):
    return int(a)+int(b)

print(my_func(1,2))
print(my_func('1','2'))
"""

### propblem 6 

"""
def is_even(num):
    return num % 2 == 0
print(is_even(25))
print(is_even(26))
"""

### propblem 7 
""" 
def is_greater(num1,num2):
    if num1 > num2:
        return True
    else:
        return False

print(is_greater(3,5))
"""

#------------------------------------------------------------
""" 
# ARGS
#ARGS is returned as TUPLE
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4,5,6,7))

def show_vars(*args):
    for item in args:
        print(item)

show_vars('a',2,3,4,'5','s')

def return_args(*args):
    return args

print(return_args(1,2,3,4,5,6,6))

### KWARGS
def choose_fruit(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print('I do not know')

choose_fruit(fruit='apple',grocer='lettucd',drink='juice')

### ARGS & KWARGS

def my_func(*args,**kwargs):
    print(args)
    print(kwargs)

    if 'fruit' and 'juice' in kwargs:
        print(f"I would like to have {args[0]} of my favorite {kwargs['fruit']}")
        print(f"May I have a {kwargs['juice']} juice please !")

        print("I would like to have {} of my favorite {}".format(args[0],kwargs['fruit']))

my_func(22,13,23,10,25,grocery='lettuce',fruit='Pineapple',juice='Orange',film='Heros')   
"""
#------------------------------------------------------------
### propblem 8 

"""
def my_func(*args):
    return sum(args)

print(my_func(9,2,5,2,3,5,3,2))
"""

### propblem 9 
""" 
def my_func(*args):
    result = []
    for item in args:
        if item % 2 == 0:
            result.append(item)
    return result

print(my_func(1,23,4,5,2,23,5,52,3,23))
"""
### propblem 10 
""" 
#first way
def skyLine(x):
    result = []
    for i in range(len(x)):
        if i % 2 == 0:
            result.append(x[i].lower())
        else:
            result.append(x[i].upper())
    return ''.join(result)

print(skyLine('abdcsdsdksjdkh'))

#Second wat
def lower_upper(text):
    elements_list = []
    result = []
    for i in text:
        elements_list.append(i)
    for index,item in enumerate(elements_list):
        if index % 2 == 0:
            result.append(item.upper())
        else:
            result.append(item.lower())
    return ''.join(result)

print(lower_upper('abdcsdsdksjdkh'))

#third way
def low_up(text):
    result = ''
    for x in range(len(text)):
        if x % 2 == 0:
            result = result+text[x].upper()
        else:
            result = result+text[x].lower()
    return result 

print(low_up('HelloSOSO'))
"""


