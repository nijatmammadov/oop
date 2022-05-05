from E_Commerce_system.Products.Electronic_devices import electronic_devices
class charger(electronic_devices):
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, compatible_devices, connectivity_technology,
                 wattage):
        super(charger, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__compatible_devices = compatible_devices
        self.__connectivity_technology = connectivity_technology
        self.__wattage = wattage

    def get_compatible_devices(self):
        return self.__compatible_devices
    def set_compatible_devices(self, compatible_devices):
        self.__compatible_devices = compatible_devices

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_wattage(self):
        return self.__wattage
    def set_wattage(self, wattage):
        self.__wattage = wattage