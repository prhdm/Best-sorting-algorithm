def sort(arr):
    max_digit = max(arr)
    digit = 1
    while max_digit // digit > 0:
        buckets = [[] for _ in range(10)]
        for i in arr:
            buckets[i // digit % 10].append(i)
        arr = []
        for i in buckets:
            arr.extend(i)
        digit *= 10
    return arr
