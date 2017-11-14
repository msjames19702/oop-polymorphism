# Create Animal() superclass object.
class Animal(object):
    
    #Class Object Attribute
    species = 'mammal'
    bloodtype = 'warm blooded'
    
    def __init__(self):
        pass
        
    def whoAmi(self):
        print "Animal"
        
    def eat(self):
        print "Eating"

# Create Dog() subclass object and functions. Make use of Inheritance.
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog subclass instance created"
        
    def whoAmi(self):
        print "I'm a Dog"
        
    def sound(self):
        print "I go Woof!"
        
    def whatIdo(self):
        print "I play fetch the ball!"

# Create Cat() subclass object and functions. Make use of Inheritance.
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Cat subclass instance created"
        
    def whoAmi(self):
        print "I'm a Cat"
        
    def sound(self):
        print "I go Meow!"
        
    def whatIdo(self):
        print "I play with yarn!"

# Create Cow() subclass object and functions. Make use of Inheritance.

class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Cow subclass instance created"
        
    def whoAmi(self):
        print "I'm a Cow"
        
    def sound(self):
        print "I go Mmmmoooooo!"
        
    def whatIdo(self):
        print "I just like to eat hay!"
        
# Create object instances Animal(), Dog(), Cat() and Cow()

animalObject = Animal()
dogObject = Dog()
catObject = Cat()
cowObject = Cow()
        
# Functional polymorphisms

def whatAmi(animaltype):
    animaltype.whoAmi()

def soundImake(animalsound):
    animalsound.sound()

def iDo(animaldoes):
    animaldoes.whatIdo()

# Calling objects as parameters to make use of polymorphism

print ""
whatAmi(dogObject)
soundImake(dogObject)
iDo(dogObject)
print ""

whatAmi(catObject)
soundImake(catObject)
iDo(catObject)
print ""

whatAmi(cowObject)
soundImake(cowObject)
iDo(cowObject)
print ""

# Making use of class objects but not using polymorphism

print "The species of a dog is "+dogObject.species
print "Mammals are "+catObject.bloodtype