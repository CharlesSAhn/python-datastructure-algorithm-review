# Given a list of objects, return the object that occurs most frequently and the object that occurs
# second most frequently

def frequentlyshownobject(lst):

	counter = {}

	for item in lst:
		if item is not counter:
			counter[item] = 1
		else:
			counter[item] += 1

	findHighest(counter)


def findHighest(dic):
	highest_item = None
	highest_count = 0

	secondhighest_item = None
	secondhighest_count = 0

	for key in dic:
		if dic[key] > highest_count:
			highest_item = key
			highest_count = dic[key]

	dic.remove[highest_item]

	for key in dic:
		if dic[key] > secondhighest_count:
			secondhighest_item = key
			secondhighest_count = dic[key]

	return (highest_item, secondhighest_item)




