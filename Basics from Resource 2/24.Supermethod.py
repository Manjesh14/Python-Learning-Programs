class car:
    def __init__(self, type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started .....")
    @staticmethod
    def stop():
        print("Car Stopped .....")

class Toyota(car):
    def __init__(self,brand,type):
        super().__init__(type)
        self.name=brand
        super().start

car1=Toyota("Primus","electric")
print(car1.type)