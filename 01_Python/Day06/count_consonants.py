def count_consonants():
               x = input("Enter the word: ")
               vowels = "aeiou"
               count_consonants = 0
               name_2 = x.lower()
               for char in name_2:
                              if char.isalpha() and char not in vowels:
                                             count_consonants += 1
                              print(f"The consonants in word is{count_consonants}")
count_consonants()
               