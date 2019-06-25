# Given a string, determine if it is comprised of all unique characters.  For ex, the string 'abcde' has all unique characters and
# should return True.  The string 'aaabcde' contains duplicate characters and return false.


def unique_string(s):

    dic = {}

    for char in s:
        if char in dic:
            return False
        else:
            dic[char] = True

    return True

def unique_string2(s):
    return len(set(s)) == len(s)


print(unique_string("abcde"))
print(unique_string("abacde"))


