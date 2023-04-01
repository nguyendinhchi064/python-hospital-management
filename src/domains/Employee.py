from Person import Person

class Employee(Person):
    def __init__(self, id, name, gend, dob):
        super().__init__(id, name, gend, dob)
        self.__salary = 0
        self.__department = ""

    def get_salary(self):
        return self.__salary

    def get_dept(self):
        return self.__department

    def set_salary(self, salary):
        self.__salary = salary

    def set_dept(self, dept):
        self.__department = dept