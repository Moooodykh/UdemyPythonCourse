# ------------------------ Section 9: Modules and Packages is from part 68 to 70   -----------------------------

# # # # # # # # # #  part 68 (Pip Install and PyPi) # # # # # # # # #

#PYPI is a respository for open source third party python packages

# GOOGLE search with Python package for Excel as example
# open CMD and then type: install pip openpyxl
# The n you need to examine that the package installed correctly by typing
# Python , enter , import the name of the package and then it should be ok with out any problems
# important to know, check the documentation of the package and tutorial


""" CMD command prompt """ 
# C:\Users\Station>pip install requests
# Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (2.22.0)
# Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\programdata\anaconda3\lib\site-packages (from requests) (3.0.4)
# Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests) (2019.11.28)
# Requirement already satisfied: idna<2.9,>=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests) (2.8)
# Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests) (1.25.8)

# C:\Users\Station>pip install colorama
# Requirement already satisfied: colorama in c:\programdata\anaconda3\lib\site-packages (0.4.3)

# C:\Users\Station>python
# Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

# Warning:
# This Python interpreter is in a conda environment, but the environment has
# not been activated.  Libraries may fail to load.  To activate this environment
# please see https://conda.io/activation

# Type "help", "copyright", "credits" or "license" for more information.
# >>> from colorama import init
# >>> init()
#  from colorama import Fore
# >>> prin(Fore.RED + "Some red text")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'prin' is not defined
# >>> print(Fore.RED + "Some red text")
# Some red text
# >>> print(Fore.GREEN + "Some GREEN text")
# Some GREEN text


# # # # # # # # # #  part 69 (Modules and Packages) # # # # # # # # #

# we need creat another python file(module) and then import it to this file 


##### DEALIN WITH FILE FROM SAME DIRECTORY -----------
""" 
from my_module import my_func # my_module should be placed at the same location that file will import
my_func() # calling the funtion to see if it works
"""

##### DEALING WITH PACKAGES IN DIFFERENT FOLDERS/SUBFOLDERS ----------
# TO TREAT THE FOLDER AS PACKAGE YOU NEED TO HAVE __INIT__.PY FILE IN THE ROOT SO
# PTYHON CAN INTREPRET THE DIRECTORY AS PACKAGE DIRECRTORY

# I created the Mainpacke folder which contain subPackage directory and __init__.py
# I created the SubPackage folder which contain __init__.py

# --------------------------------------------------------------
# from SeSection 9 Modules and Packages.py I will  import functions from MAIN and SUB PACKAGE
#Added main_func.py script which contains the function that we want to import
#Added sub_func.py script which contains the function that we want to import
""" 
from Mainpackage import main_func #import the whole module(main_func.py) 
from Mainpackage.SubPackage import sub_func #import the whole module(sub_func.py) 
from Mainpackage.main_func import some_main_func
from Mainpackage.SubPackage.sub_func import some_sub_func
 """
# MainPackage can contain a lot of different scripts that can be imported.
# you can import a function inside sub package inside MAIN PACKAGE.
"""
main_func.some_main_func()
sub_func.some_sub_func()
some_main_func()
some_sub_func()
"""

# # # # # # # # # #  part 70 ( __name__ and "__main__") # # # # # # # # #
