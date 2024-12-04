class car:
    @staticmethod
    def start():
        print("Car Started .....")
    @staticmethod
    def stop():
        print("Car Stopped .....")

class Toyota(car):
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type=type

car2=Fortuner("disel")
print(car2.type)