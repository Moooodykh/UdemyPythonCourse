# ------------------------ Section 10 "UPDATE" is from part 83   -----------------------------

# # # # # # # # # #  part 80-82 (Error handlings) # # # # # # # # #
"""
#TRY: check if there is an error    
#EXCEPT : if there is , run this block of code
#ELSE: If there is not , run this block of code
#FINALLY: run this block of code if there is or isnot an error


def add(n1,n2):
    return n1+n2

x = input('Provide a number please ! ')
''' add(x,10) # TypeError: can only concatenate str (not "int") to str
# this occurs because of not converting to int
 '''

#### Way nr 1 without ELSE statment
try:
    add(x,10)
except:
    print('Exception and error happened')
finally:
    print('I always RUN')


#### way nr 2 with ELSE and TYPE ERROE

try:
    # add(x,10)
    print('TYR STATMENT')
except TypeError:
    print('Error happened ')
else:
    print('You entereed else statment')
    print(add(int(x),10))
finally:
    print('I run always HAHAHA')


# TRY EXCEPT with file handling
try:
    r = open('newfile.txt','r')
    r.write('This is the first line')
    r.close()
except OSError:
    print('I/O exception happened')
finally:
    print('I run always')



def ask_for_integer():
    
    while True:
        try:
            result = int(input('Please provide a number '))
        except:
            print('Whoops, you have not enter a number')
            continue
        else:
            print('Well, every thing went well')
            print(result)
            break
        finally:
            print('I RUN ALWAYS')

# ask_for_integer()


#--------------------------------------------------------
# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.'



try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print(' the list has none digits values')


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. 
# Then use a finally block to print 'All Done.'

    x = 5
    y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('Error , Division by Zero')
finally:
    print('All done')



# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask_square():
    while True:    
        try:
            user = int(input('Please type a number to calculate the square of it '))
        except TypeError:
            print('You have entered a wrong type')
            continue
        except:
            print('Wrong type error, please enter a digit ')
            continue
        else:
            return user**2
            break
        
print(ask_square())    

"""

# # # # # # # # # #  part 83-85 (Pylinting and Unitesting) # # # # # # # # #

# inside unitest folder there is a Pylint_sample1.py file which is runned by Pylint.
# run this command line: Pylint -r y Pylint_sample1.py
#  try to correct the issues until you get 10/10.

### Unitest

#the title function is located inside unittest folder and the file named TITLED
from Unittests import titled
from Unittests import cap

import unittest

class test_title(unittest.TestCase):

    def test_title_one_word(self):
        text = 'Python'
        result = titled.title_text(text)
        self.assertEquals(text,result)

    def test_title_multi_words(self):
        text = 'Mondy Python'
        result = titled.title_text(text)
        self.assertEquals(text,result)

    def test_cap_one_word(self):
        text = 'python'
        res = text.capitalize()
        result = cap.cap_func(text)
        self.assertEquals(res,result)
        

    def test_cap_multi_words(self):
        text = 'Mondy Python'
        res = text.capitalize()
        result = cap.cap_func(text)
        self.assertEquals(res,result)
       
       

if __name__ == "__main__":
    unittest.main()