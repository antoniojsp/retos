def digits_to_num(self, digits):
    result = 0
    for digit in digits:
        result = result * 10 + digit
    return result


# Assuming this is part of a function that takes `num` as input
if num < 10:
    return num

# Convert the number to a list of digits
digits = [int(char) for char in str(num)]
max_digit = max(digits)

# Check if the maximum digit is the first digit
if max_digit != digits[0]:
    # Use `reversed()` to iterate through the digits in reverse order
    for i, digit in enumerate(reversed(digits)):
        # Your logic for processing each digit here
        print(f"Index in reverse: {i}, Digit: {digit}")

