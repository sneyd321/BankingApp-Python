from Bank import *
class AtmApplication():
    """ Class that handels user input """
    #initalize field variables
    _bank = Bank()
    _acctNo = 0
    _ivalidInput = "Invalid Input. Please enter a valid number\n"

    def __init__(self):
        #here for python convention
        pass

    def run(self):
        """starts the ATM"""
        while True:
            print("Main Menu\n")
            print("1: Select Account")
            print("2: Create Account")
            print("3: Exit\n")
            try:
                choice = int(input("Enter a choice: "))          
                if choice == 1:
                    self.onSelectAccount()
                elif choice == 2:
                    self.onCreateAccount()
                elif choice == 3:
                    break
                else: 
                    print("Please enter a valid number.\nEnter 1 to select an account.\nEnter 2 to create an account.\nEnter 3 to exit.\n")
                    continue
            except ValueError:
                print("Invalid Input. Please enter a valid number\n")


    def onCreateAccount(self):
        """When Create Account is selected"""
        while True:
            try:
                clientName = input("Please enter the client name or press [ENTER] to cancel: ")
                if clientName == "":
                    break
                balanceInput = input("Please enter your intial balance or press [ENTER] to cancel: ")
                if balanceInput == "":
                    break
                elif int(balanceInput) < 0:
                    print("Please enter a number grater than 0\n")
                    continue
                else:
                    balance = int(balanceInput)
                accountType = input("Please enter the account type [c/s: chequing / savings]: ")
                if accountType == "":
                    break
                elif len(accountType) > 1:
                    print("Please enter a [c or s] to select an account\n") 
                    continue
                elif ord(accountType) != 67 and ord(accountType) != 99 and ord(accountType) != 83 and ord(accountType) != 115:
                    print("Please enter a [c or s] to select an account\n") 
                    continue
                if ord(accountType) == 67 or ord(accountType) == 99:

                    interRateInput = float(input("Please enter the interest rate for this account: "))
                    if interRateInput == "":
                        break
                    elif float(interRateInput) < 0:
                        print("Please enter a number greater than 0\n")
                        continue
                    elif float(interRateInput) > 1:
                        print("Please enter a number less than 1\n") 
                        continue
                    else:
                        interRate = float(interRateInput)
                elif ord(accountType) == 83 or ord(accountType) == 115:
                    interRateInput = float(input("Please enter the interest rate for this account: "))
                    if interRateInput == "":
                        break
                    elif float(interRateInput) < 3:
                        print("Please enter a number greater than 3\n")
                        continue
                    else:
                        interRate = float(interRateInput)

                acctNoInput = int(input("Please enter the account number [100 - 1000] or press [ENTER] to cancel: "))
                if acctNoInput == "":
                    break
                elif int(acctNoInput) < 100 or int(acctNoInput) > 1000:
                    print("Please enter a value a number between [100 - 1000]\n")
                    continue
                else:
                    acctNo = int(acctNoInput)

                if self._bank.getAccount(acctNo) != None:
                    print("Account number already exists")
                    continue
                else:
                    self._bank.openAccount(acctNo, clientName, balance, accountType, interRate)
                    break
            except ValueError:
                print("Invalid Input. Please enter a valid input\n")

    def onSelectAccount(self):
        """When select account is created"""
        while True:
            try:
                if self._acctNo == 0:
                    acctNo = input("Please enter your account ID or press [ENTER] to cancel: ")
            
                    if acctNo == "":
                        break
                    else:
                        self._acctNo = int(acctNo)
                    if self._bank.getAccount(self._acctNo) == None:
                        print("ID not found!\n")
                        self._acctNo = 0
                        return                                     
                else:
                    print("Account Menu\n")
                    print("1: Check Balance")
                    print("2: Withdraw")
                    print("3: Deposit")
                    print("4: Predict Balance")
                    print("5: Exit\n")
                
                    choice = int(input("Enter a choice: "))
        
                    if choice == 1:
                        self.onCheckBalance()
                    elif choice == 2:
                        self.onWithdraw()
                    elif choice == 3:
                        self.onDeposit()
                    elif choice == 4:
                        self.onPredictBalance()
                    elif choice == 5:
                        self._acctNo = 0;
                        break
                    else: 
                        print("Please enter a valid number.\nEnter 1 to chack balance.\nEnter 2 to withdraw from account.\nEnter 3 to deposit into account.\nEnter 4 to predict balance.\nEnter 5 to exit.\n")
                        continue
            except ValueError:
                print("Invalid Input. Please enter a valid number\n")
            

    def onCheckBalance(self):
        """When check balance is selected"""
        account = self._bank.getAccount(self._acctNo)
        print("Current balance: " + str(account.getBalance()))
        return

    def onDeposit(self):
        """When deposit is selected"""
        account = self._bank.getAccount(self._acctNo)
        amount = int(input("How much money would you like to deposit: "))
        account.deposit(amount)
        print("New balance is: " + str(account.getBalance()))
        return

    def onWithdraw(self):
        """When withdraw is selected"""
        account = self._bank.getAccount(self._acctNo)
        amount = int(input("How much money would you like to withdraw: "))
        if amount > account.getBalance():
            print("Insufficent funds!")
            return
        else:
            account.withdraw(amount)
            print("New balance is: " + str(account.getBalance()))
            return

    def onPredictBalance(self):
        """when predict balancce is selected"""
        while True:
            try:
                monthlyDeposit = int(input("Please enter a monthly deposit: "))
                if monthlyDeposit < 0:
                    print("Please enter a valid amount")
                    continue
                monthlyWithdrawl = int(input("Please enter a monthly withdrawl: "))
                if monthlyWithdrawl < 0:
                    print("Please enter a valid amount")
                    continue
            
                account = self._bank.getAccount(self._acctNo)
                print("Account Number: " + str(account.getAccountNumber()))
                print("Name: \t\t" + account.getAccountHolderName())
                balance = account.getBalance()
                newInterest = 0.0
                #for 12 months
                for i in range(0, 12):
                    balance = balance + monthlyDeposit - monthlyWithdrawl
                    interst = account.predictBalance(balance)
                    newInterest += interst
                    print("Month " + str(i + 1) + ":")
                    print("\tBalance: " + str(round(balance, 2)))
                    print("\tInterest: " + str(round(newInterest, 2)))
                print("End of the Year Balance: " + str(round((newInterest + balance), 2)))
                break
            except ValueError:
                print("Invalid Input. Please enter a valid number\n")

        
    
    

