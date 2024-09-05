class Calculator:
    def __init__(self, array):
        self.array = array

    def calculate_average(self):
        return sum(self.array) / len(self.array)

    def sum_odd_numbers(self):
        return sum(num for num in self.array if num % 2 != 0)

    def sum_even_numbers(self):
        return sum(num for num in self.array if num % 2 == 0)

    def sum_entire_array(self):
        return sum(self.array)

import unittest

class TestCalculator(unittest.TestCase):
    def test_calculate_average(self):
        calculator = Calculator([1, 2, 3, 4, 5])
        self.assertEqual(calculator.calculate_average(), 3)

    def test_sum_odd_numbers(self):
        calculator = Calculator([1, 2, 3, 4, 5])
        self.assertEqual(calculator.sum_odd_numbers(), 9)

    def test_sum_even_numbers(self):
        calculator = Calculator([1, 2, 3, 4, 5])
        self.assertEqual(calculator.sum_even_numbers(), 6)

    def test_sum_entire_array(self):
        calculator = Calculator([1, 2, 3, 4, 5])
        self.assertEqual(calculator.sum_entire_array(), 15)

if __name__ == '__main__':
    unittest.main()
# test = [1, 2, 3, 4, 5]
# print(sum(test))
# print(sum(test)/len(test))
# odd = 0
# even = 0
# count_odd = 0
# count_even = 0
# for i in test:
#     if i % 2 ==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Even Sum {even} Odd sum {odd}")

def get_values_from_user():
    values = input("Enter the values (space-separated): ")
    return [int(value) for value in values.split()]

def get_operation_from_user():
    operation = input("Enter the operation (1 for average, 2 for sum odd, 3 for sum even, 4 for sum entire array): ")
    return int(operation)

def perform_operation(values, operation):
    calculator = Calculator(values)
    if operation == 1:
        return calculator.calculate_average()
    elif operation == 2:
        return calculator.sum_odd_numbers()
    elif operation == 3:
        return calculator.sum_even_numbers()
    elif operation == 4:
        return calculator.sum_entire_array()
    else:
        return "Invalid operation"

def main():
    values = get_values_from_user()
    operation = get_operation_from_user()
    result = perform_operation(values, operation)
    print(result)

if __name__ == '__main__':
    main()