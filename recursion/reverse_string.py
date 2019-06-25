# reverse string using recursion.

def reverse(s):

    # base case
    if len(s) == 1:
        return s

    return s[-1]  +  reverse(s[:len(s)-1])



print(reverse("hello word"))