# ------------------------ Section 14 "UPDATE" is from part 103-115   -----------------------------

# # # # # # # # # #  part 103 (Methods and the Python Documentation) # # # # # # # # #
# MODULES

# # # # # # # # # #  part 104 (Python Collections Module) # # # # # # # # #

""" 
################### Counter class ########################
# we use it to count how many times a list member shows up
# Counter is dictionary sub class , which means it is a dictionary at the end
from collections import Counter

mylist = [1,1,1,2,3,4,3,3,3,4,2,2,1,4,5,1]
mylist2 = ['a','a',5,2,2,1,1,5,1]
x = Counter(mylist2)
print(Counter(mylist))
print(Counter(mylist2))
print(x['a'])

# we can count also strings
word ='aaasvvvssddsssdsddsdsb'
print(Counter(word))

# we can count also words in a sentence but do not forget to call split function
sentence = 'How many words has been shown with word word'
print(Counter(sentence.split()))

####Special methods with Counter
letters = 'aaaaaaabbbbbsssssssdddddddeeeeeeeeeeee'
c = Counter(letters)
#Most common: will return the result as TUPLE sorted by the most item repeated and descently
print(c.most_common())
print(c.most_common(3))# 3 means give the most 3 common items.


####this is a list about what we can do
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts

print(c.values())# Give you all counts for each element as a LIST  a=7,b=5....etc.
c.clear() #reset all counts
print(c.values())# Give you all counts for each element a=7,b=5....etc.
c = Counter(letters)
print(list(c))# Give you all uniqe elements as List
print(set(c))# Give you all uniqe elements as SET
print(dict(c))# Give you all elements and counts as DICT
print(c.items())# Give you a list whch contains of PAIRS (element,count)


list_of_pairs = c.items()
print(Counter(dict(list_of_pairs))) #convert from a list of (elem, cnt) pairs
print((dict(list_of_pairs)))
print(c.most_common()[::-1]) # give us all elements ordered from least common element
print(c.most_common()[-1::]) #give us least common elements as LIST
print(c.most_common()[-1]) #give us least common elements as ELEMENT (TUPLE) 
print('*'*100)


################### Default Dictionary ########################
# this is as normal dictionary but when u try to see some key value which is not exist it will take a defualt value as zero.

d = {'a':100,'b':200}
print(d['a'])
# print(d['wrong'])
# this will print key error because we do not have 'wrong' as key
# to continue running we use defaultdict
from collections import defaultdict

dd = defaultdict(lambda : 0)

dd['wow']= 100
dd['hello']= 400
dd['yay']= 200
print(dd['we']) # default value will be invoked
print(dd)

################### Tupled named ########################

from collections import namedtuple

#this is a developed tuple which can be calling either by index or attribute name
mytuple = (10,20,30)
print(mytuple[0]) # normall calling

Ntuple = namedtuple('Dog',['age','name','color'])
print(type(Ntuple))

sam = Ntuple(age =5,color = 'red',name = 'Sam')
print(sam.age)
print(sam.color)
print(sam.name)
print(sam[0])
print(sam[1])
print(sam[2])
print(sam)
"""

# # # # # # # # # #  part 105 (Opening and Reading Files and Folders (Python OS Module)) # # # # # # # # #
"""
# we will use OS as library to check the folders and report the every thing exists in that directory
# We use Shutil to move the staff around

import os,shutil

#printing the working directory
file_path = os.getcwd()
full_path = os.path.join(file_path,'PythonCode\Top_level_folder')
print(os.getcwd())
print(full_path)
os.chdir(full_path)
print('*'*100)

print(os.getcwd())


f = open('Practice.txt','w+')
f.write('This is the file')
f.close()

print('Currtent directory:',os.listdir()) # printing all files and folders inside the directory


# OR any other directory by passing the source path
print('Other directory:',os.listdir(file_path))
print(os.listdir("E:\\PROGRAMMING\\github\\UdemyPythonCourse\\PythonCode\\Top_level_folder\\"))
source = "E:\\PROGRAMMING\\github\\UdemyPythonCourse\\PythonCode\\Top_level_folder\\Practice.txt"
new_path=os.path.join(file_path,'PythonCode\Top_level_folder\mid_2_level_folder')
print(new_path)

shutil.move(source,new_path)
"""
##### SECOND PART##### 
""" 
import os, shutil
print(os.getcwd())
print(os.listdir())
new_path = os.path.join(os.getcwd(),'PythonCode\Top_level_folder')
print(new_path)
os.chdir(new_path)
print(os.getcwd())

f = open('Welcome.txt','w+')
f.write('Hello and welcome to our course')
f.close()

shutil.copy('Welcome.txt','C:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\Top_level_folder\\mid_2_level_folder')

#sending the file to recycle bin
import send2trash
send2trash.send2trash('C:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\Top_level_folder\\mid_2_level_folder\\Welcome.txt')
print('Top Level directory:',os.listdir('C:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\Top_level_folder\\'))
print(os.getcwd())

#making a copy of the whole directory but the folder name must not be exist before
shutil.copytree(os.getcwd(),'C:\\Area MK\\Learning\\OOO')
# sending the whole folder to recycle bin
send2trash.send2trash('C:\\Area MK\\Learning\\OOO')


shutil.copytree(os.getcwd(),'C:\\Area MK\\Learning\\OOO')
#reading the disk usage of the specific folder
print(shutil.disk_usage('C:\\Area MK\\Learning\\OOO'))
#make archive of that specific folder by adding the extention as string 'ZIP'
shutil.make_archive('C:\\Area MK\\Learning\\OOO','zip')
#removing the whole tree of that folder
shutil.rmtree('C:\\Area MK\\Learning\\OOO')

"""
##################### WALK METHOD ##############################

# this method is going through each folder -> sub_folders -> files 

""" 
print('*'*100)
print(os.getcwd())
for folder, sub_folders, files in os.walk('C:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\Top_level_folder'):
    print('\n')
    print(f'Currently we are looking at folder {folder}')
    print('Subfolders are:'.upper())
    for sub_older in sub_folders:
        print('\tSubfolder:',sub_older)
    print('files are:'.upper())
    for fil in files:
        print('\tfile:',fil)    
"""
"""
print('-'*100)
# I am using r'' as raw data to avoid putting a lot of backslash
# Note that the string did not end with a #\\


print(work_path)
os.chdir(work_path)
"""
#work_path =r"C:\Area MK\Learning\UdemyPythonCourse\PythonCode"
"""
#this is also right
# os.chdir('C:\\Area MK\\Learning\\UdemyPythonCourse\\PythonCode\\')
for folder, sub_folders, files in os.walk('Top_level_folder'):
    print('\n')
    print('Currently we are looking at folder:',folder.upper())
    print('Subfolders are:'.upper())
    for sub_older in sub_folders:
        print('\tSubfolder:',sub_older)
    print('files are:'.upper())
    for fil in files:
        print('\tfile:',fil)    
"""

# # # # # # # # # #  part 106 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 107 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 108 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 109 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 110 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 111 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 112 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 113 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 114 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 115 (Methods and the Python Documentation) # # # # # # # # #
