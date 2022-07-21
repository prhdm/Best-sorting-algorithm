from math import inf
import time

import algorithms.mergesort as mergesort
import algorithms.bubblesort as bubblesort
import algorithms.insertionsort as insertionsort
import algorithms.countsort as countsort
import algorithms.heapsort as heapsort
import algorithms.quicksort as quicksort
import algorithms.radixsort as radixsort


def getlist():
    with open("./test/1.txt", "r") as file:
        list = eval(file.readline())
        file.close()
        return list


def tester(timebubblearray, timeinsertionarray, timemergearray, timecountarray, timeheaparray, time_quick_array,
           timeradixarray, arr):
    timebubble, timeinsertion, timemerge, timecount, timeheap, timequick, timeradix = 0, 0, 0, 0, 0, 0, 0
    for i in range(5):
        list = arr[:]
        timebubble = testSort(bubblesort.sort, list) + timebubble
        timeinsertion = testSort(insertionsort.sort, list) + timeinsertion
        timemerge = testSort(mergesort.sort, list) + timemerge
        timecount = testSort(countsort.sort, list) + timecount
        timeheap = testSort(heapsort.sort, list) + timeheap
        timequick = testSort(quicksort.sort, list) + timequick
        timeradix = testSort(radixsort.sort, list) + timeradix
    timebubblearray.append(round(timebubble * 1000, 5) / 5)
    timeinsertionarray.append(round(timeinsertion * 1000, 5) / 5)
    timemergearray.append(round(timemerge * 1000, 5) / 5)
    timecountarray.append(round(timecount * 1000, 5) / 5)
    timeheaparray.append(round(timeheap * 1000, 5) / 5)
    time_quick_array.append(round(timequick * 1000, 5) / 5)
    timeradixarray.append(round(timeradix * 1000, 5) / 5)


def testSort(sort_algorithm, list):
    temp = list[:]
    start = time.time()
    try:
        sort_algorithm(temp)
    except RecursionError:
        print("stackoverflow")
        return inf
    except Exception:
        print("negative number")
        return inf
    end = time.time()
    return end - start
