from E_Commerce_system.Products.Electronic_devices import electronic_devices
class head_phones(electronic_devices):
    """
        This class retains the characteristics of headphones.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, connectivity_technology,
                 model_name, form_factor):
        super(head_phones, self).__init__( product_code, product_count, price, Brand, color, weight, warranty)
        self.__connectivity_technology = connectivity_technology
        self.__model_name = model_name
        self.__form_factor = form_factor

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\n" \
               f"Color: {self.get_color()}\nWeight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nConnectivity Technology: {self.__connectivity_technology}\n" \
               f"Model Name: {self.__model_name}\nForm Factor: {self.__form_factor}\nPrice: {self.get_price()}"

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_model_name(self):
        return self.__model_name
    def set_model_name(self, model_name):
        self.__model_name=model_name

    def get_form_factor(self):
        return self.__form_factor
    def set_form_factor(self,form_factor):
        self.__form_factor=form_factor