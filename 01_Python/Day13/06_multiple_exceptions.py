try:
               result = 10/0
except ZeroDivisionError:
               print("cannot divide with zero")
except TypeError:
               print("type error")
else:
               print("Division successfull")
finally:
               print("program finished")