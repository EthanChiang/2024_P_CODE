# def higherOrder(fn):
#     fn()

# def smallfunc():
#        print("Hello function")

# higherOrder(smallfunc)       

# def square(num):
#     return num**2


# myList=[-10,3,5,84,2]
# for item in map(square,myList):
#     print(item)

# for item in map(lambda x:x**2,[15,10,5,4]):
#     print(item)

for item in filter(lambda x:x**2==100,[15,10,5,4]):
    print(item)    