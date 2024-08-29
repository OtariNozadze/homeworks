import time

def decorator(func):
    def time_calculator(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        result = time_end - time_start
        print(f"This Function Took {result} Seconds")
        return result
    return time_calculator

@decorator
def function():
    for i in range(2000000):
        pass

function()


    
