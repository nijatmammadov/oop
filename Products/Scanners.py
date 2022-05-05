from E_Commerce_system.Products.Electronic_devices import electronic_devices
class scanner(electronic_devices):
    """
        This class retains the features of Scanners.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, media_type, scanner_type, model_name,
                 connectivity_technology, resolution, wattage):
        super(scanner, self).__init__( product_code, product_count, price, Brand, color, weight, warranty)
        self.__media_type = media_type
        self.__scanner_type = scanner_type
        self.__model_name = model_name
        self.__connectivity_technology = connectivity_technology
        self.__resolution = resolution
        self.__wattage = wattage

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\n" \
               f"Color: {self.get_color()}\nWeight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nPrice: {self.get_price()}\n" \
               f"Media Type: {self.__media_type}\nScanner Type: {self.__scanner_type}\nModel Name: {self.__model_name}\nConnectivity Technology: " \
               f"{self.__connectivity_technology}\nResulation: {self.__resolution}\nWattage: {self.__wattage}"

    def get_media_type(self):
        return self.__media_type
    def set_media_type(self, media_type):
        self.__media_type = media_type

    def get_scanner_type(self):
        return self.__scanner_type
    def set_scanner_type(self, scanner_type):
        self.scanner_type = scanner_type

    def get_model_name(self):
        return self.__model_name
    def set_model_name(self, model_name):
        self.__model_name = model_name

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_resolution(self):
        return self.__resolution
    def set_resolution(self, resolution):
        self.__resolution = resolution

    def get_wattage(self):
        return self.__wattage
    def set_wattage(self, wattage):
        self.__wattage = wattage



