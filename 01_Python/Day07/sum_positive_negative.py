numbers = [12, -5, 8, -10, 15, -3, 20]
negative = 0
positive = 0
for i in numbers:
               if  i>0:
                              positive +=i
               elif i<0:
                              negative +=i
print("Positve sum =",positive)
print("Negative sum =",negative)