note = input("enter your note: ")
with open("01_python/Day14/notes.txt","a")as file:
               file.write(note + "\n")
               print("Note saved successfully.")