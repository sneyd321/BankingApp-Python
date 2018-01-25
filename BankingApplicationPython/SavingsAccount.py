from Account import *
class SavingsAccount(Account):
    """Savings Account"""
    

   
    
    def deposit(self, amount):
        """Override deposit so when user deposits half the amount goes into the savings account"""
        self._balance += amount/2
