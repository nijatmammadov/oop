from E_Commerce_system.Products.Electronic_devices import electronic_devices
class Computer(electronic_devices):
    """
    This class retains the properties of computers.
    """
    def __init__(self, product_code, product_count, price, Brand, color,size, weight, warranty, processor, operation_system, RAM, series, screen_size, hard_disk_size, CPU):
        super(Computer, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__processor=processor
        self.__operation_system=operation_system
        self.__RAM=RAM
        self.__series=series
        self.__screen_size=screen_size
        self.__hard_disk_size=hard_disk_size
        self.__CPU=CPU
        self.__size = size
    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
               f"Size: {self.__size}\nWeight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nProcessor: {self.__processor}\n" \
               f"Operating System: {self.__operation_system}\nRAM: {self.__RAM}\nSeries: {self.__series}\n" \
               f"Hard Disk Size: {self.__hard_disk_size}\nCPU: {self.__CPU}\nPrice: {self.get_price()} $"

    def __hash__(self):
        return self.__product_code

    def get_processor(self):
        return self.__processor
    def set_processor(self, processor):
        self.__processor=processor

    def get_operation_system(self):
        return self.__operation_system
    def set_operation_system(self, operation_system):
        self.__operation_system=operation_system

    def get_RAM(self):
        return self.__RAM
    def set_RAM(self, RAM):
        self.__RAM=RAM

    def get_series(self):
        return self.__series
    def set_series(self, series):
        self.__series=series

    def get_screen_size(self):
        return self.__screen_size
    def set_screen_size(self, screen_size):
        self.__screen_size= screen_size

    def get_hard_disk_size(self):
        return self.__hard_disk_size
    def set_hard_disk_size(self, hard_disk_size):
        self.__hard_disk_size=hard_disk_size

    def get_CPU(self):
        return self.__CPU
    def set_CPU(self, CPU):
        self.__CPU=CPU

    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size=size



