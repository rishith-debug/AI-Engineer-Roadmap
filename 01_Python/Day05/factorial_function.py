def fact():
               x =int(input("Enter the number"))
               fact_num = 1
               for i in range(1,x+1):
                              fact_num = fact_num * i
                              print(fact_num)
fact()