import traceback

def calculate_average(array):
    try:
        if len(array) == 0:
            return 0
        return sum(array) / len(array)
    except Exception as e:
        traceback.print_exc()

def sum_odd_numbers(array):
    try:
        return sum(num for num in array if num % 2 != 0)
    except Exception as e:
        traceback.print_exc()

def sum_even_numbers(array):
    try:
        return sum(num for num in array if num % 2 == 0)
    except Exception as e:
        traceback.print_exc()

def sum_array(array):
    try:
        return sum(array)
    except Exception as e:
        traceback.print_exc()

def main():
    try:
        array = list(map(int, input("Enter the numbers separated by spaces: ").split()))
        print("Choose the operation:")
        print("1. Calculate average")
        print("2. Sum odd numbers")
        print("3. Sum even numbers")
        print("4. Sum entire array")
        operation = int(input("Enter the operation number: "))

        if operation == 1:
            print("Average:", calculate_average(array))
        elif operation == 2:
            print("Sum of odd numbers:", sum_odd_numbers(array))
        elif operation == 3:
            print("Sum of even numbers:", sum_even_numbers(array))
        elif operation == 4:
            print("Sum of entire array:", sum_array(array))
        else:
            print("Invalid operation")
    except Exception as e:
        traceback.print_exc()

# if __name__ == "__main__":
#     main()

import unittest

class TestArithmeticCalculator(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([10, 20, 30]), 20)
        self.assertEqual(calculate_average([]), 0)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers([1, 2, 3, 4, 5]), 9)
        self.assertEqual(sum_odd_numbers([10, 21, 30, 41]), 62)
        self.assertEqual(sum_odd_numbers([2, 4, 6]), 0)

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_even_numbers([10, 21, 30, 41]), 40)
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_sum_array(self):
        self.assertEqual(sum_array([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_array([10, 20, 30]), 60)
        self.assertEqual(sum_array([]), 0)

if __name__ == "__main__":
    unittest.main()