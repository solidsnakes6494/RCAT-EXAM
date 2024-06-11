import time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end= time.time()
        execution_time = end - start
        print("The execution time is ",execution_time)
        return result
    return wrapper

# Example usage:
@log_execution_time
def example_function():
    # Some time-consuming operation
    time.sleep(2)
    print("Function executed")

example_function()
"""
OUTPUT
Function executed
The execution time is  2.0468010902404785
"""
