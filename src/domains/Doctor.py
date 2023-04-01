from Employee import Employee

class Doctor(Employee):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__IsMedical = True

    def IsMedical(self):
        return self.__IsMedical