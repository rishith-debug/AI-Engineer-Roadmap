password = (input("Enter the password: "))

uppercase = False
lowercase = False
digit = False

special_char = "!@#$%^&*_[]()|:;.,"

for ch in password:
               if ch.isupper():
                              upper = True
               elif ch.islower():
                              Lower = True
               elif ch.isdigit:
                              digit = True
if len(password) >= 8 and upper and Lower and digit and special_char:
               print("Strong password")
else:
               print("Weak password")

               
               if len(password)< 8:
                              print("password should contain 8 charecters")
               if not upper:
                              print("At least one uppercase letter")
               if not Lower:
                              print("Atleast one lower letter")
               if not digit:
                              print("Atleast one digit")
               if not special_char:
                              print("At least one special_char")
               