#reverse name

a  = "Antonio"
result = ""
for i in a:
    result = i + result

print(result)

a = list("Antonio")
for i in range(len(a)//2):
    a[len(a)-i-1], a[i] = a[i], a[len(a)-i-1]

print(a)

