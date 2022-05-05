from E_Commerce_system.Products.Electronic_devices import electronic_devices
class Video_games_consoles_accessories(electronic_devices):
    """
        This class retains the features of video games consoles accessories.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, controller_type):
        super(Video_games_consoles_accessories, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__controller_type = controller_type

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
                f"Weight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nController Type: {self.__controller_type}"

    def get_controller_type(self):
        return self.__controller_type
    def set_controller_type(self, controller_type):
        self.__controller_type = controller_type