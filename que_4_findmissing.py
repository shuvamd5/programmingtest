import random
import math


def missing(a, n):
    # method 1
    for i in range(0, n):
        if a[i] != i+1:
            ans = i+1
            print("The missing number from an array of 1-100 is", ans, "method 1")
            break

    # method 2
    r = 0
    p = math.floor((3*n)/4)
    while r == 0:
        if a[p] == p+1:
            for i in range(p, n):
                if a[i] != i + 1:
                    ans = i + 1
                    print("The missing number from an array of 1-100 is", ans, "method 2")
                    r = 1
                    break
        else:
            p = p - math.floor(n/4)


# start
def st():
    arr = []
    for i in range(1, 101):
        arr.append(i)
    # choose a random number from the array
    x = random.choice(arr)
    # remove the chosen random number from the array
    arr.remove(x)
    print("The array have number from 1-100 with one number missing in random.")
    missing(arr, 99)


st()
