from employee import Employee
class SalaryEmployee(Employee):
    def __init__(self, name, age, dob, gender, phone, number, street, city, state, id, level, email, salary):
        super().__init__(name, age, dob, gender, phone, number, street, city, state, id, level, email)
        self.__salary = salary

    def __str__(self):
        return f""""
        {super().__str__()}
            Salary: {self.__salary}
        """

s1 = SalaryEmployee("Chigbo",26,"13/05/1998","M", "09115051754", 312, "Herbaert", "yaba", "lagos", "E0841","senior","chigbo@microsoft.com", 5000000)
print(s1)
