Name = input("Enter your name")
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0
special = "!@#$%^&*(){}[]" 
for ch in Name:
               if ch.isupper():
                              upper_count +=1
               
               elif ch.islower():
                              lower_count +=1
              
               elif ch.isdigit():
                              digit_count +=1
             
               elif ch in special:
                              special_count +=1

print("uppercase: ",upper_count)
print("lowercase: ",lower_count)
print("digits: ",digit_count)
print("special: ",special_count)