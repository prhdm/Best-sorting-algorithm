from math import log
from statistics import mean

is_asc = 0
is_desc = 0
has_negative = False
max_value = 0
max_number_of_digits = 0
def pyme(array:list):
    """
    This function is the main function of the program.
    It takes an array as input and returns the sorted array.
    """
    global is_asc, is_desc, has_negative, max_value, max_number_of_digits
    inversions = inversionCount(array)
    __persistData(array)
    if inversions < len(array)*log(len(array), 2) or  is_asc+1 == len(array) and is_desc+1 == len(array) or len(array) <= 20 and len(array) > 1:
        return "Insertion Sort"
    elif is_desc+1 == len(array):
        return "Merge Sort"
    elif is_asc+1 == len(array):
        return "Insertion Sort"
    elif not has_negative:
        print(max_value/len(array))
        if max_number_of_digits < log(len(array)) and max_number_of_digits*len(array) < max_value + 3*len(array):
            print(max_number_of_digits, log(len(array), 2))
            return "Radix Sort"
            
        if max_value < len(array)*log(len(array), 2):
            print(max_value, len(array))
            return "Count Sort"

        
    if is_asc < len(array) and is_desc < len(array):
            return "Quick Sort"
    else:
        return "Merge Sort"      
    
def __persistData(array):
    global is_asc, is_desc, has_negative, max_value, max_number_of_digits
    for i in range(len(array)-1):
        if array[i] < 0:
            has_negative = True
        if array[i] > array[i+1]:
            is_asc = is_asc - 1
            is_desc = is_desc + 1
        elif array[i] < array[i+1]:
            is_asc = is_asc + 1
            is_desc = is_desc - 1
        else:
            is_asc = is_asc + 1
            is_desc = is_desc + 1
        max_value = max(array[i], max_value)
        max_number_of_digits = max(len(str(array[i])), max_number_of_digits)   
    max_value = max(array[len(array)-1], max_value)
    max_number_of_digits = max(len(str(array[len(array)-1])), max_number_of_digits) 

def inversionCount(array):
    if len(array) <= 1:
        return 0
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    return inversionCount(left) + inversionCount(right) + merge(left, right)

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
