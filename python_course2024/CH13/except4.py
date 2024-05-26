# try:
#     lst = [1, 2, 3]
#     print(lst[4])  # index Error

# except KeyError:
#     print("There is a key error")

# except LookupError:
#     print("There is a look up error")

# # except IndexError:
# #     print("There is index error")

# def divide(a, b):
#     if type(a) != int and type(b) != int:
#         if b != 0:
#             return a/b
#         else:
#             return " the second argument can not be 0"
#     else:
#         return "Invalid argument type!!"

def divide(a, b):
    if type(a) != int and type(b) != int:
        raise ValueError("not Valid type given!!")
    if b == 0:
        raise ZeroDivisionError("Second argument cannot be 0")

    return a/b


try:
    print(divide(10, 0))
    print(divide(6, 3))

except Exception as e:
    print(e)
