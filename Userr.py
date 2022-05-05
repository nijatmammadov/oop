from E_Commerce_system.Amount_in_the_account import account_in_the_amount
from E_Commerce_system.Products.e_book_readers import E_book_reader
from E_Commerce_system.Products.Head_Phones import head_phones
from E_Commerce_system.Products.Product import product
from datetime import datetime
class User:
    """
    Allow to register, to log in, to log out nbwb

    """
    def __init__(self):
        self.__client_details = list()
        self.__aa = list()
        self.__logged_in = False
        self.account_amount = account_in_the_amount().get_amount()

    def register(self, name_and_surname, phone_number, adress, gender, e_mail, password):
        self.conditions = True
        if len(phone_number) != 10:
            print("Invalid phone number")
            self.conditions = False
        if len(password) < 8 or len(password) > 18:
            print("Enter password greater than 8 and less than 18")
            self.conditions = False
        Is_here = e_mail.find("@")
        if Is_here < 0:
            print("Invalid e-mail adress")
            self.conditions = False

        if self.conditions == True:
            print("Account created succesfully")
            self.client_details = [name_and_surname, phone_number, adress, gender, e_mail, password]
            self.Details_to_logged_in=[e_mail,password]
            with open("client_details.txt","a",encoding="utf-8") as file_client:
                for details in self.client_details:
                    file_client.write(str(details)+",")
                file_client.write("\n")
            with open("Details_to_log_in.txt","a",encoding="utf-8") as filee:
                for detailss in self.Details_to_logged_in:
                    filee.write(str(detailss)+",")
                filee.write("\n")

    def Login(self, e_mail_, password_):
            if self.__logged_in == False:
                with open("Details_to_log_in.txt","r",encoding="utf-8") as a:
                    details=a.read()
                    self.client_details=details.split("\n")
                    # print(self.client_details)
                    for s in self.client_details:
                        s=str(s)
                        aa1=s.split(",")
                        self.__aa.append((aa1))

                # while self.logged_in==False:
                    for ii in range(0,len(self.__aa)):
                        if e_mail_ in self.__aa[ii][0] and password_ in self.__aa[ii][1]:
                            print("You have accessed the system successfully")
                            self.__logged_in = True
                            break
                    if self.__logged_in == False:
                        print("User not found\nPlease, enter the information rightly")
            else:
                print("You are already on the system")

    def Log_out(self):
        if self.__logged_in == False:
            print("You are not already in the system")
        else:
            print("You logged out of the system")
            self.__logged_in=False

    def buy_something(self, productt, count):
        self.start_time = datetime(2021, 12, 16, 0, 0, 0)
        self.finish_time = datetime(2021, 12, 17, 0, 0, 0)
        self.now = datetime.now()
        n = productt.get_product_count()
        price=productt.get_price()
        if self.now>=self.start_time and self.now<self.finish_time:
            price=price*(0.9)
            print("Prices are 10 percent lower for Black Friday")
        if self.__logged_in == True and n >= count:
            print("Payment is made to complete the order.......")
            if self.account_amount >= price*count:
                self.account_amount -= price*count
                n -= count
                productt.set_product_count(n)
                print("Order is Completed")
            if type(productt)==E_book_reader and count >= 3:
                productw = head_phones("004", 7, 20, "Sony", "black", "", "No", "Wireless", "WHCH710N", "")
                nn = productw.get_product_count()
                nn-=1
                print(f"Congratulations, you win headphones from us.\nSpecification of your headphones:\n"
                      f"{productw}")
            else:
                print("There is not enough money in your account, please first of all increase your account amount, then try it again")
        elif self.__logged_in == False:
            print("Please, firstly, log in the system and then finished the process")
        else:
            print("There are not enough products in the warehouse")

    def Add_money_to_the_account(self, card_number, mm_yy, cvv_cvc, amount_):
        """
        The user can top up the account with a debit or credit card.
        """
        self.account_amount += amount_
        print(f"Your account ammount: $ {self.account_amount}")

    def get_client_details(self):
        return self.__client_details

    def set_client_details(self, client_details):
        self.__client_details=client_details

    def get_aa(self):
        return self.__aa

    def set_aa(self, aa):
        self.__aa = aa

    def get_logged_in(self):
        return self.__logged_in

    def set_logged_in(self, logged_in):
        self.__logged_in = logged_in

