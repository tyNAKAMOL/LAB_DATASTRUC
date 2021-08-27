def palindrome(x):
    if len(x)==1:
        return True
    elif x[0] != x[-1]:
        return False
    else:
        return palindrome(x[1:-1])

inp = input()
if palindrome(inp):
    print("Palindrome")
else:
    print("Not Palindrome")