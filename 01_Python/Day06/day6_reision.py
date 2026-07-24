""" 
def rev(text):
               reverse_str = ""
               for ch in text:
                              reverse_str = ch + reverse_str
               return reverse_str
name = input("Enter your name: ")
print(rev(name))
""" 
 
"""
name = input("Enter the word: ")
vowels = "aeiou"
count_vowels = 0
for ch in name.lower():
               if ch in vowels:
                              count_vowels += 1
print(f"number of vowels = {count_vowels}")
"""

"""
name = (input("Enter the name: "))
count_uppercase = 0
count_lowercase = 0
count_digits = 0
count_special_char = 0
special_char = "!@#$%^&*(){}[]_+=-|"

for ch in name :
               if ch.isupper():
                              count_uppercase += 1
               elif ch.islower():
                              count_lowercase += 1
               elif ch.isdigit():
                              count_digits += 1
               else :
                              count_special_char += 1
print(f"uppercase :{count_uppercase}")
print(f"lowercase :{count_lowercase}")
print(f"digit :{count_digits}")
print(f"special :{count_special_char}")
"""

def palindrome(string):
               reverse_str = ""
               clean_string = string.lower()
               
               for ch in clean_string:
                              reverse_str = ch + reverse_str
               if reverse_str == clean_string:
                              return "the word is palindrome"
               else:
                              return "The word is not a palindrome"
name = input("Enter the name: ")
print(palindrome(name))
               

