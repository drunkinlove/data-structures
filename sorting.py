def merge(leftarr, rightarr):
    """
    Implements merging arrays, which is a subroutine for merge sorting.
    We continuously check the first items of subarrays and add the smaller
    item to the bigger array. Then, we add leftovers if there are any.
    """
    array = []
    while len(leftarr) != 0 and len(rightarr) != 0:
        if leftarr[0] < rightarr[0]:
            array.append(leftarr[0])
            del leftarr[0]
        else:
            array.append(rightarr[0])
            del rightarr[0]
    if len(leftarr) == 0:
        array += rightarr
    else:
        array += leftarr
    return array

def mergeSort(array):
    """
    The body of merge sorting algorithm, which starts with dividing the array
    into two parts, recursively, until we have broken the array down into
    separate elements, which then become sorted pairs, which in turn become 
    our sorted array. Thank you, John von Neumann.

    Also added two print commands that make the process a little more visual.
    """
    if len(array) < 2:
        return array
    else:
        midpoint = len(array) // 2
        a = mergeSort(array[:midpoint])
        b = mergeSort(array[midpoint:])
    return merge(a, b)
