n = 7
for i in range(1,n):
    for j in range(1,n * 2):
        if j > n - i and j < n + i:
            if (j + i) % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print("")
