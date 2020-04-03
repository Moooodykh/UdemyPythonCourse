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