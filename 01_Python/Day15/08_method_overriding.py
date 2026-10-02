class Student():
               def __init__(self,name,age):
                              self.name = name
                              self.age = age
               def introduce(self):
                              print("my name is",self.name)
                              print("my age is ",self.age)
class CollegeStudent(Student):
               def introduce(self):
                              print(" hi my name is",self.name)
                              print("hello my age is",self.age)
student1 = CollegeStudent("rishii",20)
student2 = Student("roxy",21)
student1.introduce()
student2.introduce()
                              