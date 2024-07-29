""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest
    
    def calculate_earned_interest(self, months, interest_rate):
        """Calculate the interest earned for the account"""
        return self.balance * (interest_rate/100 * months/12)

    def update_balance_with_interest(self, interest):
        """Update the account balance with interest"""
        self.balance += interest
