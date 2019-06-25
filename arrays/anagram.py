# Anagram: when two strings can be written using the exact same letter
# Ignore spaces and capitalization

#Ex: "public relations" - "crap built on lies."

def anagrams2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    return  sorted(s1) == sorted(s2)


def anagrams(s1, s2):

    if s1 is None or s2 is None:
        return False

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}


    for char in s1:

        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in s2:

        if char in count:
            count[char] -= 1
        else:
            return False

        if count[char] < 0:
            return False

    for key in count:
        if count[key] > 0:
            return False

    return True




print(anagrams("god", "god"))
print(anagrams("public relations", "crap built on lies"))
print(anagrams("", None))
print(anagrams("DOG", "god"))

print(anagrams2("god", "god"))
print(anagrams2("public relations", "crap built on lies"))
#print(anagrams2("", None))
print(anagrams2("DOG", "god"))

