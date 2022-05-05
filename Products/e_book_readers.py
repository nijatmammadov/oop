from E_Commerce_system.Products.Electronic_devices import electronic_devices
class E_book_reader(electronic_devices):
    """
        This class retains the features of e-book readers.
    """
    def __init__(self, product_code, product_count, price, Brand, color, size, weight, on_device_storage, Battery_life, warranty):
        super(E_book_reader, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__on_device_storage=on_device_storage
        self.__Battery_life=Battery_life
        self.__size=size
    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\n" \
               f"Price: {self.get_price()}\nBrand: {self.get_Brand()}\n" \
               f"Color: {self.get_color()}\nSize: {self.__size}\nWeight: {self.get_weight()}\n" \
               f"Wrranty: {self.get_warranty()}\nBattery Life: {self.__Battery_life}\nSize: {self.__size}"

    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size = size

    def get_on_device_storage(self):
        return self.__on_device_storage
    def set_on_device_storage(self, on_device_storage):
        self.__on_device_storage = on_device_storage

    def get_Battery_life(self):
        return self.__Battery_life
    def set_Battery_life(self, Battery_life):
        self.__Battery_life=Battery_life
