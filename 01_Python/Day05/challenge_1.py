def result():
               M = int(input("Enter the student the marks in maths: "))
               S = int(input("Enter the student the marks in science: "))
               A = int(input("Enter the student the marks in Atcd: "))
               total_subjects = 3
               total_marks = M+S+A
               print(f"Total marks are {total_marks}")
               Average_marks = total_marks /total_subjects
               print(f"average marks are{Average_marks}")
               if total_marks >= 250:
                              print("Grade A")
               elif 150 <= total_marks <= 249:
                              print("Grade B")
               elif 0 <= total_marks <= 149:
                              print("Grade C")
result()
               