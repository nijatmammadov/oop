from E_Commerce_system.Products.Product import product
class electronic_devices(product):
    """
        This class is the main class of all electronic devices in the store. And it retains all their common features.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty):
        super(electronic_devices, self).__init__(product_code, product_count,price)
        self.__Brand = Brand
        self.__color = color
        self.__weight = weight
        self.__warranty = warranty
        self.__turn_on = False
    def Turn_on(self):
        if self.__turn_on == True:
            print("Device is already turned on")
        else:
            self.__turn_on = True
    def Shut_down(self):
        if self.__turn_on==False:
            print("Device is already shutted down")
        else:
            self.__turn_on = False

    def get_Brand(self):
        return self.__Brand
    def set_Brand(self, Brand):
        self.__Brand = Brand

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight

    def get_warranty(self):
        return self.__warranty
    def set_warranty(self, warranty):
        self.__warranty = warranty

    def get_turn_on(self):
        return self.__turn_on
    def set_turn_on(self, turn_on):
        self.__turn_on = turn_on
