class workers:
    def __init__(self, name_and_surname, age, duty, hours_work_a_day):
        self.__name_and_surname = name_and_surname
        self.__age = age
        self.__duty = duty
        self.__hours_work_a_day = hours_work_a_day
        self.__list = list()
        self.__is_in_system = False

    def get_name_and_surname(self):
        return self.__name_and_surname

    def set_name_and_surname(self, name_and_surname):
        self.__name_and_surname = name_and_surname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_duty(self):
        return self.__duty

    def set_duty(self, duty):
        self.__duty = duty

    def get_hours_work_a_day(self):
        return self.__hours_work_a_day

    def set_hours_work_a_day(self, hours_work_a_day):
        self.__hours_work_a_day = hours_work_a_day

    def get_is_in_system(self):
        return self.__is_in_system

    def set_is_in_system(self, is_in_system):
        self.__is_in_system = is_in_system

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
                    self.__is_in_system = True
                    break

            except IndexError:
                break

        if self.__is_in_system==False:
            print("Something went wrong, may be your username or password wrong which you entered")