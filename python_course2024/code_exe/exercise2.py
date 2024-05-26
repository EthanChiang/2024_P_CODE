# def mySort(list_num):
#     sorted = []
#     for item in list_num:
#     #    for num in i:
#         #    print("num",list_num[i])  #抓出數字
#         # print(item)
#         for i in range(0,len(list_num)):
#             if(list_num[i] < list_num[i+1]):
#                 list_num[] = list_num[i]

# 把最小的放在第一個
# 反覆做

#    print("i",i)
# def findMin(lst):
#     result =lst[0]
#     for ele in lst:
#         if ele <result:
#             result = ele
#     return  result

# def mySort(myList):
#     result_list = []
#     while len(myList) > 0:
#         min_element = findMin(myList)
#         result_list.append(min_element)
#         myList.remove(min_element)
#     return result_list

# print(mySort([17,0,-3,2,1,0.5]))

# exe2
# def isPrime(num):
#     if num < 2:
#         return False
#     else:
#         starter =2
#         while starter < num:
#             if num % starter ==0:
#               return False
#             starter+=1
#     return True

# print(isPrime(10001))
# print(isPrime(5))
# print(isPrime(91))

# #exe3
# def palindrome(str):
#     txt = str[::-1]
#     # print(txt)
#     if txt == str:
#         return True
#     else:
#         return False

# print(palindrome("bearaeb"))
# print(palindrome("this is good day to die"))

# exe4

# def pyrmid(num):
#     for i in range(num,0,-1):
#       print("*"*i,"i"*i)
#     #   print("i"*i)

# pyrmid(2)

# def pyrmid(n):
#     space = n-1
#     star =1
#     for i in range(n):
#         print(space*" "+ star * "*")
#         star +=2
#         space -= 1

# pyrmid(4)

# def inversePyrmid(n):
#     space = 0
#     star = 2*n - 1
#     for i in range(n):
#         print(space*" "+ star * "*")
#         star -=2
#         space += 1

# inversePyrmid(4)


# EXE1
# def findmin(lst):
#     result = lst[0]
#     for item in lst:
#         if item < result:
#             result = item
#     return result


# def mySort(lst):
#     result_list = []
#     while len(lst) > 0:
#         min_ele = findmin(lst)
#         result_list.append(min_ele)
#         myList.remove(min_ele)
#     return result_list
