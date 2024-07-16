import time
import functools
import argparse

def timer_decorator(func):
    """
    Measures the execution time of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f} seconds")
        return result
    return wrapper

def main():
    parser = argparse.ArgumentParser(description="Measure execution time of a function")
    parser.add_argument("function", help="Name of the function to measure")
    parser.add_argument("--num-runs", type=int, default=1, help="Number of times to run the function")
    args = parser.parse_args()

    # Get the function from the module
    module = __import__("functions")
    func = getattr(module, args.function)

    # Apply the decorator to the function
    decorated_func = timer_decorator(func)

    # Run the decorated function
    for _ in range(args.num_runs):
        decorated_func()

if __name__ == "__main__":
    main()