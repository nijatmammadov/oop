class Admin:
    def __init__(self, name_and_surname, age, e_mail, phone_number):
        self.__name_and_surname = name_and_surname
        self.__age = age
        self.__e_mail = e_mail
        self.__phone_number = phone_number
        self.list_of_datails=list()
        self.condition=True
    def register_workers(self, name_surname, age, duty, username, password):
        self.list_of_datails = [name_surname, age, duty, username, password]
        try:
            if age < 18:
                self.condition=False
                print("Persons under the age of 18 cannot work")
        except TypeError:
            print("Please enter the age as integer")
        try:
            if len(username)<=6 or len(password)<8:
                print("You must enter a username of more than 6 characters and a password of at least 8 characters.")
                self.condition=False
        except TypeError:
            print("Please enter the username and password as String")

        with open("workers_details.txt","a",encoding="utf-8") as file077:
           for details in self.list_of_datails:
                file077.write(str(details)+",")
           file077.write("\n")