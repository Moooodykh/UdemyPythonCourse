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












