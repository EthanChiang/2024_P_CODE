class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protect_var = 10
        self.__private_var = 10

    def sayhi(self):
        print("my name is {}".format(self.name))

    def get_var(self):
        print(self.__private_var)

    def set_var(self, var):
        self._private_var = var


person1 = people(name='ethan', age=39)
person1.sayhi()
print(person1.name)
person1._protect_var = 30
print("person1:", person1._protect_var)
# print(dir(person1))
print('person1.__private_var', person1._people__private_var)
person1.get_var()
