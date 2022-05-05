from datetime import datetime
class product:
    """
        This class is the mother class of all products in the store. And it retains all their common features.
    """
    def __init__(self, product_code, product_count, price):
        self.__product_code = product_code
        self.__product_count = product_count
        self.__price = price

    def __eq__(self, other):
        if other.product_count>self.__product_count:
            return other.product_count

    def get_product_code(self):
        return self.__product_code

    def set_product_code(self, product_code):
        self.__product_code=product_code

    def get_product_count(self):
        return self.__product_count

    def set_product_count(self, product_count):
        self.__product_count = product_count

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


