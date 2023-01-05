


class Student:
    def __init__(self):
        self.name = None
        self.grade = None
        
    def get_name(self):
        self.name = input("What's your name:")
    
    def get_grade(self):
        self.grade = int(input("Enter your grade:"))
    
    def show(self):
        print(f"Your name is: {self.name}")
        print(f"Your grade is: {self.grade}")
        

Tony = Student()
Tony.get_name()
Tony.get_grade()
Tony.show()
    