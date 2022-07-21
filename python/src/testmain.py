import test as test
import bestsortingalgorithm as algorithm

timeBubbleArray, timeCountArray, timeinsertionarray, timemergearray, timeHeapArray, timeQuickArray, timeRadixArray = [], [], [], [], [], [], []
numbOfCorrect = 0
def printresults(n, timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix, bestalgorithm):
    global numbOfCorrect
    print("*************************************************")
    print(bestalgorithm)
    print("Merge Sort Running time: " + str(timemerge) + " milliseconds")
    print("Insertion Sort Running time: " + str(timeinsertion) + " milliseconds")
    print("Bubble Sort Running time: " + str(timebubble) + " milliseconds")
    print("Count Sort Running time: " + str(timecount) + " milliseconds")
    print("Heap Sort Running time: " + str(timeheap) + " milliseconds")
    print("Quick Sort Running time: " + str(timequick) + " milliseconds")
    print("Radix Sort Running time: " + str(timeradix) + " milliseconds")
    print("*************************************************" + "\n")
    print("Best is " + best(timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix))
    if bestalgorithm == best(timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix):
        numbOfCorrect += 1
        print("Correct")
        print(numbOfCorrect)

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

def write_results(n, timemerge, timeinsertion, timebubble, timecount, timeheap, timequick, timeradix):
    with open("results.txt", "a") as file:
        file.write("*************************************************" + "\n")
        file.write("for n = " + str(pow(2, n)) + ":" + "\n")
        file.write("Merge Sort Running time: " + str(timemerge) + " milliseconds" + "\n")
        file.write("Insertion Sort Running time: " + str(timeinsertion) + " milliseconds" + "\n")
        file.write("Bubble Sort Running time: " + str(timebubble) + " milliseconds" + "\n")
        file.write("Count Sort Running time: " + str(timecount) + " milliseconds" + "\n")
        file.write("Heap Sort Running time: " + str(timeheap) + " milliseconds" + "\n")
        file.write("Quick Sort Running time: " + str(timequick) + " milliseconds" + "\n")
        file.write("Radix Sort Running time: " + str(timeradix) + " milliseconds" + "\n")
        file.write("*************************************************" + "\n")
        file.close()

def main(arr:list):
    i=0
    test.tester(timeBubbleArray, timeinsertionarray, timemergearray, timeCountArray, timeHeapArray,
                    timeQuickArray,
                    timeRadixArray, arr)
    printresults(i, timemergearray[i - 1], timeinsertionarray[i - 1], timeBubbleArray[i - 1], timeCountArray[i - 1],
                     timeHeapArray[i - 1], timeQuickArray[i - 1], timeRadixArray[i - 1], algorithm.pyme(arr))
    write_results(i, timemergearray[i - 1], timeinsertionarray[i - 1], timeBubbleArray[i - 1],
                      timeCountArray[i - 1],
                      timeHeapArray[i - 1], timeQuickArray[i - 1], timeRadixArray[i - 1])

