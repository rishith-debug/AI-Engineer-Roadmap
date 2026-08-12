SetA =  {10, 20, 30, 40}
SetB =  {30, 40, 50, 60}
numbers = SetA|SetB
print("The union of the numbers are:",numbers)
numbers = SetA&SetB
print("The intersection of the numbers are:",numbers)
numbers = SetA - SetB
print("The difference of the numbers are:",numbers)
numbers = SetA ^ SetB
print("The symmetric difference of the numbers are:",numbers)