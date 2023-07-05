def palindrome(p):
    n = len(p)  # string length
    if n == 0:
        print("No string entered")
        st()
    if n < 2:
        return n
    start = 0
    ml = 1
    for i in range(n):
        low = i - 1
        high = i + 1
        while high < n and p[high] == p[i]:
            high = high + 1

        while low >= 0 and p[low] == p[i]:
            low = low - 1

        while low >= 0 and high < n and p[low] == p[high]:
            low = low - 1
            high = high + 1

        length = high - low - 1
        if ml < length:
            ml = length
            start = low + 1

    print("The Longest palindrome substring is: ")
    print(p[start: start + ml])
    print("and the Length is: ")
    print(ml)
    st()


# starting function
def st():
    string = input("Enter a String to check palindrome : ")
    palindrome(string)


st()
