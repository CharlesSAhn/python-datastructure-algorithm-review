

# if n =4, return 4+3+2+1 = 10

def rec_sum(n):

    if n < 1:
        return n

    return rec_sum(n-1) + n


print(rec_sum(4))



# if n = 4321, return 4+3+2+1
def sum_func(n):
    if len(str(1)) == 1:
        return n

    return sum_func(int(n/10)) + n % 10

print(sum_func(65654))



def word_split(phrase, list_of_words, output = None):

    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    return output



print(word_split("themanran", ['the', 'ran', 'man']))