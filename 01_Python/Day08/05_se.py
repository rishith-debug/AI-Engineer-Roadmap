numbers = int(input("enter the number: "))
num = [10,20,30,40,50]
Found = False
for i in num:
               if i == numbers:
                 Found  = True
if Found:
               print("Element is found")
else:
               print("Element not found")
               