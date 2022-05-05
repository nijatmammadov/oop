from E_Commerce_system.Products.Electronic_devices import electronic_devices
class stylus(electronic_devices):
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, number_of_batteries, compatible_devices, charging_time):
        super(stylus, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__number_of_batteries = number_of_batteries
        self.__compatible_devices = compatible_devices
        self.__charging_time = charging_time

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
               f"Weight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nNumber Of Batteries: {self.__number_of_batteries}\nCompatible Devices: " \
               f"{self.__compatible_devices}\nCharging Time: {self.__charging_time}"

    def get_number_of_batteries(self):
        return self.__number_of_batteries
    def set_number_of_batteries(self, number_of_batteries):
        self.__number_of_batteries = number_of_batteries

    def get_compatible_devices(self):
        return self.__compatible_devices
    def set_compatible_devices(self, compatible_devices):
        self.__compatible_devices = compatible_devices

    def get_charging_time(self):
        return self.__charging_time
    def set_charging_time(self, charging_time):
        self.__charging_time = charging_time