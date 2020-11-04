# ------------------------ Section 21: Bonus Material -Introduction to GUIs is from part 145 to 151   -----------------------------

# # # # # # # # # #  part 145 ( Introduction to GUIs) # # # # # # # # #
# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/3547984#overview


# # # # # # # # # #  part 146 ( Quick note about ipywidgets) # # # # # # # # #
# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/7473134#overview


# # # # # # # # # #  part 147 ( Interact Functionality with GUIs) # # # # # # # # #
from ipywidgets import interact,interactive,fixed
import ipywidgets as wid
from ipywidgets import widgets

# we need to define a function and pass it to the interact to see how that works
def func_x(x):
    return x

#we need to define a default values and INTERACT is smart enough to determine what it needs to show us

### 1. Example one : INTERGERs
interact(func_x,x = 10)
### 2. Example two : STRING
interact(func_x,x = 'Hello')
### 3. Example three : BOOLEAN
interact(func_x,x = True)


from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f,a=10,b=20)
display(w)

# # # # # # # # # #  part 148 ( Advanced Lists) # # # # # # # # #
# # # # # # # # # #  part 149 ( Advanced Python Objects Assessment Test) # # # # # # # # #
# # # # # # # # # #  part 150 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
# # # # # # # # # #  part 151 ( Advanced Python Objects Test - Solutions) # # # # # # # # #
