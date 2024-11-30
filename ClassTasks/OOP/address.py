
class Address:
    def __init__(self,  number, street, city, state):
        self.__number = number
        self.__street = street
        self.__city = city
        self.__state = state

    def __str__(self):
        return f"{self.__number}  {self.__street} {self.__city} {self.__state}"
