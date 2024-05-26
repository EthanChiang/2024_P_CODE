# def hello():
#     print("Hello from one.py")
#     print(__name__)


print("We are running one.py now")


def get_name():
    print(__name__)


if __name__ == '__main__':
    print("we are running one.py directly")
    get_name()
else:
    print("one.py is being imported")
    get_name()
