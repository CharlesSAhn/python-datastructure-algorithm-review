# Given a string of opening and closing parantheses, check whether it is balanced.  We have 3 types of parantheses: round brackets (),
# square brackets [], and curly brackets {}.  Assume that the string doesn't contain any other character than these, no spaces words or numbers.


def balanced_check(s):

    if len(s) % 2 != 0:
        return False

    opening = set('([{')    # { '(', '[', '{' }

    matches = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if matches[last_open] != paren:
                return False

    return len(stack) == 0

print(balanced_check("{{}}"))
print(balanced_check("{{[()]}}"))
print(balanced_check("{{[)]}}"))