## Class with Default Values: Modify the Car class to have default values for make and model if not provided.

class Car:
    def __init__(self, make='Toyota', model='Corolla', year=2019):
        self.make = make
        self.model = model
        self.year = year

car = Car()
print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")
car = Car('Honda', 'Civic', 2020)