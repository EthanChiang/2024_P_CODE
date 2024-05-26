# def safe_divide_2(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         print("divide by 0 attemmpt detected")
#         return None

# def save_a_file():
#     result = save_prefs()
#     if result =="error":
#        print("Preference not saved")
#        return
#     if result =="error":
#        print("Not enough memory")
#        return
#     result = save_format()
#     if result =="error":
#         print("format not saved.")
#         return


# def save_a_file():
#     try:
#       save_prefs()
#       save_text()
#       save_format()
#     except:
#       print("something went wrong...")