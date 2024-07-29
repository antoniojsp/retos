text =  ['abc', 'def', 'abc', 'def', 'a', 'h', 'dfdfd', 'dfdfd', 'abc', 'dfdfd', 'dfdfd']
count = {}

for i in text:
    count[i] = count.get(i, 0) + 1

count = list(count.items())
count = sorted(count, key=lambda x:x[1], reverse=True)[:3]

print(count)