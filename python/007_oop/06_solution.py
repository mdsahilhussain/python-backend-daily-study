class Car:
    total_car_variable = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car_variable += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def fullname(self):
        return f'{self.__brand} {self.__model}'
    
    def fuel_type(self):
        return 'Petro & Diesel'
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'


Car("Tata", "Safari")
Car("Tata", "Nexon")
Car("Tata", "Carve")

print(Car.total_car_variable)