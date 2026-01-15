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
    


Car("Tata", "Safari")
Car("Tata", "Nexon")
Car("Tata", "Carve")

print(Car.general_description())