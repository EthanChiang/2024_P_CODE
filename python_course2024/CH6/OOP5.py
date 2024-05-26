class Robot:
    def __init__(self,name) -> None:
        self.name = name
        self.__age =25

    def __this_is_private(self):
        print("This is private method")

    def greet(self):
        print("Hi,I am a robot")
        self.__this__is_private()

    def age_setter(self,new_age):
        self.__age=new_age

    def age_getter(self):
        print(self.__age)          

my_robot = Robot("Ethan")
# my_robot.__this_is_private()        
