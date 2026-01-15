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

    


my_new_car = Car("Tata", "Safari")
# my_new_car.model = 'Nexon' #! error: property 'model' of 'Car' object has no setter
# print(my_new_car.model()) #! error: str object is not callable


print(my_new_car.model)