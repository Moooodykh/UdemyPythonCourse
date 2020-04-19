# ------------------------ Section 8: Object Oriented Programming is from part 59 to 67   -----------------------------

# # # # # # # # # #  part 59 (Object Oriented Programming - Introduction) # # # # # # # # #

### OOP allows to creat code that is repeatable and organazied 
# object == classes (some people call that)
# Self : it is keyword that tells Python that this method is connected to a class , not just only function 


######
    # class NameOfClass():
    # def __init__(self,param1,param2):
        #self.param1 = param1
        #self.param2 = param2

    # def some_method(self):
            #perform some action
            #print(self.param1)
######


# # # # # # # # # #  part 60 (Object Oriented Programming - Attributes andv Class Keyword) # # # # # # # # #

""" 
class SampleWord():
    pass

my_sample = SampleWord()
# my_sample is an instance of SampleWord() class
print(type(my_sample))  #<class '__main__.SampleWord'>


class Dog():
    def __init__(self,breed): # attributes
        self.breed = breed


my_dog = Dog(breed='Lab')

print(type(my_dog))
print(my_dog.breed)

#### more explaining:

class Dog2():
    def __init__(self,mybreed): 
        # attributes
        # We take in the argument
        # Assign it using sel.attribute_name
        self.class_attribute = mybreed
                #NAME OF THE CLASS ATTRIBUTES
my_small_dog = Dog2('Gelski')
print(type(my_small_dog))
print(my_small_dog.class_attribute)#NAME OF THE CLASS ATTRIBUTES  and this can be change according to class defenition


class Cat():
    def __init__(self,breed,name,spots):
        self.breed = breed #we are expecting string
        self.name = name #we are expecting string
        # excepect boolean TRUE/FALSE
        self.spots = spots
        
my_blond_cat = Cat('House','Jody',True)
print(type(my_blond_cat))
print(my_blond_cat.name)
print(my_blond_cat.breed)
print(my_blond_cat.spots)
"""

# # # # # # # # # #  part 61 (Object Oriented Programming - Class Object Attributes and Methods) # # # # # # # # #
""" 
#--------------------------------------------------------------------------------------
##### SELF NEED TO BE CALLED EVERYWHERE IN THE CLASS CALLING, IN METHODS AND ATTRIBUTES
#--------------------------------------------------------------------------------------
class Dog():
    # CLASS OBJECT ATTRIBUTE 
    #THIS IS SAME FOR ANY INSTANCE
    species = 'mammal'

    #ATTRIBUTES
    def __init__(self,breed,name):
        self.breed = breed
        self.name  = name

    #ACTION/OPERATIONS --> (METHODS)
    def bark(self):
        print("WOOOOF!!")
        print("my name is : {}".format(self.name))

    # ,ethod can take external attributes
    def barking(self,number):
        print('WOOOF!!')
        print(f'My name is {self.name} and my number is {number}')



# SELF keyword will be attached(shown) when you call your instance
my_s_dog = Dog('Lab','Poppy')

print(my_s_dog.species)
print(my_s_dog.breed)
print(my_s_dog.name)
my_s_dog.bark()
my_s_dog.barking(20)

print('----------------------------------------------------------')

class Circle():
    #COMMON ATTRIBUTE
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    # Attributes
    def __init__(self,Radius=1):  # Radius = 1 is a default value if no body will override the value
        self.radius = Radius
        self.area = Radius * Radius * self.pi #or  Circle.pi
        self.area2 = Radius * Radius * Circle.pi
        # LINE 116 and 117 is equals
    # Methods
    def get_circumference(self):
        return 2 * self.pi * self.radius 


small_circle = Circle(5)
print(small_circle.pi)
print(small_circle.radius)
print(small_circle.area)
print("the circumference is : " + str (small_circle.get_circumference()))

"""
"""
ADDING ANOTHER EXAMPLE OR RECTANGULAR, TRIANGEL AND SEQUARE
"""
# # # # # # # # # #  part 62 (Object Oriented Programming - Inheritance and Polymorphism ) # # # # # # # # #
