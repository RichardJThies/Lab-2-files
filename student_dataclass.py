#Part 3
from dataclasses import dataclass

@dataclass#annotation

class Student:#function inside a class is a method, outside methods are just functions
    name: str
    schoolID: str
    gpa: float

def main():#would you use a dictonary to hold new students if you were adding them?
    newStudentInfo = Student(newStudentName, newStudentID, newStudentGPA)
    
    print('Please enter information about new student. Hit enter to quit.')
    newStudentName = input('New name? ')
    newStudentID = input('New ID? ')
    newStudentGPA = input('New GPA? ')
    while True:
        if newStudentName or newStudentID or newStudentGPA == '':
            break
    print(newStudentInfo)

if __name__ == '__main__':#this construction is for when files are importing code from other files, all could will run by default, this stops that from occuring
    main()









