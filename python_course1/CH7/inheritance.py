class Animal:
    def eat(self):
        print("eating")


class Bird(Animal):
    def eat(self):
        print('Bird')


class Dog(Animal):
    def eat(self):
        print('Dog')


a = Animal()
a.eat()
b = Bird()
b.eat()
c = Dog()
c.eat()

def demo(a):
    a.eat()

for item in [a,b,c]:
    demo(item) 
