class account_in_the_amount:
    """
    This class has a user account amount. When you first open an account, you have $ 2 in your account.
    The money deposited in the account is not refundable.
    """
    def __init__(self):
        self.__amount = 2

    def get_amount(self):
        return self.__amount
    def set_amount(self, amount):
        self.__amount = amount


