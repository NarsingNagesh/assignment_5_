
class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber

s = Student()
s.setName(input("enter The Name : "))
s.setRollNumber(int(input("Enter The Roll Number : ")))
print("Name : " , s.getName()) 
print("Roll_No : " , s.getRollNumber()) 