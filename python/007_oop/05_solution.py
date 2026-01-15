class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

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
    
tesla = ElectricCar("Tesla", "Model S", '85kWh')
print(tesla.get_brand())
print(tesla.fuel_type())

tata = Car("tata", "Safari")
print(tata.get_brand())
print(tata.fuel_type())