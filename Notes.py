from Student import *

# review on Methods

def sayLotsOfStuff():
    print("Lots of")
    print("stuff")

def cubeIt( num ):
    return num * num * num

sayLotsOfStuff()
print(cubeIt(5))

# Abstraction -- details are hidden away

badkid = Student("Freddy", 10, "Science")
print(badkid.getName())
another = Student("Jim", 10, "Computer Science")
print(another.getName())
another.setName("James")
print(another.getName())

def doNothing():
    pass


