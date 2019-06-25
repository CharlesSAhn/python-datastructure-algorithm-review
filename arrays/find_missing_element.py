# Consider an array of non-negative integers.  A second array is formed by shuffling the elements of the first and
# deleting a random element. Give these two arrays, find which element is missing in the second array.

# Ex. input:  finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
              # 5 is missing.



def finder(array1, array2):
    # if len(array1) - len(array2) != 1:
    #     return -1

    tracker = {}


    for num in array1:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1


    for num in array2:
        if num in tracker:
            tracker[num] -= 1
        else:
            return num

    for key in tracker:
        if tracker[key] > 0:
            return key





# nlogn
def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    #zip->   zip([1,2,3], [4,5,6])  -> [(1,4), (2,5), (3,6)]
    for num1, num2 in zip(arr1, arr2):

        if num1 != num2:
            return num1

    return arr1[-1]



print(finder([1,2,3,3,5,6,7, 4], [3,5,7,2,1,4,6]))

