def pairs(a, n, sm):
    count = []  # Initialize result
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] + a[j] == sm:
                count.append([a[i], a[j]])
                break
    print("Pairs for the sum of ", sm, "is", count)


# start
def st():
    arr = [1, 5, 7, -1, 5]
    lt = len(arr)
    print(arr)
    s = input("Enter the sum to find the pairs : ")
    s = int(s)
    pairs(arr, lt, s)


st()
