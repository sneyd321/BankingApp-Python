from Account import *

class ChequingAccount(Account):
    """Chequing Account"""

    

    def withdraw(self, amount):
        """Override withdraw to allow an overdraft of $500"""
        #if amount is less than the overdraft limit
        if amount < self._balance + 500:
            #withraw amount
            self._balance -= amount

    

