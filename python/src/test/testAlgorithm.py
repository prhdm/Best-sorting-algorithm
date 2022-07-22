from math import inf
import time

import src.sortingAlgorithms.mergesort as mergesort
import src.sortingAlgorithms.bubblesort as bubblesort
import src.sortingAlgorithms.insertionsort as insertionsort
import src.sortingAlgorithms.countsort as countsort
import src.sortingAlgorithms.heapsort as heapsort
import src.sortingAlgorithms.quicksort as quicksort
import src.sortingAlgorithms.radixsort as radixsort
import src.bestSortingAlgorithm.bestsortingalgorithm as algorithm
import src.plot.plot as plot


def best(timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix):
    if timemerge < timeinsertion and timemerge < timebubble and timemerge < timecount and timemerge < timeheap and timemerge < timequick and timemerge < timeradix:
        return "Merge Sort"
    elif timeinsertion < timemerge and timeinsertion < timebubble and timeinsertion < timecount and timeinsertion < timeheap and timeinsertion < timequick and timeinsertion < timeradix:
        return "Insertion Sort"
    elif timebubble < timemerge and timebubble < timeinsertion and timebubble < timecount and timebubble < timeheap and timebubble < timequick and timebubble < timeradix:
        return "Bubble Sort"
    elif timecount < timemerge and timecount < timeinsertion and timecount < timebubble and timecount < timeheap and timecount < timequick and timecount < timeradix:
        return "Count Sort"
    elif timeheap < timemerge and timeheap < timeinsertion and timeheap < timebubble and timeheap < timecount and timeheap < timequick and timeheap < timeradix:
        return "Heap Sort"
    elif timequick < timemerge and timequick < timeinsertion and timequick < timebubble and timequick < timecount and timequick < timeheap and timequick < timeradix:
        return "Quick Sort"
    elif timeradix < timemerge and timeradix < timeinsertion and timeradix < timebubble and timeradix < timecount and timeradix < timeheap and timeradix < timequick:
        return "Radix Sort"
    else:
        return "Error"


class Test:
    def __init__(self):
        self.numbOfCorrect = 0
        self.timeBubbleArray = []
        self.timeinsertionarray = []
        self.timemergearray = []
        self.timeCountArray = []
        self.timeHeapArray = []
        self.timeQuickArray = []
        self.timeRadixArray = []
        self.arr = []
        self.bestalgorithm = ""

    def set_arr(self, arr):
        self.arr = arr

    def test(self, name):
        self.bestalgorithm = algorithm.pyme(self.arr)
        self.tester(self.timeBubbleArray, self.timeinsertionarray, self.timemergearray, self.timeCountArray,
                    self.timeHeapArray, self.timeQuickArray, self.timeRadixArray, self.arr)
        self.printResult()
        self.write_results(name)

    def printResult(self):
        timemerge = self.timemergearray[len(self.timemergearray) - 1]
        timebubble = self.timeBubbleArray[len(self.timeBubbleArray) - 1]
        timeinsertion = self.timeinsertionarray[len(self.timeinsertionarray) - 1]
        timecount = self.timeCountArray[len(self.timeCountArray) - 1]
        timeheap = self.timeHeapArray[len(self.timeHeapArray) - 1]
        timequick = self.timeQuickArray[len(self.timeQuickArray) - 1]
        timeradix = self.timeRadixArray[len(self.timeRadixArray) - 1]
        print("*************************************************")
        print(self.bestalgorithm)
        print("Merge Sort Running time: " + str(timemerge) + " milliseconds")
        print("Insertion Sort Running time: " + str(timeinsertion) + " milliseconds")
        print("Bubble Sort Running time: " + str(timebubble) + " milliseconds")
        print("Count Sort Running time: " + str(timecount) + " milliseconds")
        print("Heap Sort Running time: " + str(timeheap) + " milliseconds")
        print("Quick Sort Running time: " + str(timequick) + " milliseconds")
        print("Radix Sort Running time: " + str(timeradix) + " milliseconds")
        print("*************************************************" + "\n")
        print("Best is " + best(timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix))
        if self.bestalgorithm == best(timemerge, timeinsertion, timebubble,
                                      timecount, timeheap, timequick, timeradix):
            self.numbOfCorrect += 1

    def get_number_of_correct(self):
        return self.numbOfCorrect

    def tester(self, timebubblearray, timeinsertionarray, timemergearray, timecountarray, timeheaparray,
               time_quick_array,
               timeradixarray, arr):
        timebubble, timeinsertion, timemerge, timecount, timeheap, timequick, timeradix = 0, 0, 0, 0, 0, 0, 0
        for i in range(5):
            list = arr[:]
            timebubble = self.testSort(bubblesort.sort, list) + timebubble
            timeinsertion = self.testSort(insertionsort.sort, list) + timeinsertion
            timemerge = self.testSort(mergesort.sort, list) + timemerge
            timecount = self.testSort(countsort.sort, list) + timecount
            timeheap = self.testSort(heapsort.sort, list) + timeheap
            timequick = self.testSort(quicksort.sort, list) + timequick
            timeradix = self.testSort(radixsort.sort, list) + timeradix
        self.appendToArray(timebubblearray, timebubble)
        self.appendToArray(timeinsertionarray, timeinsertion)
        self.appendToArray(timemergearray, timemerge)
        self.appendToArray(timecountarray, timecount)
        self.appendToArray(timeheaparray, timeheap)
        self.appendToArray(time_quick_array, timequick)
        self.appendToArray(timeradixarray, timeradix)

    def appendToArray(self, arr, time_sort):
        arr.append(round(time_sort * 1000, 5) / 5)

    def testSort(self, sort_algorithm, list):
        temp = list[:]
        start = time.time()
        try:
            sort_algorithm(temp)
        except Exception:
            return inf
        end = time.time()
        return end - start

    def write_results(self, file_name):
        timemerge = self.timemergearray[len(self.timemergearray) - 1]
        timebubble = self.timeBubbleArray[len(self.timeBubbleArray) - 1]
        timeinsertion = self.timeinsertionarray[len(self.timeinsertionarray) - 1]
        timecount = self.timeCountArray[len(self.timeCountArray) - 1]
        timeheap = self.timeHeapArray[len(self.timeHeapArray) - 1]
        timequick = self.timeQuickArray[len(self.timeQuickArray) - 1]
        timeradix = self.timeRadixArray[len(self.timeRadixArray) - 1]
        with open(file_name, "a") as file:
            file.write("*************************************************" + "\n")
            file.write("Merge Sort Running time: " + str(timemerge) + " milliseconds" + "\n")
            file.write("Insertion Sort Running time: " + str(timeinsertion) + " milliseconds" + "\n")
            file.write("Bubble Sort Running time: " + str(timebubble) + " milliseconds" + "\n")
            file.write("Count Sort Running time: " + str(timecount) + " milliseconds" + "\n")
            file.write("Heap Sort Running time: " + str(timeheap) + " milliseconds" + "\n")
            file.write("Quick Sort Running time: " + str(timequick) + " milliseconds" + "\n")
            file.write("Radix Sort Running time: " + str(timeradix) + " milliseconds" + "\n")
            file.write("Best is " + best(timemerge, timeinsertion, timebubble, timecount,
                                         timeheap, timequick, timeradix) + "\n")
            file.write("Best from algorithm is " + self.bestalgorithm + "\n")
            file.write("number of correct cases: " + str(self.numbOfCorrect) + "\n")
            file.write("*************************************************" + "\n")
            file.close()

    def plot_results(self,name):
        plot.plotresults(self.timeBubbleArray, self.timeinsertionarray, self.timemergearray,
                         self.timeCountArray, self.timeHeapArray, self.timeQuickArray, self.timeRadixArray, name)
