from Userr import User
from E_Commerce_system.Products.Cameras import cameras
from E_Commerce_system.Products.Product import product
from E_Commerce_system.Products.Electronic_devices import electronic_devices
from Sales_manager import Sales_Manager
from E_Commerce_system.Products.Computers import Computer
from Sales_Persons import Sales_persons
from E_Commerce_system.Products.Mobile_Phones import mobile_phones
from E_Commerce_system.Products.video_games_consoles_accessories import Video_games_consoles_accessories
from E_Commerce_system.Products.peripherals.Touchpad import touchpad
from E_Commerce_system.Products.Laptops import laptops
from E_Commerce_system.admin import Admin
from E_Commerce_system.Products.e_book_readers import E_book_reader
from datetime import datetime
from E_Commerce_system.Products.Data_storage import Data_Storage
from E_Commerce_system.Products.peripherals.mouse import Mouse
from E_Commerce_system.Products.peripherals.stylus import stylus
print("*********************************************************")
nicat=User()
nicat.register("Nicat Mammadov","0502552222","Baku,Azerbaijan","Male","nicat@gmail.com","nicat4561")
nicat.Login("nicat@gmail.com","nicat4561")
print("*********************************************************")

admin = Admin("Eloyset Adigozelov",46, "eloyset.adigozelov@gmail.com","055- 125 45 15")
admin.register_workers("Tural Hasanli", 25, "Sales Manager", "Tural_e_com","tural78565")
admin.register_workers("Farid Sattarov",23,"Sales Manager","farid_sattar","farid78526")
admin.register_workers("Elsever Gasimov", 21,"Sales Person","elsever_","elsever456")
admin.register_workers("Subhan Shirinzade",26,"Sales Person","subhan753","subhan_qwwww")
admin.register_workers("Togrul Mammadli",19,"Sales Person", "togrul.077", "togrul458")
print("*********************************************************")


Tural=Sales_Manager("Tural Hasanli",25,"Sales Manager",6)
Farid=Sales_Manager("Farid Sattarov",23,"Sales Manager",8)
print("*********************************************************")


darya=User()
darya.register("Darya Alakbarov","0505663231","Baku,Azerbaijan","Male","darya@gmail.com","passww144")
darya.Login("darya@gmail.com","passww144")


nicat.Login("nicat@gmail.com","nicat4561")
nicat.Log_out()
nicat.Login("nicat@gmail.com","nicat4561")

print("********************************")

print("************************Products*********************************")
SanDisk=Data_Storage("077","4",59.99,"SanDisk","Black,red","","","128 GB","","specific","","","","","","USB 2")
iBUYPOWER = Computer("001", 5, 1229, "IBUYPOWER","Black","15 inc","1.8 kg","2 year","Intel i7-11700F 2.5GHz","Windows 10","16 GB","208i","1 Centimeters","240 GB","Core i7")
mouse=Mouse("044",4,8.99, "HP", "Black", "" , "", "Wifi , USB", "optical")
Stylus = stylus("0123",7,47.99,"JAMJAKE","white","","", "1 Lithium Metal batteries required. (included)"," Tablets", "90 minutes")

Tural.Add_Product(SanDisk)
Farid.Add_Product(iBUYPOWER)
Tural.Add_Product(mouse)
Farid.Add_Product(Stylus)
print("*********************************************************")
print(nicat.account_amount)
n=input("Please, enter the card number: ")
m=int(input("How much do you want to add: "))
date=input("MM/YY: ")
cvv=input("CVV: ")
nicat.Add_money_to_the_account(n, cvv, date,m)
nicat.buy_something(iBUYPOWER,6)
print(nicat.account_amount)


print(Computer.__doc__)

print(iBUYPOWER)

ss = touchpad("002", "4", "320", "Eloyset", "black", "dde", "2")
print(ss)
Farid.Add_Product(ss)
kk=laptops("112",4,1455,"Asus","galaboy","15 inch","14kg","2 year","efubf","ygceye","ygyg","eygvy","ueygyec","euguf","euhe","euheu")

Tural.Add_Product(kk)
darya.buy_something(iBUYPOWER,5)
print(darya.account_amount)
darya.Add_money_to_the_account("4555123378994566","11/22","565",5000)

darya.buy_something(iBUYPOWER,2)
print(darya.account_amount)
print(iBUYPOWER.get_product_count())

Elsever=Sales_persons("Elsever Gasimov",21,"Sales Person",8)
Emin=Sales_persons("Emin Kazimov",26,"Sales Person",8)


for seller in (Emin,Elsever, Tural, Farid):
    print("**********************")
    seller.introduce_yourself()


admin.register_workers("Khanlar Azizov", 25, "Sales Manager", "khanlar.077","khanlar123")
khanlar=Sales_Manager("Khanlar Azizov", 25, "Sales Manager","6")
s=input("Enter your username: ")
ss=input("Enter your password: ")
khanlar.log_in_as_worker(s,ss)
khanlar.Add_Product(iBUYPOWER)
print(khanlar.get_product_list())
kobo = E_book_reader("012", 5, 59.99, "Kobo", "Black", "6 Inches", "5.9 Ounces","8 GB", "2 Hours", " 1 year")
print(nicat.account_amount)
nicat.buy_something(kobo, 4)
print(kobo.get_product_count())

