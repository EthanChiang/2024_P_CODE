class Robot:

    ingredient = "metal"
    #constructor
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    @staticmethod
    def greet():
        print("A robot says hi.....")

    # def walk(self):
    #     print(f"{self.name} is walking")

    # def sleep(self,hours):
    #     print(f"{self.name} is going to sellp for {hours} hours")    

    # def greet(self):
    #     print(f"hi,my name is {self.name}, and I am made of {self.__class__.ingredient}") 

my_robot1 = Robot("ethan",39)
# # my_robot2 = Robot()
# print(type(my_robot1))
# my_robot1.walk()
# my_robot1.sleep(15)

# my_robot1.greet()
# print(my_robot1.__class__.ingredient)
# print(Robot.ingredient)

Robot.greet()
my_robot1.__class__.greet()
my_robot1.greet()