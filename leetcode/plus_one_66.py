test = [9]

from typing import List
class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1,-1):

            #if lest significant digit is from 0 to 8, then adding 1 won't have a carry value
            if digits[i] < 9:
                digits[i] +=1
                break
            else:
                #if LSD is 9, then value is carried to the digit on the left.
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)

        return digits

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     for i in range(len(digits)-1, -1,-1):
    #         temp = digits[i] + 1
    #
    #         #if lest significant digit is from 0 to 8, then adding 1 won't have a carry value
    #         if temp < 10:
    #             digits[i] = temp
    #             break
    #         #if LSD is 9, then value is carried to the digit on the left.
    #         digits[i] = 0
    #         if digits[0] == 0 and i == 0:
    #             digits = [1] + digits
    #
    #     return digits




a = Solution()
print(a.plusOne(test))