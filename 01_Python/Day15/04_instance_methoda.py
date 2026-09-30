class student:
               def __init__(self,name,age):
                              self.name = name
                              self.age = age
                              
               def introduce(self):
                              print("my name is",self.name)
                              print("and my age is ",self.age)
student1 = student("rishii",20)
student2 = student("roxy",21)
student1.introduce()
student2.introduce()