class UserData:
    def __init__(self):
        self.data = self.read_data()
    def read_data(self):
        import json
        try:
            with open("data/data.json", "r") as f:
                self.data = json.load(f)
                return self.data
        except FileNotFoundError:
            self.data = {}
            return self.data

class Atm:
    # constructor  
    def __init__(self):
         self.pin = ""
         self.balance = 0
         self.user_data = UserData()
         self.menu()

    def menu(self):
        user_input = input("""
        Welcome to the ATM Machine
        PRESS
        1. Enter 1 to Create Pin
        2. Enter 2 to Deposit Money
        3. Enter 3 to Withdraw Money
        4. Enter 4 to Check Balance
        5. Enter 5 to Exit
         
       """)
        if user_input == "1":
            print("seleted Create Pin")
            if self.create_pin(self.user_data):
                print("Pin creation successful")
            else:
                print("Pin creation failed")
                
        elif user_input == "2":
            print("seleted Deposit Money")
            if self.deposit_money():
                print("Deposit successful")
            else:
                print("Deposit failed")
        
        
        elif user_input == "3":
            print("seleted Withdraw Money")
        elif user_input == "4":
            print("seleted Check Money")
        elif user_input == "5":
            print("seleted Exit")
        else:
            print("Presses wrong button")
            
    
    def create_pin(self, user_data):
    
        acc_max_try = 3
        pin_max_try = 3
        print("You are a new user please enter your account number: ")
        while acc_max_try:
            account_number = input("Enter your account number: ")
            if not self.validate_account_number(account_number, self.user_data):
                print("Entered account number is not valid\n")
                acc_max_try -= 1
                if acc_max_try == 0:
                    print("You have exceeded the maximum number of tries")
                    return False
            else:
                while pin_max_try:
                    pin = input("Please enter your new pin: ")
                    if not self.validate_pin(pin):
                        print("Please create a valid pin")
                        pin_max_try -= 1
                        if pin_max_try == 0:
                            print("You have exceeded the maximum number of tries")
                            return False
                    else:
                        self.user_data.data[account_number] = {'pin': pin, 'balance': 0}
                        self.update_data(self.user_data, account_number=account_number, pin=pin, balance=0)
                        print(self.user_data.data)
                        break
                return True
        
        print("Pin created successfully.")
        print("Your account number is:", account_number)
        print("Your pin is:", self.user_data.data[account_number])
    def validate_account_number(self, account_number, user_data):
        if account_number in user_data.data or len(account_number) < 6:
            return False
        else:
            return True
    def validate_pin(self, pin):
        if len(pin) < 6:
            return False
        else:
            return True
    
    
    def update_pin(self):
        pass
    
    def authenticate_user(self, pasword):
        pass
    
    def deposit_money(self):
        deposit_max_try = 3
        while deposit_max_try:
            account_number = input("Please Enter you Account Number: ")
            pin = input("Please Enter your Pin: ")
            if not (account_number in self.user_data.data and self.user_data.data[account_number]['pin'] == pin):
                print("Invalid credentials try again\n")
                deposit_max_try -= 1
                if deposit_max_try == 0:
                    print("You have exceeded the maximum number of tries")
                    return False
            else:
                money_to_deposit = float(input("Please Enter amount to deposit: "))
                curr_balance = self.user_data.data[account_number]['balance'] or 0
                new_balance = curr_balance + money_to_deposit
                self.user_data.data[account_number]['balance'] = new_balance
                print(f"Deposit successful. New balance is: {new_balance}")
                self.update_data(self.user_data, account_number=account_number, balance=new_balance)
                return True
        return False
            


        pass
    
    def check_balance(self):
        pass
    
    def update_data(self, user_data, account_number=None, pin=None, balance=None):
        import json
        import os
        
        # Load existing data
        existing_data = {}
        if os.path.exists("data/data.json"):
            with open("data/data.json", "r") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    print("Error reading JSON file. Starting with empty data.")
        
        # Update or create the account entry
        if account_number:
            if account_number not in existing_data:
                # Create new entry
                existing_data[account_number] = {'pin': pin or '', 'balance': balance or 0}
            else:
                # Update existing entry
                if pin is not None:
                    existing_data[account_number]['pin'] = pin
                if balance is not None:
                    existing_data[account_number]['balance'] = balance
        
        # Save the updated data back to the file
        with open("data/data.json", "w") as f:
            json.dump(existing_data, f, indent=4)
        
        print("Data updated in data/data.json")