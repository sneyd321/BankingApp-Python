class Account():
    """Holds user account information"""
    #Initialize field variables
    _acctHolderName = ""
    _acctNo = 0
    _annualIntrRate = 0.0
    _balance = 0.0

    def __init__(self, acctNo, acctHolderName):
        self._acctHolderName = acctHolderName
        self._acctNo = acctNo

    def getAccountHolderName(self):
        """return account holder name"""
        return self._acctHolderName

    def getAccountNumber(self):
        """return account number"""
        return self._acctNo

    def getAnnualIntrRate(self):
        """return interest rate"""
        return self._annualIntrRate

    def setAnnualIntrRate(self, newIntRate):
        """set the value of the interest rate"""
        self._annualIntrRate = newIntRate

    def getBalance(self):
        """return the current balance of the user"""
        return self._balance

    def deposit(self, amount):
        """deposit money into account"""
        self._balance += amount

    def withdraw(self, amount):
        """withdraw maney from account"""
        if amount > self._balance:
            self._balance -= amount

    def predictBalance(self, balance):
        """predict furture balance"""
        interest = (balance * self._annualIntrRate)/12
        return interest
