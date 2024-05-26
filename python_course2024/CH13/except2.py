# try:
#    f=open("testfile.txt")
#    f.write("Write a test line")
# except TypeError:
#    print("There is a type error")
# except OSError:
#    print("Tere is an OS Error")
# except:
#    print("Whatever other errors will go here")
# finally:
#    print("this will run no matter what")

def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here: "))
        except:
            print("Invalid number. please try again")
        else:
            print("Good Job")
            return result


ask_for_int()
