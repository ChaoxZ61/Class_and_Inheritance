class Animal:
    "Animal class"
    def __init__(self, species, age):
        self._species = species
        self._age = age

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def set_species(self,species):
        self._species = species

    def set_age(self,age):
        self._age = age

    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")

class Book:
    "Book class"
    def __init__(self, title, author, year, genre):
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._year

    def get_genre(self):
        return self._genre

    def set_title(self,title):
        self._title = title

    def set_author(self,author):
        self._author = author

    def set_year(self,year):
        self._year = year

    def set_genre(self,genre):
        self._genre = genre

    def readBy(self, reader):
        print(f"The book {self._title} is read by {reader}")

class Vehicle:
    "Vehicle class"
    def __init__(self, model, manufacturer, year, horsepower, weight):
        self._model = model
        self._manufacturer = manufacturer
        self._year = year
        self._horsepower = horsepower
        self._weight = weight

    def get_model(self):
        return self._model

    def get_manufacturer(self):
        return self._manufacturer

    def get_year(self):
        return self._year

    def get_horsepower(self):
        return self._horsepower

    def get_weight(self):
        return self._weight

    def set_model(self,model):
        self._model = model

    def set_manufacturer(self,manufacturer):
        self._manufacturer = manufacturer

    def set_year(self,year):
        self._year = year

    def set_horsepower(self,horsepower):
        self._horsepower = horsepower

    def set_weight(self, weight):
        self._weight = weight

    def speeding(self):
        print("Vroom")

    def breaking(self):
        print("Skr")

    def openDoor():
        print("The door is opend.")
    
    