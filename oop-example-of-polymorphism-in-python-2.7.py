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
        pass
    
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
        pass
    
    def whoAmi(self):
        print "I'm a Cat"
    
    def sound(self):
        print "I go meow!"
        
    def whatIdo(self):
        print "I play with yard!"

# Create polymorphic object instances Dog() & Cat()

dogObject = Dog()
catObject = Cat()
wolfObject = Dog()
tigerObject = Cat()

# Functional polymorphisms

def whatAmi(animaltype):
    animaltype.whoAmi()

def soundImake(animalsound):
    animalsound.sound()

def iDo(animaldoes):
    animaldoes.whatIdo()
    
# Calling the above functions with objects as arguments to illustrate polymorphism

print "Dog says ..."
whatAmi(dogObject)
soundImake(dogObject)
iDo(dogObject)

print "Cat says ..."
whatAmi(catObject)
soundImake(catObject)
iDo(catObject)

print "Wolf says ..."
whatAmi(wolfObject)
soundImake(wolfObject)
iDo(wolfObject)

print "Tiger says ..."
whatAmi(tigerObject)
soundImake(tigerObject)
iDo(tigerObject)
