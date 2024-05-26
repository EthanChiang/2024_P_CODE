# y = [1, 2, 3]
# a= [1, 2, 3, 4 , 5]

# y.append("4")
# print(y)
# def demo1(a):
#     a.append(6)
#     print("a:" , a)

# demo1(a = y)
# print(y)



z = 1 
def demo2(a):
    global z 
    print(z,type(z))
    z = z+y
  #  print(z)

demo2(a=5)
         