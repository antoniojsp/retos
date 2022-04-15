def strings_xor(s, t):
    res = ""
    for i, j in zip(s, t):
        if i != j:
            res = '1'
        else:
            res = '0'

    return res

print(strings_xor('10000', '01100'))

