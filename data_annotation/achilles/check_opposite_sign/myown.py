
def check_opposite_signs(num:tuple) -> bool:

    if num[0] < 0 and num[1] > 0 or num[0] > 0 and num[1] < 0:
        return True

    return False


print(check_opposite_signs((-1,2)))