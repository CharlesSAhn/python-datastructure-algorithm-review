# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
# its ok for 'AAB' to return 'A2B1'
# case sensitive

def compress(s):

    i = 0
    j = 0
    count = 0

    response = ""

    if len(s) == 0:
        return ""

    if len(s) == 1:
        return s + "1"

    while j < len(s):
        if s[i] == s[j]:
            count += 1
            j += 1
        else:
            response +=  s[i] + str(count)
            i = j
            count = 0

    response += s[i] + str(count)
    return response

print(compress("AAAABCCCCCDDEEEEF"))

