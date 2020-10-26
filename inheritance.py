class Vehicle:
    def generic_purpose(self):
        print("This is used for transportation")


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.roof = True

    def specific_purpose(self):
        print(f"Car has {self.wheels} wheels, and travel with family")


class MotorCycle(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.roof = False

    def specific_purpose(self):
        print(f"MotorCycle has {self.wheels} wheels, and used for road trip")


class Father:
    def skills(self):
        print("Gardening and programing")


class Mother:
    def skills(self):
        print("Cooking and art")

# Multiple inheritance


class Child(Father, Mother):
    def skills(self):
        Mother.skills(self)
        Father.skills(self)
        print("Sports")


if __name__ == '__main__':
    c = Car()
    c.generic_purpose()
    c.specific_purpose()

    m = MotorCycle()
    m.generic_purpose()
    m.specific_purpose()

    # isinstance
    print(isinstance(c, Car))
    print(issubclass(Car, MotorCycle))

    child = Child()
    child.skills()

