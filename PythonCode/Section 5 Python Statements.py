# # # # # # # # # #  part 33 (If Elif and Else Statements in Python) # # # # # # # # #

""" 
# control flow means that I will excute certain code based on conditions
# if , elif,else

# IF some_condition:
#excute some code
# elif some_other_condition
#excute something different
# else:
#excute some code

# IF
if True:
print("IT's True")

if 3>2:
print("IT's True")

hungry = False
if hungry:
print('FEED me')
# IF ELSE
if hungry:
print('FEED me')
else:
print('I am not hungry')
print('---------------------------------------')
# IF ELIF ELSE
loc = 'stadium'
if loc == 'Auto shop':
print('Cars are cool')
elif loc == 'bank':
print('Money  is cool')
elif loc == 'Store':
print('Welcome to STORE')
else:
print('I do not know much')


# other example
name = 'John'

if name=='Gabi':
print('Hello Gabi')
elif name == 'Sammy':
print('Hello Sammy')
else:
print('Hello, what is your name ')
"""

# # # # # # # # # #  part 34 (For Loops in Python) # # # # # # # # #

""" 
# for means "ITERATE"
# my_iterabel = [1,2,3]
# for item_name in my_iterabel:
#    print(item_name)
mylist = [1,2,3,4,5,6,7,8,9,10]
for number in mylist:
print(f"{number:1.2f}, hello ")


for item in mylist:
# check for even
if item % 2 == 0:
print(item)
else:
print(f"odd number,{item}")


list_sum = 0
for num in mylist:
list_sum = list_sum + num
print(list_sum)  # this will print the perodic sum  

print(list_sum) # this will print the final result 


My_string = 'Hello World'
for charc in My_string:
print(charc)

for _ in 'Hello world':
#print('cool!')
print(_)


tup = (1,2,3)
for iten in tup:
print(iten)

print('--------------------------------')
new_list = [(1,2),(3,4),(5,6),(7,8)]
print(len(new_list))
for each in new_list:
for m in each:
print(m)


# TUPLE unpacking 
for (a,b) in new_list:
print(a)
print(b)
# this will print all elemnts 

for (a,b) in new_list:
print(a)
# this will print first element 

for a,b in new_list:
print(b)
# this will print second element 

new_l =[(1,2,3),(4,5,6),(7,8,9)] 
for a,b,c in new_l:
print(b)

print('******************************')
dic = {'k1':1,'k2':2,'k3':3,'k4':4}

for Nitem in dic:
print(Nitem) # this will loop through the keys


# if we want the value we need to call .items() method to the dictionary and then use TUPLES UNPACKING way
for key,value in dic.items():
print(key)
print(value)

# if we want only values we need to call .values() method to the dictionary
for keys in dic.values():
print(keys)
"""

# # # # # # # # # #  part 35 (While Loops in Python) # # # # # # # # #


"""
# while some_condition(true):
# do something
# else:
# do something else

### WHILE
x = 0
while x<5:
print(f"the current value of is {x}")
x = x + 1
# YOU NEED TO ADD A CONDITION TO STOP WHILE LOOP, otherwises it will continue forever

print('**************************')
### WHILE ELSE
y = 50
while y < 5:
print(f"the current value of is {y}")
y += 1
else:
print(f"y is not less than 5")


#---------------------- these words work with all loops , for while.....
### BRAEK: Break out of the current closest enclosing loop 
myString = 'Sammy'
for e in myString:
if e == 'a':
break # when It comes to a letter it will go out of this for loop
print(e)
#IF I want to stop the loop when I reach some thing I use BREAK


### CONTINUE:goes to hte top of the closet enclosing lopp
# which means If I want to ignor some thing and be back again to the start of the loop
myString = 'Sammy'
for letter in myString:
# f I want to avoid 'a' letter
if letter == 'a':
continue # will send me to the start of for loop again
print(letter) 

### PASS:doe nothing at all
x=[1,2,3]
for item in x:
# if you leave it empty
#SyntaxError: unexpected EOF while parsing
# we use Pass
pass 

print('end of my script')

print('**************************')
# break pass contiue with while

z = 0
while z<7:# do not forget to break the condition otherwise it will be endless
if z == 1:
pass
elif z == 3 :
z += 1
continue
elif z == 5:
break
print(z)
z += 1
"""

# # # # # # # # # #  part 36 (Useful Operators in Python) # # # # # # # # #

""" 
### RANGE 
# is a generator of values, RANGE(start,stop"excluding this number",step)
for num in range(0,10,2): 
    print(num)
range(0,10,2) # from 0 to 9 with step 2
range(3,10) ## from 3 to 9 with step 1
range(10) # from 0 to 9 step 1

# We can put that range in a list by casting LIST to a range
my_list  = list(range(3,10))
print(my_list)


### ENUMERATE 
# is an index coming with string,list.....objects which count the index
count_index = 0
word = 'abcdef'
for letter  in word:
    print('letter {} coming with a index number {}'.format(letter,count_index))
    count_index += 1

# or 
index = 0
for charc in word:
    print(word[index] + ' is coming in {} index position'.format(index))
    index+= 1

# OR - EMUMERATE
for a in enumerate(word):
    print(a) # this will print 
             #(0, 'a')
             #(1, 'b')
             #(2, 'c')
             #(3, 'd')
             #(4, 'e')
             #(5, 'f')

for index , value in enumerate(word):
    print(str(index) + ' index has a value ' + str(value))
    # print(value)

### ZIP
# this function is joining two lists together , opposite of enumerat

list1 =[1,2,3]
list2 =['a','b','c']
list3 = [100,200,300]
print (zip(list1,list2)) # this will show this message :zip object at 0x0000025224B180C8 , we need to iterate through the object
for item in zip(list1,list2,list3): 
    print(item)

# zip will zip the shortest of the lists
list1 =[1,2,33,4,5,6] # 6 elements
list2 =['a','b','c']
list3 = [100,200,300]
itemList = []
for item in zip(list1,list2,list3): 
    #print(item) # the answer will be as above zip will zip based on the shortest of the lists
    #(1, 'a', 100)
    #(2, 'b', 200)
    #(33, 'c', 300)
    print(list(item))

# or
print('Other way of making a list of zipped things together')
print(list(zip(list1,list2,list3)))

print('############################')


### IN 
# will check if the item in the list,string....etc and return TRUE or FALSE
result = 'x' in [1,2,3]
result1 = 'x' in 'The horizonx'
result2 = 'mykey' in {'mykey':1,'key2':2} # this will check the keys only
result3 = 2 in {'mykey':1,'key2':2}.values() # checking the value
print(result3)

# INPUT
Inresult = input('What is your name')  # every thing is taken as a STRING
print(f"hello , {Inresult}")

calcnum = input('what is your favorite number')
seqaure = int(calcnum) ** 2
print(f"the input :{calcnum} and it's sequare :{seqaure}")
#OR


calcnum = int(input('what is your favorite number'))
seqaure = calcnum ** 2
print(f"the input :{calcnum} and it's sequare :{seqaure}")

##### Arithmetic functions #####

### MIN / MAX 
listnew = [1,2.3,44,25,-2] 
print(str(min(listnew)) + ' is the minimum number of the list')
print(str(max(listnew)) + ' is the max number of the list')

### RANDOM
from random import shuffle
my_list_sh = [1,2,3,4,5,6,7,8,9,0]
print(f"my orginal list is : {my_list_sh}")
shuffle(my_list_sh)
print(f"my list after shuffling :  {my_list_sh}")

from random import randint
print(randint(0,99))

 """
# # # # # # # # # #  part 37 (List Comprehensions in Python) # # # # # # # # #