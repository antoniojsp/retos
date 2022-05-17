string_example = "antonio"
string_example2 = "abba"
string_example3 = "mario"


def is_unique(string: str) -> bool:
    abc = {}
    for i in string:
        if i not in abc:
            abc[i] = 1
        else:
            return False
    return True


print(is_unique(string_example))
print(is_unique(string_example2))
print(is_unique(string_example3))
print()


def is_unique_2(string: str) -> bool:
    lista = list(string)
    lista.sort()
    for i in range(0,len(lista)-1):
        if lista[i] == lista[i+1]:
            return False

    return True


print(is_unique_2(string_example))
print(is_unique_2(string_example2))
print(is_unique_2(string_example3))