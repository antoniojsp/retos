test = 12321

def isPalindrome(nums):
    if nums < 0:
        return False
    temp = []
    while True:
        left = nums%10
        temp.append(left)
        nums = int(nums/10)
        if nums == 0:
            break

    return temp == list(reversed(temp))

print(isPalindrome(test))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         inverted_nums = []
#         while x != 0:
#             inverted_nums.append(x%10)
#             x = int(x/10)
#
#         return inverted_nums == list(reversed(inverted_nums))
