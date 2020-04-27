# ONE.PY

import sys,os
my_dir ='E:/PROGRAMMING/github/UdemyPythonCourse/PythonCode/Mainpackage/SubPackage/'

#this CODE WILL HELP US TO import func2 from three.py which is located in other directory
#three.py is just to try to implement import functinality
sys.path.insert(1, my_dir)
from three import func2



def func():
    print('FUNC() CALLED FROM ONE.PY')


print('Top-level of ONE.PY')  
func2()

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")