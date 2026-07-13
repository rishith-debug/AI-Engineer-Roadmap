Num1 = float(input("Enter the number1: "))
operator = input("operator(+,-,*,/):")
Num2 = float(input("Enter the number2: "))

if operator == "+":
               result = Num1 + Num2
               print(f"Result: {Num1} + {Num2} = {result}")
elif operator == "-":
               result = Num1 - Num2
               print(f"Result: {Num1} - {Num2} = {result}")
elif operator == "*":
               result = Num1 * Num2
               print(f"Result: {Num1} * {Num2} = {result}")
elif operator == "/":
               if Num2 == 0:
                              print("Error . it cant be divided by 0")
else: 
               result = Num1 / Num2
               print(f"Result: {Num1} / {Num2} = {result}")
               
                
               
               
               
