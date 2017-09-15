from sorting import mergeSort

def binarySearch(array, targval):
    """
    Performs binary search.
    """
    L, R = 0, len(array) - 1
    while True:
        m = (L+R) // 2
        if array[m] < targval:
            L = m + 1
            continue 
        if array[m] > targval:
            R = m - 1
            continue
        break
    return m

userarray = input("Enter a series of numbers, divided by space, to have it "
    "sorted, then have a binary search performed.\n")
userarray = userarray.split(" ")
for i in range(len(userarray)):
    userarray[i] = int(userarray[i])
if len(userarray) > 1:
    uservalue = int(input("\nNow enter a value to search its index.\n"))
    userarray = mergeSort(userarray)
    print("\nAfter sorting, first occurence of element " + str(uservalue) + 
        " has index of " + str(binarySearch(userarray, uservalue)) + 
        ": " + str(userarray))
else:
    print("Not enough elements in the array.\n")
input("Press Enter to close the program.")