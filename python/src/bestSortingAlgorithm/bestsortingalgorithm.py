from math import log


def pyme(array: list):
    """
    This function is the implementation of the algorithm.
    It takes an array as input and returns the best sorting algorithm.
    """
    """
    The complexity of this algorithm is O(n log n).
    we can improve the algorithm by using the following optimizations:
    1. We can ignore the inversions because we use it for determining the best sorting algorithm on small arrays
    and we can ignore it for large arrays.
    2. because we use the max_value and max_number_of_digits to determine the best sorting algorithm for arrays with
    no negative numbers, we can ignore them for arrays with negative numbers and we can just find 
    the max number of digits by the number that has the max value.
    """
    is_asc, is_desc, has_negative, max_value, max_number_of_digits = __analyse(array)  # Analyse the array for
    # finding attributes of the array
    inversions = inversion_count(array)  # Count the inversions for Insertion Sort
    n_log_n = len(array) * log(len(array), 2)  # Calculate the n log n
    if inversions < n_log_n or (is_asc == len(array) - 1 and is_desc == len(array) - 1) or \
            20 >= len(array) > 1 or is_asc == len(array) - 1:
        return "Insertion Sort"  # If the inversions are less than n log n or
        # the array is sorted in ascending order or if the array is small or all keys are the same we use Insertion Sort
    if is_desc == len(array) - 1:
        return "Merge Sort"  # If the array is sorted in descending order we use Merge Sort
        # by test, it works better than others
    if not has_negative:  # count sort and radix sort can only be used if the array has no negative numbers
        if max_number_of_digits < log(len(array), 2) and max_number_of_digits * len(array) < max_value + len(array) \
                and max_number_of_digits * len(array) < n_log_n / 2:
            return "Radix Sort"  # for the array with bigger rang than linear and the number of digits is smaller
            # than the biggest number of the array we use Radix Sort
        if max_value < len(array) * log(len(array), 2):
            return "Count Sort"  # if the max value is small count sort is better than radix sort
    if is_asc < len(array) * 3 / 5 and is_desc < len(array) * 3 / 5:
        return "Quick Sort"  # Quick Sort is better than Merge Sort for arrays with a lot of inversions
        # and if the array is sorted in ascending order and descending order we use other sorts.
        # it works better on big arrays.
    else:
        return "Merge Sort"
        # merge sort needs more space than quick sort and merge is better for small arrays.
        # merge sort need to copy array every time and quick sort need to copy array only once.
    # we didn't use heap sort because it is slower than merge sort and quick sort
    # bubble sort is just a simple sorting algorithm that doesn't use any optimizations.
    # bubble sort is easier to understand and it is just handy to use but by test it works slower than Insertion.


def __analyse(array):
    is_asc, is_desc, has_negative, max_value, max_number_of_digits = 0, 0, False, 0, 0
    temp_asc = 0
    temp_desc = 0
    for i in range(len(array) - 1):
        if array[i] < 0:
            has_negative = True
        if array[i] >= array[i + 1]:
            temp_asc = max(temp_asc, is_asc)
            is_desc = temp_desc + 1
        else:
            temp_asc = temp_asc + 1
            is_desc = max(temp_desc, is_desc)
        max_value = max(array[i], max_value)
        max_number_of_digits = max(len(str(array[i])), max_number_of_digits)
    is_asc = max(is_asc, temp_asc)
    is_desc = max(is_desc, temp_desc)
    max_value = max(array[len(array) - 1], max_value)
    max_number_of_digits = max(len(str(array[len(array) - 1])), max_number_of_digits)
    return is_asc, is_desc, has_negative, max_value, max_number_of_digits


def inversion_count(array):
    """
    This function is the implementation of the inversion algorithm.
    It takes an array as input and returns the number of inversions.
    """
    if len(array) <= 1:
        return 0
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return inversion_count(left) + inversion_count(right) + merge(left, right)


def merge(left, right):
    count = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            i += 1
        else:
            count += len(left) - i
            j += 1
    return count
