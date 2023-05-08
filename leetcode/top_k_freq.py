from collections import Counter

def topKFrequent(nums, k):
    count = dict(Counter(nums))
    # value = list(count.items())
    print(count)
    result = sorted(count.items(), key=lambda x:x[0])[:k]
    print(result)

    return [i[1] for i in result]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

