

def convert_to_base(num:int, base:int) -> str:

    result = []
    while num >= 1:
        result.append(num%base)
        num//=base

    return "".join([str(i) for i in result[::-1]])

print(convert_to_base(100, 3))


