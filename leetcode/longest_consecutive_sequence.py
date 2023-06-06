class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        no_repetition = set(nums)
        answer = float("-inf")
        for i in no_repetition:
            current = i
            if current - 1 in no_repetition:
                continue

            count = 1
            j = 1
            while current + j in no_repetition:
                count += 1
                j += 1
            else:
                answer = max(count, answer)

        return answer