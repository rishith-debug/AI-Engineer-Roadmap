name = input("Enter your name: ")
reverse_name = ""
name = name.lower()
for i in name:
               reverse_name = i + reverse_name 
if reverse_name == name :
                              print("IT is a palindrome")
else:
               print("Not a palindrome")