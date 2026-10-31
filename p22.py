
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Rahul", 75)
student2 = Student("Aman", 32)

student1.display()
student1.check_result()

student2.display()
student2.check_result()
