import time
import random
import algorithms.mergesort as mergesort
import algorithms.bubblesort as bubblesort
import algorithms.insertionsort as insertionsort

def randomArrayGenerator(size):
    list = []
    for i in range(pow(2,size)):
            list.append(random.randint(0,10))
    return list

def bubbleSortTest(list):
    temp = list[:]
    start = time.time()
    bubblesort.sort(temp)
    end = time.time()
    return end - start

def mergeSortTest(list):
    temp = list[:]
    start = time.time()
    mergesort.sort(temp)
    end = time.time()
    return end - start

def insertionSortTest(list):
    temp = list[:]
    start = time.time()
    insertionsort.sort(temp)
    end = time.time()
    return end - start

def tester(n, timebubblearray, timeinsertionarray, timemergearray):
    timebubble , timeinsertion , timemerge = 0 , 0 , 0
    for i in range(5): 
        list = randomArrayGenerator(n)
        timebubble = bubbleSortTest(list) + timebubble
        timeinsertion = insertionSortTest(list) + timeinsertion
        timemerge = mergeSortTest(list) + timemerge
    
    timebubble = round(timebubble*1000,2)/5
    timeinsertion = round(timeinsertion*1000,2)/5
    timemerge = round(timemerge*1000,2)/5
    timebubblearray.append(timebubble)
    timeinsertionarray.append(timeinsertion)
    timemergearray.append(timemerge)
