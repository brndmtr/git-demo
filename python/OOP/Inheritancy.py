class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent):
    hair_color = "red"
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

print(Child.hair_color)