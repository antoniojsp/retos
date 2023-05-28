import collections

first_bad = 45
end = 100
arr = [True if i >= first_bad else False for i in range(0,end)]
print(arr)

print(collections.Counter(arr))