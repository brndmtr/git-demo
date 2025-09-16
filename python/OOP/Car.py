class Car:
    def __init__(self, color:str, mileage:str):
        self.color: str = color
        self.mileage: str = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage} miles"


blue = Car("blue", "20,000")
red = Car ("red", "30,000")
print(blue.description())
print(red.description())