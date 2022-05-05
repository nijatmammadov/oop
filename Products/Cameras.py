from E_Commerce_system.Products.Electronic_devices import electronic_devices
class cameras(electronic_devices):
    """
    This class retains the features of the cameras.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, indoor_or_outdoor_Usage,
                 connectivity_technologies, Room_type):
        super(cameras, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__indoor_or_outdoor_Usage = indoor_or_outdoor_Usage
        self.__connectivity_technologies = connectivity_technologies
        self.__Room_type = Room_type
    def __str__(self):
        return f"Product Code: {self.get_product_code()}\nProduct Count: {self.get_product_count()}\nPrice: {self.get_price()}\nBrand: {self.get_Brand()}\n" \
               f"Color: {self.get_color()}\nWeight: {self.get_weight()}\nWarranty: {self.get_warranty()}\nIndoor or Outdoor Usage: {self.__indoor_or_outdoor_Usage}" \
               f"Connectivity Technologies: {self.__connectivity_technologies}\nRoom Type: {self.__Room_type}"

    def get_indoor_or_outdoor_Usage(self):
        return self.__indoor_or_outdoor_Usage
    def set_indoor_or_outdoor_Usage(self, indoor_or_outdoor_Usage):
        self.__indoor_or_outdoor_Usage=indoor_or_outdoor_Usage

    def get_connectivity_technologies(self):
        return self.__connectivity_technologies
    def set_connectivity_technologies(self, connectivity_technologies):
        self.__connectivity_technologies=connectivity_technologies

    def get_Room_type(self):
        return self.__Room_type
    def set_Room_type(self, Room_type):
        self.__Room_type=Room_type