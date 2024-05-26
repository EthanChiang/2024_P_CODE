import shelve

# integer1 = [1,2,3,4,5,6]
# integer2 = [6,7,8,9,10]
# integer3=[100,101,102,103]

# with shelve.open("shelf-example","c") as shelf:
#     shelf["ints1"] = integer1
#     shelf["ints2"] = integer2
#     shelf["ints3"] = integer3


with shelve.open("shelf-example","r") as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf["ints2"])