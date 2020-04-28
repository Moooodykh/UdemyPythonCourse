# ------------------------ Section 10 : Section 10: Errors and Exceptions Handling is from part 71 to 75   -----------------------------

# # # # # # # # # #  part 71 (Errors and Exception Handling) # # # # # # # # #



""" 
# errors can happen all the time
# if an error happens that means the running script will be stopped so that we use error/exception handling
# ------------THREE KEY WORDS--------------------
# TRY: this is a block of code which can cause an error
# EXCEPT:this is a block which will be run in case there is an error in try statment
# FINALLY: A final block of code which will be run regardless an error


#------------------------------------------------------------
#You can check out the full list of built-in exceptions here. Now let's learn how to handle errors
#  and exceptions in our own code.
#https://docs.python.org/3/library/exceptions.html
#------------------------------------------------------------
def add(n1,n2):
    return n1 + n2


number1 = 20
number2 = input('Please give us a random number')
add(number1,number2) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('Every thing is FINE')

try:
    # THIS BLOCK OF CODE THAT MAY HAS AN ERROR
    result = 10 + 10 #'10' producing an error   
except:
    print('Hej you may not adding correctly')
else:
    print('Add went successfully')
    print(result)

print('-'*100)


# try , except with many Error handls, else and finally example
try:
    f = open('testfile.txt','r')
    f.write('This is a new line')
except TypeError:
    print('you got a type error')
except OSError:
    print('you got a realted I/O error')
except IOError:
    print('you got a realted I/O error based on access data')
except:
    print('Another exception type ')

else:
    print('Every thing is Written successfully')
    f.close()
finally:
    print('I run all the time ')
# it is not important to have else statment
# the more logical way is , try statement if some errors happened run except code 
# else if there is no error run ELSE statment code 


# try , except , else and finally example
def is_int():

    while True:
        try:
            num = int(input('provide us a number'))

        except:
            print('You did not enter a number , please enter a number')
            continue
        
        else:
            print('Great that you enter a number, thank you')
            break
            
        finally:
            print("thanks for using this application")

is_int()
"""

# # # # # # # # # #  part 72 - 73 (Errors and Exceptions Homework / Solution) # # # # # # # # #

"""
### Problem 1
# Handle the exception thrown by the code Sbelow by using try and except blocks.
#for i in ['a','b','c']:
#    print(i**2)

try:
    for i in [1,'b','c']:
        print(i**2)
except:
    print('You are not entering numbers')
else:
    print(i**2)

### Problem 2
# Handle the exception thrown by the code below by using try and except blocks
# . Then use a finally block to print 'All Done.'
# x = 5
# y = 0
# z = x/y
print('*'*100)
try:
    x = 5 
    y = 0
    z = x/y
except:
    print('division by zero')
else:
    print(z)
finally:
    print('All done!!')

### Problem 3
# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.
#  def ask()
print('+'*100)

def ask():
    while True:

        try:
            num = int(input('provide a number '))
        except:
            print('please provide an integer')
            continue
        else:
            print(f'Sequre of {num} is:',num**2)
            break
    
ask()
"""
# # # # # # # # # #  part 74 (Pylint Overview) # # # # # # # # #
# we need to install pylint library
# pip install pylint
# WE need to run that to one simple example by openning cmd then Pylint thisfile.py
# check the report and try to implement and correct the errors


""" 
we put this example as start
a = 1
b = 2
print (a)
print(b)
we got -6 of 10 by running this in CMD pylint cap.py

# we developed the code to look like down and I got 10 of 10 : 
'''
This is a simple function
'''

def func():
    '''
    this is a simple function
    '''
    first = 1
    second = 2
    print(second)
    print(first)
    

 """

# # # # # # # # # #  part 75 (Running tests with the Unittest Library) # # # # # # # # #

# in this section will move to Folder Unittest which contains the function script and unit tests for this function
