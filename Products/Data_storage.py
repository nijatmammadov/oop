from E_Commerce_system.Products.Electronic_devices import electronic_devices
class Data_Storage(electronic_devices):
    """
        This class retains the characteristics of storage devices.
    """
    def __init__(self,  product_code, product_count, price, Brand, color, weight, warranty, digital_storage, series, specific_uses_or_roduct,
                 form_factor, read_speed, write_speed, cache_size, item_weight, hard_disk_description):
        super(Data_Storage, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__digital_storage = digital_storage
        self.__series = series
        self.__specific_uses_for_product = specific_uses_or_roduct
        self.__form_factor = form_factor
        self.__read_speed = read_speed
        self.__write_speed = write_speed
        self.__cache_size = cache_size
        self.__item_weight = item_weight
        self.__hard_disk_description = hard_disk_description

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\n" \
               f"Price: {self.get_price()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\nWeight: {self.get_weight()}\n" \
               f"Wrranty: {self.get_warranty()}\nDigital Storage: {self.__digital_storage}\nSeries: {self.__series}\nSpecific Uses For Product: " \
               f"{self.__specific_uses_for_product}\nForm Factor: {self.__form_factor}\nRead Speed: {self.__read_speed}\nWrite Speed: {self.__write_speed}" \
               f"\nCache Size: {self.__cache_size}\nItem Weight: {self.__item_weight}\nHard Disk Description: {self.__hard_disk_description}"

    def get_digital_storage(self):
        return self.__digital_storage
    def set_digital_storage(self, digital_storage):
        self.__digital_storage = digital_storage

    def get_series(self):
        return self.__series
    def set_series(self, series):
        self.__series = series

    def get_specific_uses_or_product(self):
        return self.__specific_uses_or_product
    def set_specific_uses_or_product(self, specific_uses_or_roduct):
        self.__specific_uses_or_product=specific_uses_or_roduct

    def get_form_factor(self):
        return self.__form_factor
    def set_form_factor(self, form_factor):
        self.__form_factor = form_factor

    def get_read_speed(self):
        return self.__read_speed
    def set_read_speed(self, read_speed):
        self.__read_speed = read_speed

    def get_write_speed(self):
        return self.__write_speed
    def set__write_speed(self, write_speed):
        self.__write_speed =  write_speed

    def get_cache_size(self):
        return self.__cache_size
    def set_cache_size(self, cache_size):
        self.__cache_size = cache_size

    def get_item_weight(self):
        return self.__item_weight
    def set_item_weight(self, item_weight):
        self.__item_weight = item_weight

    def get_hard_disk_description(self):
        return self.__hard_disk_description
    def set_hard_disk_description(self, hard_disk_description):
        self.__hard_disk_description = hard_disk_description
