# Problem:  given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers
# except for the element at that index.

# for example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2x3x4, 1x3x4, 1x2x4, 1x2x3]
# you can not use division in your answer.

#take a greedy approach and keep track of these results for later re-use
# consider when # is 0

# go through our list twice in a greedy fashion
# first loop, get the products of all the integers before each index
# second pass, we will go backwards to get the products of all the integers after each index.

# then we just need to multiply all the products before and after each index




def index_prod(lst):

	output = [None] * len(lst)        # complexity : O(n) space

	product = 1
	i = 0

	while i < len(lst):              # O(n) run time
		output[i] = product
		product *= lst[i]

		i += 1
	print(output)

	product = 1
	i = len(lst) - 1

	while i >= 0:
		output[i] *= product
		product *= lst[i]
		i -= 1

	return output

print(index_prod([1,2,3,4]))
