class Animal:
    "Animal class"
    def __init__(self, species, age):
        self.__species = species
        self.__age = age

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def set_species(self,species):
        self.__species = species

    def set_age(self,age):
        self.__age = age

    def move(self):
        pass

    def eat(self):
        print("Eating")

class Fish(Animal):
    def __init__(self, species, age, length):
        super().__init__(species, age)
        self.__length = length

    def length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length
    
    def move(self):
        print("Swimming")

class Snake(Animal):
    def length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length
    
    def move(self):
        print("Sliding")

class Snake(Animal):
    def name(self, name):
        self.__name = name

    def get_length(self):
        return self.__name
    
    def move(self):
        print("Walking")

    def work(self):
        print("Working!")

class Book:
    "Book class"
    def __init__(self, title, author, year, genre):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def set_title(self,title):
        self.__title = title

    def set_author(self,author):
        self.__author = author

    def set_year(self,year):
        self.__year = year

    def set_genre(self,genre):
        self.__genre = genre

    def readBy(self, reader):
        print(f"The book {self._title} is read by {reader}")

class Textbook(Book):
    def subject(self, subject):
        self.__subject = subject

    def level(self, level):
        self.__level = level

    def get_subject(self):
        return self.__subject
    
    def get_level(self):
        return self.__level 

class AddressBook(Book):
    def region(self, region):
        self.__region = region

    def get_region(self):
        return self.__region

class Vehicle:
    "Vehicle class"
    def __init__(self, model, manufacturer, year, weight):
        self.__model = model
        self.__manufacturer = manufacturer
        self.__year = year
        self.__weight = weight

    def get_model(self):
        return self.__model

    def get_manufacturer(self):
        return self.__manufacturer

    def get_year(self):
        return self.__year

    def get_weight(self):
        return self.__weight

    def set_model(self,model):
        self.__model = model

    def set_manufacturer(self,manufacturer):
        self.__manufacturer = manufacturer

    def set_year(self,year):
        self.__year = year

    def set_weight(self, weight):
        self.__weight = weight

    def speeding(self):
        print("Vroom")

    def breaking(self):
        print("Skr")

class Car(Vehicle):
    def horsepower(self, horsepower):
        self.__horsepower = horsepower

    def get_horsepower(self):
        return self.__horsepower

    def openDoor(self):
        print("Open the door.")

class Bicycle(Vehicle):
    def wheelSize(self, wheelSize):
        self.__wheelSize = wheelSize

    def get_wheelSize(self):
        return self.__wheelSize

    def ride(self):
        print("Ride the bicycle.")
    
class Boat(Vehicle):
    def length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def surfing(self):
        print("Surfing the boat.")

class HotAirBallon(Vehicle):
    def size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def rise(self):
        print("Hot air ballon in the air.")

