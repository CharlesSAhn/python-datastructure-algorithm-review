# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
# input s="abc" ->   ['abc', 'acb', 'bac', 'bca', .......]
# if character is repeated, treat them as distinct character.

def permuation(s):

    out = []

    #base case
    if len(s) == 1:
        out[s]

    else:
        # for every letter in string
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3

            for perm in permuation(s[:1] + s[i+1:]):
                out += [let+perm]

    return out



print(permuation('abc'))