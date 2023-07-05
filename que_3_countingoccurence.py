def count(s, c):
    res = 0

    for i in range(len(s)):
        # Checking
        if s[i] == c:
            res = res + 1

    if res == 0:
        print("No match found ")
        print("Choose another character to find ")
        st()
    else:
        print("The number of occurrence of " + c + " is : ")
        print(res)
        st()


# start
def st():
    string = input("Enter string : ")
    ct = input("Character to count : ")
    # call
    count(string, ct)


st()
