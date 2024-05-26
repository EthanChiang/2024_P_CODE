import except3


try:
    num = "-55"
    except3.enter_age(num)
except except3.NegativeNumberException as error:
    print(error)

except:
    print("Something Ww dont know went wrong...")
