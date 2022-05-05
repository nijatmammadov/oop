from E_Commerce_system.Products.Electronic_devices import electronic_devices
class Mouse(electronic_devices):
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, connectivity_technology, movement):
        super(Mouse, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__connectivity_technology = connectivity_technology
        self.__movement = movement

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
               f"Weight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nConnectivity Technology: {self.__connectivity_technology}\n" \
               f"Movement: {self.__movement}"

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_movement(self):
        return self.__movement
    def set_movement(self, movement):
        self.__movement = movement