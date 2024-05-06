import os

class BANK:
    def __init__(self) -> None:
        self.USER_PIN = 5678
        self.INITIAL_BALANCE = 2302
        self.CURRENT_BALANCE = self.INITIAL_BALANCE
        self.Login_Attempts = 0

    def Login(self):
        status = False
        while True:
            self.Clear_Screen()
            print(f"\n\t\t{'#'*50}")
            print("\t\t\tBank Account Manager - Login")
            print(f"\t\t{'#'*50}\n")

            pin = int(input("\t\tEnter your PIN: "))
            if pin == self.USER_PIN: 
                status = True
                break
            else: 
                self.Login_Attempts += 1
                if self.Login_Attempts >= 3:
                    print("\t\tYour account has been blocked.\n\n")
                    break
                print("\t\tIncorrect PIN. Please try again.")
                input("")

        return status


    # Function to change the user's pin
    def CHANGE_PIN(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}")
        print("\t\t\tAccount Settings - Change Pin")
        print(f"\t\t{'#'*50}\n")

        new_pin = input("\t\tEnter new PIN: ")
        self.USER_PIN = int(new_pin)
        print("\t\tPIN changed successfully.")
        print("\n\t\tPress Any KEY To SHOW MENU...")
        input("")

    def DEPOSIT(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}")
        print("\t\t\t\tDeposit Account Balance")
        print(f"\t\t{'#'*50}\n")
        print(f"\t\t--BALANCE: {self.CURRENT_BALANCE}\n")

        amount = float(input("\t\tEnter amount to deposit: "))
        self.CURRENT_BALANCE += amount
        print(f"\t\tDeposit of KD {amount} successful. Current Balance: {self.CURRENT_BALANCE}")
        print("\n\t\tPress Any KEY To SHOW MENU...")
        input("")
    
    def CASH_WITHDRAW(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}")
        print("\t\t\t\tWithdraw Account Balance")
        print(f"\t\t{'#'*50}\n")
        print(f"\t\t--BALANCE: {self.CURRENT_BALANCE}\n")

        withdraw_amount = float(input("\t\tEnter amount to withdraw: "))
        if withdraw_amount > 1000:
            print("\t\tWithdrawal amount exceeds maximum limit of KD 1000.")
        elif withdraw_amount > self.CURRENT_BALANCE:
            print("\t\tInsufficient balance.")
        else:
            self.CURRENT_BALANCE -= withdraw_amount
            print(f"\t\tWithdrawal of KD {withdraw_amount} successful.")

        print("\n\t\tPress Any KEY To SHOW MENU...")
        input("")

    def QUICK_WITHDRAW(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}")
        print("\t\t\t\tWithdraw Account Balance")
        print(f"\t\t{'#'*50}\n")
        print(f"\t\t--BALANCE: {self.CURRENT_BALANCE}\n")

        print("\t\ta: K.D. 50")
        print("\t\tb: K.D. 100")
        print("\t\tc: K.D. 250")
        print("\t\td: K.D. 500")
        choice = input("\n\t\tEnter your choice: ")

        selected_Amount = 0
        if choice == 'a':  
            selected_Amount = 50

        elif choice == 'b': 
            selected_Amount = 100

        elif choice == 'c': 
            selected_Amount = 250

        elif choice == 'd': 
            selected_Amount = 500

        else: print("\t\tInvalid choice.")

        if selected_Amount>0:
            if self.CURRENT_BALANCE>selected_Amount:
                self.CURRENT_BALANCE -= selected_Amount
                print(f"\t\tWithdrawal of KD {selected_Amount} successful.")
            else:
                print("\t\tInsufficient balance.")

        print("\n\t\tPress Any KEY To SHOW MENU...")
        input("")
    
    def BALANCE(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}")
        print("\t\t\t Current Account Balance")
        print(f"\t\t{'#'*50}\n")
        print(f"\n\t\tCurrent Balance: KD {self.CURRENT_BALANCE}")
        print("\n\t\tPress Any KEY To SHOW MENU...")
        input("")
        
    # Function to display the menu
    def MENU(self):
        self.Clear_Screen()
        print(f"\n\t\t{'#'*50}\n")
        print("\t\tWelcome To Bank Account Manager")
        print("\t\tThis Program Help You Manage Your Account Balance!\n")
        print("\t\t0. Display Menu")
        print("\t\t1. Change PIN")
        print("\t\t2. Cash Deposit")
        print("\t\t3. Quick Withdraw")
        print("\t\t4. Cash Withdraw")
        print("\t\t5. Display Balance")
        print("\t\t99. Exit")

    def Clear_Screen(self):
        os.system("cls")


# Main program
def main():
    bank = BANK()
    while True:
        if bank.Login():
            while True:
                bank.MENU()
                choice = input("\n\t\tEnter your choice: ")
                print(f"\n\t\t{'#'*40}")
                if choice == '1': bank.CHANGE_PIN()
                elif choice == '2': bank.DEPOSIT()
                elif choice == '3': bank.QUICK_WITHDRAW()
                elif choice == '4': bank.CASH_WITHDRAW()
                elif choice == '5': bank.BALANCE()
                elif choice == '0': bank.MENU()
                elif choice == '99': break
                else: 
                    print("\t\tInvalid choice.")
                    input("")
        else: break
        break

if __name__ == "__main__":
    main()
