""" 
def rev(text):
               reverse_str = ""
               for ch in text:
                              reverse_str = ch + reverse_str
               return reverse_str
name = input("Enter your name: ")
print(rev(name))
""" 

def palindrome(string):
               name = string.lower()
               reverse_str = ""
               
               for ch in name:
                              reverse_str = ch + reverse_str
               if name == reverse_str:
                              return "palindrome"
               else:
                              return "Not a palindrome"
name = input("Enter the name: ")
print(palindrome(name))
                              
