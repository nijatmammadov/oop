from  E_Commerce_system.Products.Electronic_devices import electronic_devices
class tvs(electronic_devices):
    """
        This class retains the features of TVs.
    """
    def __init__(self, product_code, product_count, price, Brand, color, weight, warranty, screen_size, sapported_internet_services,
                 connectivity_technology, resulution, display_technology, model_name, refresh_rate, year):
        super(tvs, self).__init__(product_code, product_count, price, Brand, color, weight, warranty)
        self.__screen_size = screen_size
        self.__sapported_internet_services = sapported_internet_services
        self.__connectivity_technology = connectivity_technology
        self.__resulution = resulution
        self.__display_technology = display_technology
        self.__model_name = model_name
        self.__refresh_rate = refresh_rate
        self.__year = year

    def __str__(self):
        return f"Product code: {self.get_product_code()}\nProduct count: {self.get_product_count()}\nBrand: {self.get_Brand()}\nColor: {self.get_color()}\n" \
                f"Weight: {self.get_weight()}\nWrranty: {self.get_warranty()}\nScreen Size: {self.__screen_size}\n" \
               f"Sapported Internet Services: {self.__sapported_internet_services}\nConnectivity Technology: {self.__connectivity_technology}\n" \
               f"Resulation: {self.__resulution}\nDisplay Technology: {self.__display_technology}\nModel Name: {self.__model_name}" \
               f"Refresh Name: {self.__refresh_rate}\nYear: {self.__year}"



    def get_screen_size(self):
        return self.__screen_size
    def set_screen_size(self, screen_size):
        self.__screen_size = screen_size

    def get_sapported_internet_services(self):
        return self.__sapported_internet_services
    def set_sapported_internet_services(self, sapported_internet_services):
        self.__sapported_internet_services = sapported_internet_services

    def get_connectivity_technology(self):
        return self.__connectivity_technology
    def set_connectivity_technology(self, connectivity_technology):
        self.__connectivity_technology = connectivity_technology

    def get_resulution(self):
        return self.__resulution
    def set_resulution(self, resulution):
        self.__resulution = resulution

    def get_display_technology(self):
        return self.__display_technology
    def set_display_technology(self, display_technology):
        self.__display_technology = display_technology

    def get_model_name(self):
        return self.__model_name
    def set_model_name(self, model_name):
        self.__model_name = model_name

    def get_refresh_rate(self):
        return self.__refresh_rate
    def set_refresh_rate(self, refresh_rate):
        self.__refresh_rate = refresh_rate

    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year