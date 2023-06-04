def start_end_decorator(func):

    def wrapper(*args, **kwargs): #*args 不指名的參數 **kwargs 指名的參數 兩者概括全部
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(add5(10))