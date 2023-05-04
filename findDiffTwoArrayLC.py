# https://leetcode.com/problems/find-the-difference-of-two-arrays/

nums1 = [1,2,3]
nums2 = [2,4,6]

def contar(arr:list):
    temp = {}

    for i in arr:
        if i not in temp:
            temp[i] = 0

    return temp


a = contar(nums1)
b = contar(nums2)

result1 = {}
result2 = {}
for i in nums1:
    if str(i) not in a:
        result1[i] = 0

for j in nums2:
    if j not in b:
        result2[j] = 0


print([result1, result2])

# def findDifference(nums1: list[int], nums2: list[int]):
#     a = []
#     b = []
#
#     for i in nums1:
#         if i not in nums2 and i not in a:
#             a.append(i)
#     for j in nums2:
#         if j not in nums1 and j not in b:
#             b.append(j)
#
#     return [a,b]
#
#
# print(findDifference(nums1, nums2))
#

