
def or_operation_ones(bin1:str, bin2:str):
    suma = 0
    or_bin = bin(int(bin1, 2) | int(bin2, 2))[2:]
    for i in or_bin:
        suma += int(i)
    return suma

a = [
"11101",
"10101",
"11001",
"10111",
"10000",
"01110"]


def max_pairs(arr:list):
    maximo = 0
    results = {}
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            subjects = or_operation_ones(arr[i], arr[j])
            maximo = max(int(subjects), maximo)
            if subjects in results:
                results[subjects] += 1
            else:
                results[subjects] = 1

    return [maximo, results[maximo]]

print(max_pairs(a))


