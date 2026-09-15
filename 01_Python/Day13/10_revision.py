try:
               num = int(input("Enter a number: "))
               if num < 0 :
                            raise ValueError("Number is negative")
except ValueError as e:
               print("Invalid number",e)
else:
               print("valid number")
finally:
               print("Program finished")
               
