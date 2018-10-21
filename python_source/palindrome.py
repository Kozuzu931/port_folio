def palindrome(s):
    back=s[::-1]
    an=0
    if back==s:
        print(True)
        an=True
    else:
        print(False)
        an=False
    return an
