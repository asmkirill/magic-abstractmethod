# Magic - ABS - abstractmethod

This program is a implementation of an abstract class and its derived classes in Python. 

The abstract class is called Vehicle, and it has four parameters: brand_name, year_of_issue, base_price, and mileage. 

The program includes four derived classes from Vehicle: Car, Motorcycle, Truck, and Bus, which inherit all of the properties of the Vehicle class.

The Vehicle class also includes three methods that must be implemented by the derived classes. 
The vehicle_type method returns a string that represents the type of the vehicle, using the format of brand_name + name of the class. 
The is_motorcycle method returns a boolean value depending on the number of wheels of the vehicle (2 wheels indicate a motorcycle). 
The purchase_price method calculates the price of the vehicle, which is the base_price minus 0.1 times the mileage. 

If the resulting price is less than 100,000, the method should return 100,000.

The program also includes various decorators, such as abstractmethod, staticmethod, and property, to ensure proper functioning of the methods. 
All classes and methods have been already implemented, and the program is ready to use.


The @property decorator is used in the purchase_price method of the Vehicle class to define a method that behaves like an attribute. 
This allows the method to be accessed like a regular attribute, using dot notation, without the need to call it like a method.
By defining purchase_price as a property, the calculation of the purchase price is done automatically each time the attribute is accessed, 
without the need for an explicit method call. 
This makes the code more concise and easier to read, while still providing the functionality of a method.

Using @property also allows for the possibility of adding additional code to the getter or setter methods in the future, 
without having to modify any code that relies on the property. This makes the code more maintainable and flexible.


The @abstractmethod decorator is used to define an abstract method in an abstract base class in Python. 
An abstract method is a method that is declared but does not have an implementation. 
It is meant to be overridden in a derived class, where it will have a concrete implementation.
