class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def fullname(self):
        return f'{self.__brand} {self.__model}'
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
tesla = ElectricCar("Tesla", "Model S", '85kWh')
print(tesla.fullname())
print(tesla.get_brand())

# HW: setter function self study