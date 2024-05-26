a='12345'

b = [1, 2, 3, 4]

c = ("c","d","a","b")

d = {
    1:"a",
    2:"b",
    3:"c"
}    

for item in d:
    print(item)

for item1,item2 in d.items():
    print("{}= {}".format(item1,item2))  

for item in range(1,20,4):
    print(item)    


