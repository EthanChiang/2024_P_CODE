# import one

# one.hello()
# print(__name__)


import one

print("We are running two.py now")


def get_name():
    print(__name__)


if __name__ == '__main__':
    print("we are running two.py directly")
    get_name()
    one.get_name()
