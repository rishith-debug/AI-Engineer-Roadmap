print("Welcome to SBI ATM ")
balance = 8000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
               print("your balance is ",+balance)
elif choice == 2:
               deposit = float(input("Enter deposit amount :"))
               Balance = deposit + balance
               print(" your Balance is :",+Balance)
elif choice == 3:
               withdraw = float(input("Enter the amount:"))
               Balance = withdraw - balance
               print("your balance is :",+Balance)
elif choice == 4:
               print("Thank you") 
               
               
