from abc import ABC
from abc import abstractmethod, abstractproperty


class Vehicle(ABC):

    # Defining the constructor method to initialize the Vehicle object
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

        
"""
    An abstract method that returns the number of wheels on the vehicle.
    This method is abstract and has to be implemented by the subclasses.
    
    :return: int, the number of wheels on the vehicle.
"""

    @abstractmethod
    def wheels_num(self) -> int:
        return 0

    def vehicle_type(self) -> str:
        self.vehicle_type = self.brand_name + ' ' + self.__class__.__name__
        return self.vehicle_type

    def is_motorcycle(self) -> bool:
        return Vehicle.wheels_num(self) == 2

    
"""
    Calculates the purchase price of the vehicle based on its base price and mileage. 
    :return: float, the purchase price of the vehicle.
    
    Defining a property to calculate the purchase price of the vehicle
"""

    @property
    def purchase_price(self) -> float:
        if (self.base_price - 0.1 * self.mileage) < 100000:
            vehicle_price = 100000
        else:
            vehicle_price = (self.base_price - 0.1 * self.mileage)
        return vehicle_price
    
    
# blocks define a basic vehicle hierarchy with a common interface for getting information about each vehicle.  
        
class Car(Vehicle):
    def wheels_num(self):
        return 4


class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


class Truck(Vehicle):
    def wheels_num(self):
        return 10


class Bus(Vehicle):
    def wheels_num(self):
        return 6

