class Student:
	college = "VJIT"
	def __init__(self,name,age):
                self.name = name
                self.age = age
	def introduce(self):
                print("my name is",self.name)
                print("and i'm from",self.college)
Student1 = Student("rishi",20)
Student2 = Student("roxy",21)
Student1.introduce()
Student2.introduce()