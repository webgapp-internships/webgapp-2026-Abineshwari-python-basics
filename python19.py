class Vehicles:

    def __init__(self, brand,speed):

        self.brand = brand
        self.__speed = speed

    def get_speed(self):

        return self.__speed

    def vehicle_info(self):

        return f"brand : {self.brand}"


class Car(Vehicles):

    def __init__(self, brand, speed, fuel_type):
         
         super().__init__(brand, speed)

         self.fuel_type = fuel_type
    
    def display_details(self):

        print(self.vehicle_info())
        print("Speed :", self.get_speed())
        print("Fuel Type :", self.fuel_type)    

        if self.get_speed() >= 120:

            print("Status : Fast Car")

        else:

            print("Status : Normal Car")
            
            print()

Car1 = Car("Toyota", 120, "petrol")
Car2 = Car("Thar", 180, "Diesel")
Car3 = Car("Hyundai creta", 100, "Petrol")

Car1.display_details()
Car2.display_details()
Car3.display_details()