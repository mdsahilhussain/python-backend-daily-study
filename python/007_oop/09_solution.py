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
    
    @staticmethod
    def general_description():
        return 'Cars are means of transport'
    
    @property
    def model(self):
        return self.__model

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric Charge'
    
tesla = ElectricCar("Tesla", "Model S", '85kWh')

isinstance_check_1 = isinstance(tesla, ElectricCar)
isinstance_check_2 = isinstance(tesla, Car)

print(isinstance_check_1)
print(isinstance_check_2)
