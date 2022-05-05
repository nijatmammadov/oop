from E_Commerce_system.Products.Electronic_devices import electronic_devices
from E_Commerce_system.Products.Computers import Computer
from E_Commerce_system.Products.peripherals.Touchpad import touchpad
class laptops(Computer):
    """
        This class retains the characteristics of Laptops.
    """
    def __init__(self, product_code, product_count, price, Brand, color,size, weight, warranty,
                 processor, operation_system, RAM, series, screen_size,hard_disk_size, CPU,battery_life):
        super(laptops, self).__init__( product_code, product_count, price, Brand, color,size, weight, warranty,
                 processor, operation_system, RAM, series, screen_size,hard_disk_size, CPU)
        self.__battery_life=battery_life
        self.touch_pad = touchpad(product_code, product_count, price, Brand, color, weight, warranty)
    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
                f"Size: {self.get_size()}\nWeight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nProcessor: {self.get_processor}\n" \
                f"Operating System: {self.get_operation_system()}\nRAM: {self.get_RAM()}\nSeries: {self.get_series()}\n" \
                f"Hard Disk Size: {self.get_hard_disk_size()}\nCPU: {self.get_CPU()}\nPrice: {self.get_price()} $\nBattery Life: {self.__battery_life}"

    def get_Battery_life(self):
        return self.__battery_life
    def set_Battery_life(self, battery_life):
        self.__battery_life = battery_life
