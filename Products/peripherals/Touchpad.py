from E_Commerce_system.Products.Electronic_devices import electronic_devices
class touchpad(electronic_devices):
    def __init__(self, product_code, product_count, price, Brand, color, weight , warranty ):
        super(touchpad, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        
    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
               f"Weight: {self.get_weight()}\nWrranty: {self.get_warranty()}"
