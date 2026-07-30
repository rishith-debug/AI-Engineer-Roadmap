numbers = [20,30,40,50,60,70]
largest = numbers[0]
second_largest = numbers[0]
for i in numbers:
               if i > largest:
                              second_largest = largest 
                              largest = i
               elif i > second_largest and i!= largest:
                              second_largest = i
print("The second_largest is",second_largest)