example = "Mr John Smith    "
length = 13

space = "%20"

result = ""
temp = example.strip()
for i in temp:
    if i != " ":
        result += i
    else:
        result += space

print(result)
