# Give a string of words, reverse all the words
# Ex: 'Given is the best' -> 'best the is This'
# remove all leading and trailing white space


def rev_word(s):
    s = s.strip()
    s_list = s.split(" ")
    s_list.reverse()

    return " ".join(s_list)

def rev_word2(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:

        if  s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1

            words.append(s[word_start: i])

        i += 1

    return " ".join(reversed(words))



print(rev_word2('Hi John, how are you?'))
print(rev_word2('   Hi John, how are you?'))