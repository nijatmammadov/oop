from Workers import workers



class Sales_persons(workers):
    def __init__(self, name_and_surname, age, duty, hours_work_a_day):
        super(Sales_persons, self).__init__(name_and_surname, age, duty, hours_work_a_day)
        self.logged_in = False

    def introduce_yourself(self):
        if self.logged_in==True:
            print(f"Hello, I am {self.get_name_and_surname()}, I am {self.get_age()} years old.\n"
                  f" My duty is {self.get_duty()}.The job here is to send orders as an online seller.\n"
                  f" I work {self.get_hours_work_a_day()} hours a day.")


    def log_in_as_worker(self, username, password):
        with open("workers_details.txt", "r", encoding="utf-8") as file_workers:
            s = file_workers.read()
            list1 = s.split("\n")
        for lines in list1:
            self.__list = lines.split(",")
            try:
                if self.__list[3] == username and self.__list[4] == password:
                    print("You have successfully accessed.")

                    print(f"""
                        *********************************************
                        Your name and surname: {self.__list[0]}
                        Your age: {self.__list[1]}
                        Your duty: {self.__list[2]}
                        Your username: {self.__list[3]}
                        Your password: {self.__list[4]}
                        *********************************************
                        """)
                    self.logged_in = True
                    break

            except IndexError:
                break

        if self.logged_in ==False:
            print("Something went wrong, may be your username or password wrong which you entered")