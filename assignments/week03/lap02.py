# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "4":
            break

        if choice == "3":
            deposit = float(input("Deposit amount:"))
            if deposit < 0 :
                print("CANNOT DEPOSIT REST THAN 0")
            else:    
             balance = balance + deposit
            print("Successfully,Your balance now = ", balance)

        if choice == "2":
            withdraw = float(input("Withdraw amount: "))
            if withdraw < 0 or withdraw > balance :
                print("CANNOT WITH DRAW LESS THAN 0 ")
                continue
            else:
             balance = balance - withdraw
            print("Successfully.Your balance now =",balance)

        if choice == "1":
            print("Your balance now = ",balance)        
        else:
            continue    
else:
    print("Invalid PIN")




