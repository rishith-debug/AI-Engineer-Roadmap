class Student:
               def __init__(self,name,age):
                              self.name = name
                              self.age = age
               def introduce(self):
                              print("my name is",self.name)
                              print("and my age is",self.age)
class collegeStudent(Student):
               pass
student1 = collegeStudent("rishii",20)
student2 = collegeStudent("roxy",21)
student1.introduce()
student2.introduce()


               