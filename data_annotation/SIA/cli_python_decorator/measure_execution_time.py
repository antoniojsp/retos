import argparse
import time
from functools import wraps

# Define the decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time} seconds.")
        return result
    return wrapper

# Define some example functions to test the decorator
def example_function1():
    time.sleep(1)  # Simulate some work

def example_function2():
    time.sleep(2)  # Simulate some work

# Map function names to their corresponding functions
function_map = {
    "example_function1": example_function1,
    "example_function2": example_function2,
}

# CLI interface using argparse
parser = argparse.ArgumentParser(description="Measure execution time of functions.")
parser.add_argument("-f", "--function", type=str, help="Name of the function to measure execution time.", required=True)
args = parser.parse_args()

# Get the function from the function map
func = function_map.get(args.function)

if func is None:
    print(f"Error: Function '{args.function}' not found.")
else:
    # Apply the decorator to the function and execute it
    decorated_func = timing_decorator(func)
    decorated_func()