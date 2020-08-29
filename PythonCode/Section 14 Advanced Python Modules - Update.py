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

# # # # # # # # # #  part 106 ( Python Datetime Module) # # # # # # # # #

""" import  datetime

### TIME
mytime = datetime.time(5,20)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)

### DATE
mt = datetime.datetime.today()
print(mt)
print(mt.year)
print(mt.month)
print(mt.day)
print(mt.ctime()) # another time format


from datetime import datetime
my_time = datetime(2020,9,23,22,33,44,23) # this is specifying the Day and Hours
print(my_time)
my_time=my_time.replace(year=2050) # replace if I want to modify some time/date
print(my_time)


#### Usign Arthimtetic with:
### DATE
date1 = datetime(2021,8,12)
date2 = datetime(2017,5,13)
result = date1 - date2
print(result)
print(type(result))
print(result.days)

###TIME
dateime1 = datetime(2021,11,3,3,22,0)
dateime2 = datetime(2021,11,3,3,12,0)
mydiff = dateime1 - dateime2
print(mydiff)
print(mydiff.days)
print(mydiff.seconds)
print(mydiff.total_seconds())



import datetime

t = datetime.time(4, 20, 1)

# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)


today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('From ordinal:', today.fromordinal(737657))
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)
"""

# # # # # # # # # #  part 107 (Python Math and Random Modules) # # # # # # # # #

""" 
####MATH
import  math
# calling the help for MATH lib
# help(math) 

value = 4.35
print(math.floor(value)) # round it down
print(math.ceil(value)) # rount it up
print(round(value)) #normal round

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)# NOT A NUMBER

# NUMPY is a specific library which can be used when we used complex marthmatic operation

print(math.log(math.e))

# to define your log and base we can define that
print(math.log(100,10)) # which means I have 10 as a base , which number is as power to have 100 as result
print(math.sin(10))# radians
print(math.degrees(math.pi/2))# degrees
print(math.radians(180))# radians

print('*'*100)
####RANDOM
import random
print(random.randint(0,100))
random.seed(101) # THIS will make the randon as same place
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))


### other thing
mylist = list(range(5,20))
print(mylist)
print(random.choice(mylist)) # choose one item randomly

# choose multipile items randomly
#1. SAMPLE WITH REPEATED ITEMES
print(random.choices(mylist,k=5)) # choose five items randomly
#2. SAMPLE WITHOUT REPEATED ITEMES
print(random.sample(mylist,k=5)) # choose five items randomly unique five elements

random.shuffle(mylist)# SHUFFLE THE LIST
print(mylist)

#IF WE WANT TO HAVE A RANDOM FLOAT NUMBERS
ele = random.uniform(0,100)
print(ele)

print(random.gauss(mu=0,sigma=1))
"""

# # # # # # # # # #  part 108 ( Python Debugger) # # # # # # # # #
"""
import pdb

x = [1,2,3]
y = 2
z = 3

result1 = y + z

pdb.set_trace()

result2 = x + y
"""
# # # # # # # # # #  part 109 (Python Regular Expressions Part One) # # # # # # # # #
"""
print('hello' in 'hello man how are you?')

pattern = 'hello'
text = "The person's phone number is 408-555-1234. Call soon! hello hello hello"

import re

#this is to find the first object
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.start())
print(match.end())


mat = re.findall(pattern,text)
print(mat)
print(len(mat))

#IF I need to go through the iterations 
# we use re.findIter
more_matches = re.finditer(pattern,text)
for item in more_matches:
    print(item)
    print(item.span())
    print(item.start())
    print(item.end())
#if I want to return the actual match value , use group
    print(item.group())
"""

# # # # # # # # # #  part 110 (Python Regular Expressions Part two) # # # # # # # # #

"""
###### CHARACTER IDENTINFIERS
#############################

# Code	Meaning                                 EXAMPLE PATTERN         EXAMPLE MATCHING
# \d	a digit                                 file_\d\d               file_25
# \D	a non-digit                             \D\D\D                  ABC
# \s	whitespace (tab, space, newline, etc.)  a\sb\sc                 a b c 
# \S	non-whitespace                          \S\S\S\S                Yoyo
# \w	alphanumeric                            \w-\w\w-1               _-bc-1
# \W	non-alphanumeric                        \W\W\W\W                +-*/
import re
text = 'my phone number is 992-442-5523'
pattern = '\d\d\d-\d\d\d-\d\d\d\d'
pattern2 = '\d{3}-\d{3}-\d{4}'
pattern3 = r'\d{3}-\d{3}-\d{4}'
match1 = re.search(pattern,text)
match2 = re.search(pattern2,text)
match3 = re.search(pattern3,text)
print(match1)
print(match1.group())
print(match2)
print(match2.group())
print(match3)
print(match3.group())


###### CHARACTER QUANTIFIERS
#############################

# Code	Meaning                                 EXAMPLE PATTERN         EXAMPLE MATCHING
# + 	occurs one or more                      Version\w-\w+           VersionA-b-sdsdsd
# {3}	occurs exacly three times               \D{3}                   123
# {2,4}	occurs between 2 and 4 times  a\sb\sc   \d{2,4}                 4556
# {3,}	occurs three or more times              \w{3,}                  Anycharacter
# * 	occurs zero or more times               A*B*C*                  AAACCC (Zero or more A followed by zero or more B followed by zero or more C)
# ? 	occurs once or none                     Plurals?                Plural ('l' followed by Zero or one s)


import re
text = 'my phone number is 992-442-5523'
c_pattern = r'\d{3}-\d{3}-\d{4}'

match_number = re.search(c_pattern,text)
print(match_number) 
print(match_number.group()) 

###### COMPILE is a great function to extract the information from patterns based on dividing them to groups
# and then call which group you want as example I want to call the first three numbers
# EACH () is a GROUP
compile_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(compile_pattern,text)
print(result)
print(result.group())#calling the whole number
print(result.group(1))#calling the first three numbers
print(result.group(2))#calling the second three numbers
print(result.group(3))#calling the third three numbers
"""

# # # # # # # # # #  part 111 (Python Regular Expressions Part three) # # # # # # # # #








########################################################################################
########################## DO NOT GO OUT FROM RE UNTIL YOU CHECK THE OLD JYPTER NOOTBOOK
########################################################################################


# # # # # # # # # #  part 112 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 113 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 114 (Methods and the Python Documentation) # # # # # # # # #
# # # # # # # # # #  part 115 (Methods and the Python Documentation) # # # # # # # # #
