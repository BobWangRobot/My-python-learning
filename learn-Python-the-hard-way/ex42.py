## Animal is-a object (yes, sort of  confusing) look at the extra credi
class Animal(object):
    pass

## Dog is a animal
class Dog(Animal):

    def __init__(self, name):
        ## add dog's name
        self.name = name

## cat is a animal\animal has cat
class Cat(Animal):

    def __init__(self, name):
        ##add cat's name
        self.name = name

## person is a object
class Person(object):

    def __init__(self, name):
        ## person has a name
        self.name = name

        ##Person has-a pet of some kond
        self.pet = None

## employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ??hmm what is this strange magic?super transfer Parent class object, like name
        super(Employee, self).__init__(name)
        ## employee has a salary
        self.salary = salary

## fish is a object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## halibut is a fish(大比目鱼)
class Halibut(Fish):
    pass


## rover is_a Dog
rover = Dog("Rover")

## satna is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a maty named satan
mary.pet = satan

## frank is a employee
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
