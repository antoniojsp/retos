def separateNumbers(s):
    # Write your code here
    result = ""
    for i in range(len(s) // 2):
        val = int(s[:i + 1])
        repeat = len(s) // (i + 1)
        candidate = ""
        start = ""
        for j in range(repeat):
            if j == 0:
                start = str(val)
            candidate +=str(val)
            val += 1

        if candidate.startswith(s):
            result = f"YES {start}"
            break

    if result:
        print(result)
    else:
        print("NO")


test = "101103"
separateNumbers(test)