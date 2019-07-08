# Given an integer array, output all the unique pairs that sum up to a specific value k
# Ex:

#  pair_sum([1,2,3,4], 4)
# Return: (1,3), (2,2)

def pair_sum(num_list, k):

    pair_counter = 0
    used_number = []

    for digit in num_list:
        if k - digit in num_list and digit not in used_number:
            pair_counter += 1
            used_number.append(k - digit)

    return pair_counter

def pair_sum2(arr, k):

    if len(arr) < 2:
        return

    # sets for tracking
    # set: a collection which is unordered and unindexed.    set = {"apple", "banana"}  set.add("orange") or set(["apple"])
    # sets cannot have multiple occurrence of the same element
    seen = set()
    output = set()

    for num in arr:

        target = k - num

        print(num)

        if target not in seen and target != num:
            seen.add(num)
        
        else:
            output.add( (  min(num, target) , max(num,target) ) )

    #return len(output)

    return '\n'.join(map(str, list(output)))


print(pair_sum2([1,2,3,4], 4))
