roman_numeral = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

def romanToInt(s: str) -> int:
    values = list(map(lambda x: roman_numeral[x], s))
    starting_value = values.pop()
    answer = starting_value
    prev = starting_value
    while values:
        current = values.pop()
        if prev == current or answer < current:
            answer += current
        else:
            answer -= current
        prev = current

    return answer

val = "DCXXI"


print(romanToInt(val))
print(romanToInt("III"))