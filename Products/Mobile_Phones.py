
from  E_Commerce_system.Products.Electronic_devices import electronic_devices
class mobile_phones(electronic_devices):
    """
        This class retains the features of Mobile phones.
    """
    def __init__(self,product_code, product_count, price, Brand, color,size, weight, warranty, model_name, operating_system,
                 year, sim_card_slot_count, cellular_technology, memory_storage_capacity, form_factor, rear_wide_camera,
                 front_wide_camera,ram, battery_life):
        super(mobile_phones, self).__init__(product_code,product_count,price,Brand,color, weight, warranty)
        self.__size = size
        self.__model_name = model_name
        self.__operating_system = operating_system
        self.__year = year
        self.__sim_card_slot_count = sim_card_slot_count
        self.__cellular_technology = cellular_technology
        self.__memory_storage_capacity = memory_storage_capacity
        self.__form_factor = form_factor
        self.__rear_wide_camera = rear_wide_camera
        self.__front_wide_camera = front_wide_camera
        self.__battery_life = battery_life
        self.__ram = ram

    def __str__(self):
        return f"Product code: {self.get_product_code}\nProduct count: {self.get_product_count}\nBrand: {self.get_Brand}\n" \
               f"Color: {self.get_color}\nSize: {self.__size}\nWeight: {self.get_weight}\nWrranty: {self.get_warranty}\n" \
               f"Model Name: {self.__model_name}\nOperating System: {self.__operating_system}" \
                f"\nRAM: {self.__ram}\nSim card slot count: {self.__sim_card_slot_count}\nCellular Technology: " \
               f"{self.__cellular_technology}\nMemory Storage Capacity: {self.__memory_storage_capacity}\nForm Factor: {self.__form_factor}" \
                f"\nRear Wide Camera: {self.__rear_wide_camera}\nFront Wide Camera: {self.__front_wide_camera}\nPrice: {self.__price} $"

    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size = size

    def get_model_name(self):
        return self.__model_name
    def set_model_name(self, model_name):
        self.__model_name = model_name

    def get_operating_system(self):
        return self.__operating_system
    def set_operating_system(self, operating_system):
        self.__operating_system = operating_system

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year

    def get_sim_card_slot_count(self):
        return self.__sim_card_slot_count
    def set_sim_card_slot_count(self, sim_card_slot_count):
        self.__sim_card_slot_count = sim_card_slot_count

    def get_cellular_technology(self):
        return self.__cellular_technology
    def set_cellular_technology(self, cellular_technology):
        self.__cellular_technology = cellular_technology

    def get_memory_storage_capacity(self):
        return self.__memory_storage_capacity
    def set_memory_storage_capacity(self, memory_storage_capacity):
        self.__memory_storage_capacity = memory_storage_capacity

    def get_form_factor(self):
        return self.__form_factor
    def set_form_factor(self, form_factor):
        self.__form_factor = form_factor

    def get_rear_wide_camera(self):
        return self.__rear_wide_camera
    def set_rear_wide_camera(self, rear_wide_camera):
        self.__rear_wide_camera = rear_wide_camera

    def get_front_wide_camera(self):
        return self.__front_wide_camera
    def set_front_wide_camera(self, front_wide_camera):
        self.__front_wide_camera = front_wide_camera

    def get_battery_life(self):
        return self.__battery_life
    def set_battery_life(self, battery_life):
        self.__battery_life = battery_life

    def get_ram(self):
        return self.__ram
    def set_ram(self, ram):
        self.__ram = ram
