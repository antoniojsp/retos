n = 4
def magic_square(n):
    n *= 2
    for i in range(0,n):
        for j in range(0, n):
            print("[", i,",", j, "]", end=" ")
        print()
    print("\n"*2)

magic_square(1)
magic_square(2)
magic_square(3)
