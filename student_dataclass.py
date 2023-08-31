#Part 3
from dataclasses import dataclass

@dataclass#annotation

class Student:#function inside a class is a method, outside methods are just functions
    name: str
    schoolID: str
    gpa: float

def main():#would you use a dictonary to hold new students if you were adding them?
    tim = Student('tim', '12345', '3.1')#P
    print(tim.name)
    print(tim.schoolID)
    print(tim.gpa)
    print(tim)#Python has still generated a __init__ and __str__ method in the background

    sarah = Student('sarah', '25642yr', '3.3')
    print(sarah.name)
    print(sarah.schoolID)
    print(sarah.gpa)
    print(sarah)#to customize this generated __init__ and __str__ methods, look into the python documentation

    jake = Student('jake', 'dgj5463', '3.0')
    print(jake.name)
    print(jake.schoolID)
    print(jake.gpa)
    print(jake)

if __name__ == '__main__':#this construction is for when files are importing code from other files, all could will run by default, this stops that from occuring
    main()









