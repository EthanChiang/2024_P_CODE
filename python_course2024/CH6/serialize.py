import pickle

# x=10
# y=[1,2,3,4]

# with open("pickle_file","wb") as p_file:
#      pickle.dump(x,p_file)
#      pickle.dump(y,p_file)

# with open("pickle_file","rb") as p_file:
#     print(pickle.load(p_file))
#     print(pickle.load(p_file))

# x= 10
# y=100
# my_list = [1,2,3,4,5,9]


# def save_data():
#     global x,y,my_list
#     data = {
#         "x":x ,"y":y ,"my_list":my_list
#     }
#     with open("my_pickle_file","wb") as pfile:
#         pickle.dump(data,pfile)

# save_data()

# x=None
# y=None
# my_list = None
# def restore_data():
#     global x,y,my_list
#     with open("my_pickle_file","rb") as pfile:
#         data=pickle.load(pfile)
#         x=data['x']
#         y=data['y']
#         my_list =data['my_list']

# restore_data()
# print(x,y,my_list)

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)