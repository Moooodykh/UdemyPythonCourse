# ------------------------ Section 12 :Python Decorators is from part 81 to 82   -----------------------------

# # # # # # # # # #  part 81 (Decorators with Python Overview) # # # # # # # # #
"""
# Decorators can be thought of as functions which modify the functionality of another function. 
# They help to make your code shorter and more "Pythonic".
# To properly explain decorators we will slowly build up from functions. 
# Make sure to run every cell in this Notebook for this lecture to look the same on your own computer.
# So let's break down the step

def simple():
    return 1

s = 'global'

def check_for_locals():
    print(locals())
check_for_locals()

def we():
    x = 1
    y = 2
    print(locals()) # calling all the local variables
    print(locals()['y']) # calling all the local variables which called 'y'
    print(x+y)

we()

print(globals().keys()) # calling all the global variables
print(globals().keys()) # calling all the global variables KEYS ONLY
print(globals().values()) # calling all the global variables VALUES ONLY
### this is the answer and all global variables , if I need to call one 
# {'__name__': '__main__', '__doc__': None, '__package__': None, 
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000178BFC8C048>, 
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
# '__file__': 'c:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\Section 12 Python Decorators.py', 
# '__cached__': None, 'simple': <function simple at 0x00000178BFF912F0>, 's': 'global', 
# 'we': <function we at 0x00000178BFF91378>}
print(globals()['__file__']) #calling all the global variables and which file is running
print('*'*100)

print(locals().items())
print('+'*100)



def hello(name='Jose'):
    print('The Hello() function called')

    def greet():
        print('The greet() function called')
    
    def welcome():
        print('The welcome() function called')
    
    greet() # this will enable calling the greet func from inside hello func
    welcome() # this will enable calling the welcome func from inside hello func
    


hello() # IF I want to call GREET OR WELCOME function I NEED to call them from HELLO func

### IF I want to acces these two functions GREET AND WELCOME from OUTSIDE.
#welcome() # this is wrong(NOT DEFINED FUNCTION)

wel = hello
print(wel)
print(wel())

# I can save them to a variable.

def hello2(name='Jose'):
    
    def greet2():
        return '\t This is inside the greet() function'
    
    def welcome2():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet2
    else:
        return welcome2

xx = hello2() # WE are assigning xx to the greet func not to greet() which means excute greet function.
print(xx)
print(xx())
# we can call the result directly
print('-'*100)
print(hello2()()) # calling and excuting greet2 function because the default name is 'Jose'
# If I want to call welcome2 func
yy = hello2('Sam')
print(yy)
print(hello2('Same')()) #calling and excuting welcome2 function because the default name is 'Jose'

# ------------------------------------------------
### another example
def cool():
    
    def super_cool():
        return('I am super cool')
    
    return super_cool

callingCool = cool()
print(callingCool)
print(callingCool())

#-------------------------------------------------------
################### calling function from another function ###############
print('-'*100)
def hi():
    return 'Hi Mooody'
def other(some_def_func):
    print(
        'Other code to be run here'
        )
    print(some_def_func()) # running the passsed function

other(hi) # Paasing the name of the function withour excueting the function HI


#################################DECORATOR#######################################
print('/'*100)

def func_need_decoration():
    print('I need to have decoreation')

def new_decoration(func):

    def wrap_func():
        print('Some extra code will be run BEFORE the decoration')
        func()
        print('Some extra code will be run AFTER the decoration')
    return wrap_func

### way nr 1 by calling the decorator
func_need_decoration() # calling the original function
decorated_func = new_decoration(func_need_decoration)
decorated_func() # calling the decoration wrap_func()


### way nr 2 by calling the decorator
# we need to define new decoration before
print('"'*100)
# If I want to call the decoration I add @new_decoration 
@new_decoration
def func_needsdecoration():
    print('I need to have decoreation'.upper())


func_needsdecoration()
print('='*100)
# otherwise #@new_decoration
# @new_decoration
def func_needsdecoration2():
    print('I need to have decoreation'.upper())
func_needsdecoration2()

 """
# # # # # # # # # #  part 82 (Decorators Homework) # # # # # # # # #
