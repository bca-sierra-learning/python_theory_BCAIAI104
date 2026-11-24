class Car:
    #class members

    def __init__(self):
        #instance variables
        self.manufacturer=""
        self.modelno=""
        self.color=""
        self.price=""
        self.number=""

    #member methods
    def start_car(self):
        print("Car started..")

    def stop_car(self):
        print("Car stoped..")

    def change_color(self,newColor):
        print(f"Color changed to {newColor} ")

    def get_color(self):
        print(f"Car colur is: {self.color}")

    def initial_car(self):
        self.manufacturer=input('Enter car manufacturer name : ')
        self.color=input("Enter car color :")

    def display_car(self):
        print(f"MAnufacturer name : {self.manufacturer}")
        print(f"Car color : {self.color}")

#creating the object
#syntax : objectname=classname()
firstCar=Car()
firstCar.initial_car()
secondCar=Car()
secondCar.initial_car()
firstCar.get_color()
secondCar.get_color()



