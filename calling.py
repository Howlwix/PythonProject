def already_called(func):
    func.already_in_called = False
    def wrapper():
        if not func.already_in_called:
           func.already_in_called = True
           return func()
        else:
            print("already in call")
    return wrapper
@already_called
def initialize():
    print("calling")
initialize()
initialize()
initialize()
