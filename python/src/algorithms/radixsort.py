def sort(arr: list):
    max_value = max(arr)
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
