# def add(*args):
#     print(args,type(args))
#     result = 0
#     for item in args:
#        result = result+ item
#     return result        

# add(1, 2, 3,10,20, 30)    

# def test(a, b, c):
#     print(a+ b+ c)

# def add(x,**kwargs):
#     print(type(kwargs))
#     if x==2:
#         test(**kwargs)

# add(2,a=1,b=2,c=3)

def demo(a,b=False):
    if b:
    #    print(b)
        pass
        print(b)
    else:
        return a*a
    

demo(a=3,b=True)   