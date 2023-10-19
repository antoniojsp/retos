nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

listas = {"nums1":sorted(nums1), "nums2":sorted(nums2)}

if len(nums1) <= len(nums2):
    shortest, longest = listas["nums1"], listas["nums2"]
else:
    shortest, longest = listas["nums2"], listas["nums1"]
result = []
j = 0
for i in range(len(shortest)):

    while j < len(longest):
        if shortest[i] == longest[j]:
            result.append(shortest[i])
            j+=1
            break
        j+=1

print(result)