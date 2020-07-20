# ------------------------ Section 6 "UPDATE" is from part 42-47,57,58   -----------------------------

# # # # # # # # # #  part 42 (Methods and the Python Documentation) # # # # # # # # #

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