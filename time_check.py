import time


def timer(function):
    """
    Decorator to print function execution time in second and return value
    """
    def func(*args, **kwargs):
        start_time = time.time()
        return_value = function(*args, **kwargs)
        finish_time = time.time()
        print('Elapsed time:', finish_time - start_time)
        print('Answer:', return_value)
        return return_value
    return func
