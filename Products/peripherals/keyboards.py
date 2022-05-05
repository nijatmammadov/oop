from E_Commerce_system.Products.Electronic_devices import electronic_devices
class keyboard(electronic_devices):
    def __init__(self,product_code, product_count, price, Brand, color, weight, warranty, keyboard_description,
                 connectivity_technology, special_feature, series, number_of_keyboards):
        super(keyboard, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__keyboard_description = keyboard_description
        self.__connectivity_technology = connectivity_technology
        self.__special_feature = special_feature
        self.__series = series
        self.__number_of_keyboards = number_of_keyboards

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\n" \
               f"Price: {self.get_price()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\nWeight: {self.get_weight()}\n" \
               f"Wrranty: {self.get_warranty()}\nKeyboard description: {self.__keyboard_description}\nConnectivity technology: {self.__connectivity_technology}" \
               f"Special Feature: {self.__special_feature}\nSeries: {self.__series}\nNumber of keyboards: {self.__number_of_keyboards}"

    def get_keyboard_description(self):
        return self.__keyboard_description
    def set_keyboard_description(self, keyboard_description):
        self.__keyboard_description = keyboard_description

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_special_feature(self):
        return self.__special_feature
    def set_special_feature(self, special_feature):
        self.__special_feature = special_feature

    def get_series(self):
        return self.__series
    def set_series(self, series):
        self.__series = series

    def get_number_of_keyboards(self):
        return self.__number_of_keyboards
    def set_number_of_keyboards(self, number_of_keyboards):
        self.__number_of_keyboards = number_of_keyboards
