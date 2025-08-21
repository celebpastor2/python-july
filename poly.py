from abc import ABC, abstractmethod

class Auto(ABC) :    
    __brand = ""
    __color = ""
    __model = ""
    __engine= ""

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def stop():
        pass
    
    @abstractmethod
    def speed():
        pass
    
    @property
    @abstractmethod
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @brand.deleter
    def brand(self):
        self.__brand = None 
    
    @property
    @abstractmethod
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @brand.deleter
    def brand(self):
        self.__color = None 
    
    @property
    @abstractmethod
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @model.deleter
    def model(self):
        self.__model = None 
    
    @property
    @abstractmethod
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value):
        self.__engine = value

    @engine.deleter
    def engine(self):
        self.__engine = None


class Car(Auto):
    brand = ""
    color = ""
    model = ""
    engine = ""

    def move():
        print("Voom")





class Bike(Auto):
    brand = ""
    color = ""
    model = ""
    engine = ""

    def move(): 
        print("Zooom")

class Boat(Auto):
    color = "Red"
    model = "Armani"
    __brand = "See"

    def move(self): 
        print(self.__brand)

    def __turn():
        pass
