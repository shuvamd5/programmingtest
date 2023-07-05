def duplicates(a, b):
    present = False

    # ArrayList to store the output
    dp = []
    for i in range(b - 1):
        for j in range(i + 1, b):

            if a[i] == a[j]:
                if a[i] in dp:
                    break

                else:
                    dp.append(a[i])
                    present = True

    if present:
        print(dp)
    else:
        print("No duplicates present in arrays")
    sf()


# function
def sf():
    arr = []
    i = 1
    while i != 0:
        x = input("Enter number : ")
        arr.append(x)
        i = int(x)
    n = len(arr)
    duplicates(arr, n)


# start
def st():
    print("Enter number between 1 to 100 to store in array")
    print("Number can be repeated to find duplicate number present in array")
    print("Press 0 to start finding")
    sf()


st()
