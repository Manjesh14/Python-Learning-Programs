class Car:
    def __init__(self) -> None:
        self.accelerator = False
        self.brk= False
        self.clutch=False

    def start(self):
        self.accelerator = True
        self.clutch=True
        print("Car Started .....")

car1=Car()
car1.start()