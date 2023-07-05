def difference(x, y, z, p):
    r = 0
    for i in range(z):
        present = False
        for j in range(p):
            if x[i] == y[j]:
                present = True
                break
        if not present:
            r = 1
            print(x[i], end=" ")
    if r == 0:
        print("All numbers are present in the second array", end=" ")


# start
def st():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 1, 0, 5]
    m = len(a)
    n = len(b)
    difference(a, b, m, n)


st()
