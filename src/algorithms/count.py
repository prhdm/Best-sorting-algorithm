def getMax(arr):
    """
    Get max value in array
    """
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

def sort(arr):
    """
    Count sort algorithm
    """
    max_value = getMax(arr)
    count = [0] * (max_value + 1)
    for i in arr:
        count[i] += 1
    i = 0
    for j in range(len(count)):
        while count[j] > 0:
            arr[i] = j
            i += 1
            count[j] -= 1
    return arr

    