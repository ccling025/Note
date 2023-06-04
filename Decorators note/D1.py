def start_end_decorator(func):

    def wrapper():
        print("start")
        func()
        print("end")
    
    print(type(wrapper))
    return wrapper #回傳此函式

@start_end_decorator
def print_name():
    print("XD")

print_name()

