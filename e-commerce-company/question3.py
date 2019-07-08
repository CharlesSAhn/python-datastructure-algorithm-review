# Given two rectangles, determine if they overlap. The rectangles are defined as a dictionary.

r1 = {
	'x': 2, 'y': 4,
	'w': 5, 'h': 12
}

r2 = {
	'x': 5, 'y': 8,
	'w': 5, 'h': 10
}


# break it up to sub-problems.  We can split up the problem into an x-axis problem and y-axis problem.
# create a function that can detect overlap in 1 dimension.

def overlap(coor1, dim1, coor2, dim2):

	greater  = max(coor1, coor2)
	lower = min(coor1 + dim1, coor2 + dim2)

	if greater >= lower:
		return (None, None)

	overlap = lower-greater

	return (greater, overlap)


def calc_rect_overlap(r1, r2):

	x_overlap, w_overlap = overlap(r1['x'], r1['w'], r2['x'], r2['w'])

	y_overlap, h_overlap = overlap(r1['y'], r1['h'], r2['y'], r2['h'])

	if not w_overlap or not h_overlap:
		print('no overlap')
		return None

	return {'x': x_overlap, 'y': y_overlap, 'w': w_overlap, 'h': h_overlap}

print(calc_rect_overlap(r1, r2))