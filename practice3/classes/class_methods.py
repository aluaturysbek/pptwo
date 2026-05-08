class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car brand:", self.brand)

car1 = Car("Toyota")

car1.show()