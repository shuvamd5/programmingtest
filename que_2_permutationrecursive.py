def permute(pr, lf, rt):
    if lf == rt:
        print(''.join(pr))
    else:
        for i in range(lf, rt):
            pr[lf], pr[i] = pr[i], pr[lf]
            permute(pr, lf+1, rt)
            pr[lf], pr[i] = pr[i], pr[lf]


# start
def st():
    string = input("Enter string : ")
    n = len(string)
    pr = list(string)
    # call
    if n == 0:
        print("No string entered ")
    else:
        permute(pr, 0, n)


st()
