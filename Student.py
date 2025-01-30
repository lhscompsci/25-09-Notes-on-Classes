# Classes in Python

class Student:
    def __init__(self, name, grade, course):
        self.name = name
        self.grade = grade
        self.course = course

        # "has-a" relationship between class and instance variables

    def setName(self, poo):  # mutators
        self.name = poo

    def getName(self):  # accessors
        return self.name


