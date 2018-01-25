from Account import *
from ChequingAccount import *
from SavingsAccount import *
class Bank():
    """Class that holds account information and creates accounts"""
    #list that holds all bank information
    _accountList = []
    
    def __init__(self):
        #Create 10 default accounts when initalized
        for i in range(0, 9):
            #Create account demo account object
            account = Account(100 + i, "Demo Account #" + str(i))
            #initalze default interest
            account.setAnnualIntrRate(0.1)
            #initialize default amount
            account.deposit(100)
            #add account to account list
            self._accountList.append(account)

    def openAccount(self, acctNo, clientName, balance, acctType, intrRate):
        """Creates account"""
       
        #Check which type of account was chosen
        #if checking account
        if acctType == "c" or acctType == "C":
            #create chequing account
            account = ChequingAccount(acctNo, clientName)
            #set annual interest rate
            account.setAnnualIntrRate(intrRate)
            #set balance 
            account.deposit(balance)
            #add account to account list
            self._accountList.append(account)
        #if saving account
        else:
            #Create saving account
            account = SavingsAccount(acctNo, clientName)
            #set annual interest rate
            account.setAnnualIntrRate(intrRate)
            #set balance
            account.deposit(balance)
            #add account to account list
            self._accountList.append(account)
                
       


    def getAccount(self, acctNo):
        """looks if account is available and returns account if no account is found return None"""
        for account in self._accountList:
            if account.getAccountNumber() == acctNo:
                return account
        return None

