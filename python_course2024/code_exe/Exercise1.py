# def printMany():
#     for i in range(1,6):
#           print(f"# {i} \n")
    

# printMany()

# def printEvery3():
#     for i in range(1,89,3):
#        print(i)

# printEvery3()


#exe2
# def position(words):
#     count =0
#     for item in words:
#         # print("item:",item)
#         if item.upper() == item:
#             return (item,count)
#         count+=1    
#     return -1

# def position(string):
#     for num,s in enumerate(string):
#         if s == s.upper():
#             return(s,num)
#     return -1



# print(position("abCD"))


# exe3
# def findSmallCount(List1,int1):
#     count =0
#     for item in List1:
#         if item < int1:
#             count+=1

#     return count


# print(findSmallCount([1,2,2,7],4))    
# print(findSmallCount([1,2,3,4,5],0))        

# exe4
# def findSmallTotal(List1,int1):
#     sum =0
#     for item in List1:
#         if item < int1:
#             sum+=item

#     return sum

# print(findSmallTotal([1,2,2,7],4))    
# print(findSmallTotal([1,2,3,4,5],0)) 

# exe6
# def findAllSmall(List1,int1):
#     result =[]
#     for item in List1:
#         if item < int1:
#             result.append(item)

#     return result   

# print(findAllSmall([1,2,2,7],4))    
# print(findAllSmall([1,2,3,4,5],10)) 

#exe 7 
# def summ(list1):
#     sum = 0
#     for i in list1:
#         sum+=i

#     return sum

# print(summ([-10,-20,-30]))      

# Simple Exe 2
# def stars(nums):
#     for i in range(1,nums+1):
#         print("*"*i)
#         # for j in range(i+1):          
#         #   print("*")
#         # # print("\n")

# stars(4)

def stars(nums):
    for i in range(1,nums+1):
        print("*"*i)
    for i in range(nums-1,0,-1):
        print("*"*i)    


stars(4)

# def table (n):
#     for i in range(1,10,1):
#         print(f"{n}x{i}={n*i}")

# table(3)

# def table9to9():
#        for i in range(1,10,1):
#          for j in range(1,10,1):
#              print(f"{i}X{j}={i*j}")   

# table9to9()

# def swap(string):
#       result=""
#       for item in string:
#           if item.upper() == item:
#               result = result + item.lower()
#           else:
#               result = result + item.upper()
#             #   print(f"{item.upper()}")

#       return result

# print(swap("alOGHha.")) 

# def findMin(list_num):
#      if list_num == []:
#        return "underfined"
#      min=list_num[0]
#      for item in list_num:
#          if item < min:
#               min=item
#      return min

# print(findMin([1, 6, 0, 33, 44, 88, -10]))               