def mySum(*args):
    result = 0
    for item in args:
        result = result+item

    return result


print(mySum(1, 2, 3, 4))
