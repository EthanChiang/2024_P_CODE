class C:
    def do_stuff(self):
        print("hello from class C")

class D:
    def do_another(self):
        print("DDDDDDD")

class A(C,D):
   pass

a=A()
a.do_stuff()
a.do_another()