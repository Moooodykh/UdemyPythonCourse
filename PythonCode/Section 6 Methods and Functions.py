# ------------------------ Section 6 "Methods and Functions" is from part 40 to 53   -----------------------------

# # # # # # # # # #  part 40 (Methods and the Python Documentation) # # # # # # # # #

"""
MyList = [1,2,3]
MyList.append(3)
help(MyList.insert)
#this will show what is the method doing.
#Very good link to understand different method is 
#1. https://docs.python.org/3/library/
#2. Stack overflow
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

"""
# # # # # # # # # #  part 41 (Functions in Python) # # # # # # # # #
# function is creating a clean repeatable code which will be used in different places

# def name_of_function(ONLY LOWER CASE)("variable"):
 #   '''
 #    Docstring explains function
 #  '''
#    print("Hello" + name)

#name_of_function("Jose")
#Hello Jose

# IN FUNCTION WE RETURN VALUES NOT PRINTING THEM

def add_function(num1,num2):
    return num1 + num2

result = add_function(1,2)
print(result)

def name_function():
    '''
    DOCSTRING: INFORMATION ABOUT THE FUNCTION
    INPUT: no input
    OUTPUT: hello..
    '''
    print('Hello')
help(name_function) # this will show no thing because there is no information stored about this function


# CALLING
name_function()

def say_hello(name = 'NAME'): # ='NAME' means that has a default value if I forget to add while I am calling the function from somepoint 
    #which means if I called the function say_hello() without the argument it will be a compile error
    print(f"Hello {name}")

say_hello('Waleed')
say_hello() # calling the default value 'NAME' to avoid compilation error

def hello_say(name = 'NAME'):
    return 'Hello ' + name

result = hello_say('Jose')
print(result)

def add(nu1,nu2):
    return nu1 + nu2

answer = add(20,30)
print(answer)

#way1
def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False
#way 2 
# more advanced 
def check_dog(mystr):
    return 'dog' in mystr.lower()
# becase of the down statement
print('dog' in 'My Dog is running'.lower())




# PIG LATIN FUNCTION: if the word start with Vowel we add ay to the end : apple -> appleay
#  if it start with consonant we  take the consonant to the end and then add ay : word ->ordway

def pig_latin(word):
    '''
    This function convet the text word to pig latin language
    '''
    first_letter = word[0]
    # check the vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter.lower() + 'ay'
    
    return pig_word

print(pig_latin('orange'))


# WE NEED TO IMPLEMNT
def is_prime(num):
    pass