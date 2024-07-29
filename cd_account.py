"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, 0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest = cd_account.calculate_earned_interest(months, interest_rate)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = cd_account.update_balance_with_interest(interest)
    

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(interest)

    # Return the updated balance and interest earned.
    return  f"Updated balance: {cd_account.balance: .2f}, Interest earned: {cd_account.interest: .2f}"

# Test the function
if __name__ == "__main__":
    print(create_cd_account(1000, 5, 12))  # Expected output: Updated balance: 1050.0, Interest earned: 50.0
    print(create_cd_account(2000, 3, 6))  # Expected output: Updated balance: 2030.0, Interest earned: 30.0
    print(create_cd_account(5000, 8, 24))  # Expected output: Updated balance: 5400.0, Interest earned: 400.0
    print(create_cd_account(10000, 10, 36))  # Expected output: Updated balance: 13000.0, Interest earned: 3000.0
