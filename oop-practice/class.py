class Car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
    def car(self):
        return f"{self.model} {self.year} {self.make}"
car = Car("Toyota", 2023, "Carmy")
print(car.car())
        