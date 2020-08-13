import sys,os
print(__file__)
print(__name__)

file_directory = __file__
print(sys.path.insert(1, file_directory))

def func2():
    print('FUNC()2 CALLED FROM Three.PY')


