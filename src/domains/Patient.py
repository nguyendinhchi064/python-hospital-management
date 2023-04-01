from Person import Person

class Patient(Person):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__illness = ""
        self.__debt = 0

    def get_illness(self):
        return self.__illness

    def get_debt(self):
        return self.__debt
    
    def set_illness(self, illness: str):
        self.__illness = illness

    def set_debt(self, debt):
        self.__debt = debt