### Encapsulation

class Vehicle:

    #Attributes
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    

    #Methods
    def display_info(self):
        return f"The car is manufactured by {self.make} in the year {self.year} and the model is {self.model}."


#Example 1
Vehicle_1=Vehicle("Ford","Mustang","1921")
print(Vehicle_1.display_info())



### Inheritance

class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        super().__init__(make,model,year)
        self.doors=doors

    def display_info(self):
        return f"The car is manufactured by {self.make} in the year {self.year} and the model is {self.model} with {self.doors} doors."

Car_1=Car("Maruti","Suzuki",1921,4)
print(Car_1.display_info())
