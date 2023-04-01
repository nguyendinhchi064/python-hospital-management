class Person():
    def __init__(self, id, name, gend, dob):
        self.__id = id
        self.__name = name
        self.__gend = gend
        self.__dob = dob
        self.__phone = ""
        self.__email = ""

    # get info
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_gend(self):
        return self.__gend

    def get_dob(self):
        return self.__dob

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    # set info
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_gend(self, gend):
        self.__gend = gend

    def set_dob(self, dob):
        self.__dob = dob

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email
