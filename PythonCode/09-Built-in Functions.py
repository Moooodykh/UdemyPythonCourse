# ------------------------ Section 9 "Built in functions" is from part 1 to 9   -----------------------------

# # # # # # # # # #  part 1 (Map Function) # # # # # # # # #
# map is used to aply iterable(list) to a function.

def ferhernheit(temp):
    return (9.0/5)*temp + 32

temp_list = [0,22,33,100]

print(list(map(ferhernheit,temp_list)))

# we can used lambda expression 
print(list(map(lambda n: (9.0/5)*n + 32, temp_list)))

print('*'*100)
##### map can be used with more than one argument:
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(list(map(lambda x,y:x+y,a,b)))# taking the a[0] adding to b[0] and so on.
print(list(map(lambda x,y,z:x+y+z,a,b,c)))# taking the a[0] adding to b[0] adding to c[0] and so on.


#--------------------------------------------------------

# # # # # # # # # #  part 2 (Reduce  Function) # # # # # # # # #

# # # # # # # # # #  part 3 (Filter Function) # # # # # # # # #

# # # # # # # # # #  part 4 (Zip Function) # # # # # # # # #

# # # # # # # # # #  part 5 (Enumerate Function) # # # # # # # # #

# # # # # # # # # #  part 6 (all() and any() Function) # # # # # # # # #

# # # # # # # # # #  part 7 (Complex Function) # # # # # # # # #

# # # # # # # # # #  part 8 (Built-in Functions Assessment Test) # # # # # # # # #

# # # # # # # # # #  part 9 (Built-in Functions Assessment Test - Solution) # # # # # # # # #

