prices = [7,5,5,1,36,34]
left, right, maximo = 0,1,0
#maximum profit
while right < len(prices):
    if prices[left] < prices[right]:
        suma = prices[right] - prices[left]
        maximo  = max(maximo, suma)
    else:
        left = right

    right +=1

print(maximo)






# a = "geeksforgeeks"
# s = 3
# unique = set()
# length = 0
# maximo = 0
# for i in a:
#     if i not in unique:
#         length +=1
#     else:
#         maximo = max(maximo, length)
#         length = 1
#         unique = set()
#
#     unique.add(i)
#
# print(maximo)
#







# a = [100,23,300,24,5,200]
# k = 2
#
# sum_temp = sum(a[:k])
# max_sum = sum_temp
# for i in  range(len(a)-k):
#     print(sum_temp, a[i], a[i+k])
#     sum_temp = sum_temp - a[i] + a[i+k]
#     max_sum =  max(sum_temp, max_sum)
#
# print(max_sum)