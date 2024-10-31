class Car:
    def __init__(self, brand, model, year, mileage, _fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_started = False
        self.__fuel_level = _fuel_level

    def refuel(self, amount):
        if amount >= 100:
            print("Error")
        else:
            self.__fuel_level = amount
            print("Success!")

    def start_engine(self):
        self.engine_started = True

    def drive(self, miles):
        self.mileage = miles

    def display_info(self):
        print("Brand:", self.brand, "Model:", self.model, "Year:", self.year, "Mileage:", self.mileage, "Engine started:", self.engine_started, "Fuel Level:", self.__fuel_level)
#
#
#
# car1 = Car("Ford", "Mustang", 2021, 0, 0)
car2 = Car("BMW", "3 Series", 2022, 0, 0)
# car1.start_engine()
# car1.drive(100)
# car1.display_info()
# car1.refuel(100)
# car2.refuel(50)
car2.__fuel_level=100
car2.display_info()
