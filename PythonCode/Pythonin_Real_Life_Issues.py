import os
import sys  

print('*'*100)

# sys.executable returns the Python.exe path
print(sys.executable)

# retrurn the directory path of the()"
DIR = os.path.dirname(sys.executable)
print(DIR)

#realpath is giving the whole path of the running file
DIR = os.path.dirname(os.path.realpath(__file__))

SCRIPT_DIR = os.path.realpath(os.path.abspath(DIR))
print(DIR)
print(os.path.abspath(DIR))
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))


DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPT_DIR = os.path.realpath(os.path.abspath(DIR))
print(SCRIPT_DIR)
# '..' is deleting which path directory now and going one level upp
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
print(REPO_ROOT)
print(sys.path)