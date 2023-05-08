#https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter

# binary = lambda x: format(1<<x, '08b')

def topKFrequent(nums, k):
    count = dict(Counter(nums))
    sort_dict = lambda x: x[1]
    ordered = list(sorted(count.items(), key=sort_dict, reverse=True))[:k]
    return [i[0] for i in ordered]




nums = [-1,-1]
k = 1
print(topKFrequent(nums, k))
