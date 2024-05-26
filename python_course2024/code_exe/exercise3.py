# exe 1
# def mySort(list1):
#     result = []
#     for item in range(0, len(list1)-1):
#         if list1[item] < list1[item+1]:
#             min = list1[item+1]
#             print("log1:", min)
#         else:
#             min = list1[item]
#             print("log2", min)
#     # print(min)


# mySort([17, 0, -3, 2, 1, 0.5])
# mySort
# print(-3 < 1)


# intermediate 1.2
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, num//2):
#             if num % i == 0:
#                 return False
#     return True


# print(isPrime(101))

# def factorPrime(num):
#     isPrime = 0
#     result = ""
#     for i in range(2, int(num/2)):
#         while (num % i == 0):
#            # print("ans:", int(num/i))
#            # print("i:", i)
#             num = int(num/i)
#            # print("num:", int(num))
#             flag = 1
#             result += str(i) + ' x '
#             print("result", result)
#             if (num == 1):
#                 break
#     if isPrime == 0:
#         return num
#     else:
#         return result


# print(factorPrime(10001))
