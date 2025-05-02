

# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


class log_function_call:  # class which accept function
    def __init__(self ,func):
        self.func = func

    def __call__(self, *args, **kwds):  # method override when function call first print the run original function
        print("Function is being called")
        return self.func(*args , **kwds)
    
@log_function_call   # function wrap by this decorator class
def say_hello():
    print("Hello!")


say_hello()