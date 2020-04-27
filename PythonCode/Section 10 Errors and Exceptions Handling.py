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



# # # # # # # # # #  part 74 (Pylint Overview) # # # # # # # # #




# # # # # # # # # #  part 75 (Running tests with the Unittest Library) # # # # # # # # #


