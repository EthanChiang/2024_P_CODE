#字典
a={
    1: 'a',
    2: 'b',
    '3':'c'
}

print(a)

#不可改變的數據類型

l1 = [1, 2, 3]


# b = {
#     l1: 1
# }



t1 = (1, 2, 3)

c = {
   t1: l1
}
print(c)

d = dict()
print(d)

c = dict(a=1, b='ff', c='a')
print(c['c'])

f = {1:1}
f[2] = 2
f[3] = 3

print(f)

c.update(f)

print(c)
print(c.keys())
print(c.items())


