import math


def iterative(pr, lf, rt, pt):
    x = rt-1
    for i in range(lf, pt):
        if lf == x:
            print(''.join(pr))
            pr[lf], pr[rt] = pr[rt], pr[lf]
            x = rt-1
        else:
            print(''.join(pr))
            pr[x], pr[rt] = pr[rt], pr[x]
            x -= 1
    st()


# start
def st():
    string = input("Enter string : ")
    n = len(string)
    q = math.factorial(n)
    n = n-1
    pr = list(string)
    # call
    iterative(pr, 0, n, q)


st()
