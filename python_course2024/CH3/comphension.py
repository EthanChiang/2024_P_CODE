import sys
x = [1, 2, 3, 4]
square_x = []
# for item in x:
#     square_x.append(item**2)

# print(square_x)

# square_x = [item**2 for item in x]
# print(square_x)


# square_x=[item**2 for item in x if item >2]
# print(square_x)

x_square_dict = {item: item ** 2 for item in x if item > 2}
print(x_square_dict)

# x_square_set ={item **2 for item in x if item >2}
# print(x_square_set)

print(sys.path)
