def calculator():
               x = int(input("Enter the x value: "))
               y = int(input("Enter the y value: "))
               op= input("Enter the operators(+,-,*,/)")
               if op == "+":
                              result = x + y
                              print(f"{result}")
               elif op == "-":
                              result = x - y
                              print(f"{result}")
               elif op == "*":
                              result = x * y
                              print(f"{result}")
               elif op == "/":
                              if y!=0:
                                             result = x/y
                                             print(f"{result}") 
                              else :
                                             print("ERROR in division")
               else:
                              print("Invalid operator! Please choose +, -, *, or /")   
                                             
                              
calculator()                          
               
               