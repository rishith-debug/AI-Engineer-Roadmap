class Student:
               college = "Vjit"
               def __init__(self,name,age):
                              self.name = name
                              self.age = age
               def introduce(self):
                              print("my name is ",self.name)
                              print("my age is",self.age)
					
class collegeStudent(Student):
               def introduce(self):
                              print("hello my name is ",self.name)
                              print("I'm from",self.college)
student1 = Student("rishii", 20)
student2 = collegeStudent("roxy", 21)
student1.introduce()
student2.introduce()

