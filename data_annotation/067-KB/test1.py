with open("log.txt", "r") as file:
    w = file.read().split(" ")
    words = set(w)

print(words)