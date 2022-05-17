def two_sum(arr: list, target: int) -> list:
    # visited = []
    for index, value in enumerate(a):
        # visited.append(index)
        reach_target = target - value
        # for i in range(0, len(a)):
        #     if i not in visited:
        #         if a[i] == diff:
        #             return [index, i]
        for i in range(index+1, len(a)):
            if reach_target in arr[i:]:
                return [index, i]
    return []


a = [3, 2, 4]
suma = 6
print(two_sum(a, suma))