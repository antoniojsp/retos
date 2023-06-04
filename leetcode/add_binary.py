

def add_zeros(bin_number, length):
    pad = "0" * (length-len(bin_number))
    return f"{pad}{bin_number}"
def addBinary(a, b):
    bin_a = list(a)
    bin_b = list(b)

    shortest, longest = (bin_a, bin_b) if len(b) >= len(a) else (bin_b, bin_a)
    print(longest)

print(addBinary(a = "11", b = "11111"))
