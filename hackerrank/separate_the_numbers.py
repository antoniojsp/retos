
def separateNumbers(s):
    # Write your code here
    for i in range(len(s)//2):
        val = int(s[:i+1])
        repeat = len(s)//(i+1)
        temp = []
        for i in range(repeat):
            temp.append(str(val))
            val+=1
            if len(temp) > len(s):
                break
        candidate = "".join(temp)
        if candidate.startswith(s):
            print(f"YES {temp[0]}")
            return

    print("NO")

test = "1234"
separateNumbers(test)