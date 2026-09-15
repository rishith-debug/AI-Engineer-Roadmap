marks = int(input("Enter the marks: "))
if marks < 0 or marks > 100:
               raise ValueError("marks are not valid")
else:
               print("marks are valid")