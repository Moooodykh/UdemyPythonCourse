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

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

#-----------------------------------------------------------------
# ADDING ANOTHER EXAMPLE OR RECTANGULAR, TRIANGEL AND SEQUARE

class Rectangular():
    # Gnereal class attributes

    # attributes
    def __init__(self,lenght=3,width=1):
        self.length = lenght
        self.width = width
    # methods
    def get_area(self):
        return self.length * self.width
    def get_circumference(self):
        return (self.length + self.width) * 2

class Triangel():
    # common class attributes

    # attributes
    def __init__(self,a,b,c,height):
        self.firstline = a
        self.secondline = b
        self.thirdline = c
        self.height = height
        
    # methods
    def get_area(self):
        return self.firstline * self.height
    def get_circumference(self):
        return self.firstline + self.secondline + self.thirdline


small_rectangular = Rectangular()
print('Small recatngualr')
print(f"length: {small_rectangular.length} , width: {small_rectangular.width}")
print(small_rectangular.get_area())
print(small_rectangular.get_circumference())

large_rectangular = Rectangular(6,2)
print(f"large --> length: {large_rectangular.length} , width: {large_rectangular.width}, area:{large_rectangular.get_area()} , circumgerence:{large_rectangular.get_circumference()}")
"""

# # # # # # # # # #  part 62 (Object Oriented Programming - Inheritance and Polymorphism ) # # # # # # # # #

# -------------------------------------- Inheritance -----------------------------

''' 
# BASE CLASS
class Animal():

    def __init__(self):
        print('Animal created')

    def hungry(self):
        print(f" Your Animal is hungry !! ")

# CHILD CLASS
class Dog(Animal):
    # Class common attributes 
    species = 'Mammal'

    # Attributes
    def __init__(self,name,age,breed): 
        Animal.__init__(self) # this is enabling us to check that the classes are ineherited
        print('Dog created')
        self.name = name
        self.age = age
        self.breed = breed
    
    # ACTIONS / METHODS
    def bark(self):
        print(f"{self.name} is barking and my age is {self.age} WOOOF!!")
        
    def eat(self):
        print(f"{self.name} is eating now , thanks for feeding me :)")

### OVERRIDING THE BASE CLASS METHOD
# IT CAN BE BY HAVING THE SAME METHOD NAME IN THE CHILD CLASS
    def hungry(self):
        print(f" DOG is hungry !! ")

# calling the # BASE and # CHILD class
mydog = Dog('Poppy',3,'Lab')

print(mydog.species)
mydog.bark()
mydog.hungry()
mydog.eat()
'''
""" 
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

 """
# -------------------------------------- Polymorphism -----------------------------

''' 
# Polymorphism is using the same name of the method from two different classes like SPEAK example
# We can call it by:
# way nr 1 
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' Says WOOF!'
        
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' Says MEOW!'

niko = Cat('Niko')
felix = Dog('Felix')

print (niko.speak())
print (felix.speak())
print('-----------------------------')
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())
    print(type(pet.speak()))

# way nr 2
print('*****************************************************')
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko) # niko is a CAT object
pet_speak(felix)# felix is a DOG object

i= 10
print('This is:', i)
print('------------------------------------------')
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says WOOOF!'
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says WOOOF!'

fido = Dog('fido')
sisi = Cat('sisi')

def pet_speak(pet):
    print(pet.speak())

pet_speak(fido)
pet_speak(sisi)
'''
# -------------------------------------- ABSTRACT CLASS -------------------------------------

''' 
# ABSTRACT CAN BE ONLY BASE CLASS WITHOUT ANY METHOD IMPLEMENTED
# ABSTRACT CLASS IS A CLASS THAT CAN BE INTIALIZED AND ALL IT'S METHOD WILL BE OVERRIDED AND 
# IMPLEMENTED IN THE CHILD CLASS

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Sub class must implement this abstract method')

myanimal = Animal('Frid')
#myanimal.speak() # this line will through an exception

# AS LONG AS YOU HAVE A __init__ METHOD IN THE BASE CLASS WE DO NOT HAVE TO HAVE IT IN THE CHILD CLASS
# UNLESS WE NEED TO ADD ATTRIBUTES

class Dog(Animal):

    def speak(self):
        return self.name + ' says WOOOF' + ' ,Sub class implemented the "abstract method" '

class Cat(Animal):
    
    def speak(self):
        return self.name + ' says MEYW' + ' ,Sub class implemented the "abstract method" '


mydog= Dog('Pop')
mycat = Cat('meme')
print(mydog.speak())
print(mycat.speak())

# real life example is to open the file is Abstract base class.
# opening an excel is inheriting open file method and then it differs from opening a text file...etc

class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Abstract method . needed to be implemented in the child class')

class Dog(Animal):
    
    def speak(self):
        return self.name + ' says WOOOF!'

class Cat(Animal):

    def speak(self):
        return self.name + ' says WOOOF!'
ani = Animal('Ani')
ani.speak()
fido = Dog('fido')
sisi = Cat('sisi')

def pet_speak(pet):
    print(pet.speak())

pet_speak(fido)
pet_speak(sisi)
'''
# # # # # # # # # #  part 63 (Object Oriented Programming - Special (Magic/Dunder) Methods) # # # # # # # # #
#http://www.tutorialspoint.com/python/python_classes_objects.htm

""" 

my_list= [1,2,3]
len(my_list) # this is possible

class Sample():
    pass

mysample= Sample()

print(mysample) # Answer will be <__main__.Sample object at 0x00000270BF6DE848>
#len(mysample) # this will give an error 
# TypeError: object of type 'Sample' has no len()

print(mysample)



class Book():
    def __init__(self,title,Author,pages):
        self.title = title
        self.author = Author
        self.pages = pages

    def __str__(self):# RETURN ALL THE TIME NOT PRINT
        return f" {self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book object is deleted')
    


        
b = Book('Python Rokcs','Moody',200)

print(b) # this will point to a memory place , <__main__.Book object at 0x000002BC9E772F08>
print(str(b)) # this is the string represetation of the book 
print(len(b))

# TO DELETE A BOOK FROM A computer MEMORY
del b
print(b)

"""

#-----------------------------------------------------------------------
#EXAMPLES FROM http://www.tutorialspoint.com/python/python_classes_objects.htm
"""  
class Employee:
    # Class common attribute
    empcounter = 0

    # Attributes
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcounter +=1

    # methods
    def display_count(self):
        print (f'Total employees are : {Employee.empcounter}')
    
    def display_employee(self):
        return F"Empoyee Name:{self.name}, Salary: {self.salary}" 

emp1 = Employee('Sivan',32000)
emp2 = Employee('Ola',42000)

print (emp1.display_employee())
print (emp2.display_employee())
emp1.display_count()

#----------------------------------------
#NICE METHODS WITH OBJECTS

#The getattr(obj, name[, default]) − to access the attribute of object
#The hasattr(obj,name) − to check if an attribute exists or not.,
#The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created
# The delattr(obj, name) − to delete an attribute.
print(hasattr(emp1,'age'))  
setattr(emp1,'age',25)
print(getattr(emp1,'age'))
delattr(emp1,'age')
print(hasattr(emp1,'age'))
print(hasattr(emp1,'name'))
setattr(emp2,'position','Architect')# Add a 'position' attribute.
setattr(emp1,'age',0)
emp1.age = 23
print (F"Empoyee Name:{emp2.name}, Salary: {emp2.salary}, age:{emp1.age} ")
print (F"Empoyee Name:{emp2.name}, Salary: {emp2.salary}, position:{emp2.position} ")
emp2.position = 'HIL engineer'  #Modify 'age' attribute.
print (F"Empoyee Name:{emp2.name}, Salary: {emp2.salary}, position:{emp2.position} ")


#----------------------------------------------------
# __dict__ − Dictionary containing the class's namespace.
# __doc__ − Class documentation string or none, if undefined. 
# __name__ − Class name.
# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode. 
# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

print ("Employee.__doc__:" , Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

#------------------------------------------------
print('*'*100)
#---------------------------------------------------------------------------

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1))
print (id(pt2))
print (id(pt3))
# prints the ids of the obejcts
# del pt1
# del pt2
# del pt3
''''''
#-----------------------------------------Multiple Inheritance -----------------------------------------
#you can drive a class from multiple parent classes as follows −
""" 

"""
class A:        # define your class A
.....

class B:         # define your class B
.....

class C(A, B):   # subclass of A and B
..... 
"""

# www.tutorialspoint.com/python/python_classes_objects.htm

""" 
class Syster:
    def __init__(self):
        print('Syster constructor called ')


class Father:
    def __init__(self):
        print('Father constructor called ')

    def fatherfeeding(self):
        print('Father feeding')


class Mohter:
    def __init__(self):
        print('Mother constructor called ')
    
    def motherfeeding(self):
        print('Mother feeding')

# MULTIPLE INHERTIANCE
class Child(Father,Mohter):
    def __init__(self):
        print('Child contructor is called')

c = Child()
f= Father()
m = Mohter()
print(c.__class__)
print(c.__class__.__name__)

# ISSUBCLASS
print(issubclass(Child,Father))
print(issubclass(Child,Syster))
print(issubclass(Child,(Father,Mohter)))
print(issubclass(Child,(Father,Syster))) # True becuase OR, which means if Child is sbuclass of father or subclass to syster

print('-----------------------------------')
# IS OBJECT INSTATNCE
print(isinstance(c,Child))
print(isinstance(c,Syster))
 """
#-----------------------------------------Base Overloading Methods  -----------------------------------------

""" 
class Vector:

######
# 1. __init__ ( self [,args...] )

# Constructor (with any optional arguments)

# Sample Call : obj = className(args)
    def __init__(self,a,b):
        self.a = a
        self.b = b 

######
# 2. __del__( self )

# Destructor, deletes an object

# Sample Call : del obj
    def __del__(self):
        print('Are you sure that you want to delete this object?')
        user_input= input('yes or no, please')
        if user_input == 'yes':
            del self
        else:
            pass

######
# 3. __repr__( self )

# Evaluable string representation

# Sample Call : repr(obj)
    def __repr__(self):
        pass

######
# 4. __str__( self )

# Printable string representation

# Sample Call : str(obj)
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

######
# 5. __cmp__ ( self, x )

# Object comparison

# Sample Call : cmp(obj, x)

    def __cmp__(self,x):
        return self.a == x


    def __add__(self,other):
        return f'Vector({self.a}+{other.a}, {self.b}+{other.b})'

v1 = Vector(5,6)
v2 = Vector(10,12)
print(v1+v2) """

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)


# -----------------------Data Hiding------------------------
# An object's attributes may or may not be visible outside the class definition. 
# You need to name attributes with a double underscore prefix, 
# and those attributes then are not be directly visible to outsiders.

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print counter.__secretCount # this will show an error 
print (counter._JustCounter__secretCount) # object._className__attrName


# # # # # # # # # #  part 64- 65 (Object Oriented Programming - Homework & Solution) # # # # # # # # #

""" 
# Problem nr 2 , 
class Cylinder:

    pi =3.14

    def __init__(self,height=1,radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return (2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius**2)
    

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


# Problem nr 1 ,
import math
class Line:

    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    

    def distance(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) 

    def slope(self):
        return ((self.y2  - self.y1 )/(self.x2 - self.x1))

    def __str__(self):
        return f'({self.coor1},{self.coor2})'
       # return '(%d,%d)' %(self.coor1,self.coor2)


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.slope())
print(li.distance())
"""

'''
TEACHER SOLUTION

class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.slope())
print(li.distance())

'''

# # # # # # # # # #  part 66- 67 (Object Oriented Programming - Challenge Overview & Solution) # # # # # # # # #

"""
print('*'*100)
class Account:
    

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount 
        print(f'Desposit accpeted, we added ${amount} to your account ')
        print(f'Your new balance:${self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Funds Unavailable in your balance, try again with less amount')
        else:
            self.balance -= amount 
            print(f'Withdrawal accpeted, you withdraw ${amount} from your account ')
            print(f'Your new balance:${self.balance} ')

    def __str__(self):
        return (f'Account owner:{self.owner} \nAccount balance:${self.balance}' )

    def __len__(self):
        return(self.balance)

acc1 = Account('Moody',500)
print(acc1)
print(acc1.owner)
print(acc1.balance)        
acc1.deposit(50)
acc1.deposit(350)
acc1.withdraw(700) 
"""
