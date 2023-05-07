from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    value = list(count.items())
    sort_dict = lambda data : data[]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))