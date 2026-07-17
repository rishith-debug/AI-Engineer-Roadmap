def vowels():
               v = input("Enter the word: ")
               vowels = "aeiou"
               name = v.lower()
               vowels_count = 0
               for char in name:
                              if char in vowels:
                                             vowels_count += 1
                                             print(f"The vowels in given word {vowels_count}")
vowels()               
               
               
               
                              