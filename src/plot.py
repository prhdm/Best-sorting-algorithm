import matplotlib.pyplot as plt

def plotresults(timebubblearray, timeinsertionarray, timemergearray):
    plt.xlim(1,14)
    plt.ylim(0,500,5)
    plt.xlabel('Array size 2^n')
    plt.ylabel('Time in milliseconds')
    plt.plot(timebubblearray, label = "bubble sort")
    plt.plot(timeinsertionarray, label = "insertion sort")
    plt.plot(timemergearray, label = "merge sort")
    plt.legend()
    plt.show()
    