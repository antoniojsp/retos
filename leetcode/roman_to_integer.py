roman_numeral = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "M":1000
}

val = "III"


def romanToInt(s: str) -> int:
    convert = lambda x: roman_numeral[x]
    values = list(map(convert, s))
    answer = 0
    current = None
    prev = None
    while values:
        current = values.pop()
        if prev is None:
            prev = current
            answer +=current
            continue

        if prev == current:





    return answer

print(romanToInt("III"))