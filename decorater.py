def say_hello():
    print("hello")
def decorater(func):
    def wrapper():
        print("*********")
        func()
        print("*********")
    return wrapper
say_hello = decorater(say_hello)
say_hello()