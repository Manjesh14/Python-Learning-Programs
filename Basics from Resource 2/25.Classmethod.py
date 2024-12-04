class Person:
    name="anonymus"
    def Change(self,name):
        Person.name=name
        self.__class__.name=name

p1=Person()
p1.Change("Manjesh")
print(p1.name)
print(Person.name)