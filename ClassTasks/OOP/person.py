from address import Address
class Person:
    def __init__(self, name, age, dob, phone, gender, number, street, city, state):
        self.__name = name
        self.age = self.validate_age(age)
        self.__dob = dob
        self.__phone = phone
        self.__gender = gender
        self.__address = Address(number, street, city, state)


    def get_name(self):
        return self.__name

    def validate_age(self, age):
        if age < 0 or age > 150:
            return "Age must not be less than 0 or greater to 13"
        else:
            return age

    def set_age(self, age):
        self.age = self.validate_age(age)

    def get_age(self):
        return self.age

    def greet(self):
        return f"Hello, {self.__name}"

    def __str__(self):
        return f""""
        Name: {self.__name}
        Age: {self.age}
        Dob: {self.__dob}
        Phone: {self.__phone}
        Gender: {self.__gender}
        Address: {self.__address}
        
        
        """


p1 = Person("Eniola", 22, "13/13/2002", "09115051754", "M", 312, "Albert", "Ikeja", "lagos")
print(p1)