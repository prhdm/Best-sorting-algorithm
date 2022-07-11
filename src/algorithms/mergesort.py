def sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = sort(list[:mid])
    right = sort(list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
