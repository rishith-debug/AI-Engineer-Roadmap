name = str(input("Enter your name: "))
sub1 = int(input("Enter your CSA marks: "))
sub2 = int(input("Enter your ATCD marks: "))
sub3 = int(input("Enter your DM marks: "))
sub4 = int(input("Enter your IAI marks: "))
sub5 = int(input("Enter your DBMS marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
print("The total is : ",+total)
average = (sub1 + sub2 + sub3 + sub4 + sub5)/5
print("the average is :",+average)
if total >= 450 :
               print("Grade is A")
elif 200 <= total <= 449:
               print("Grade is B ")
elif 100 <= total <= 199:
               print("Grade is C ")
elif 0 <= total <= 99:
               print("Grade is D ")
if total<=50 :
               print("Fail")
else :
               print("Pass")

