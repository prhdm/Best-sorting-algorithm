import matplotlib.pyplot as plt

def plotresults(timebubblearray, timeinsertionarray, timemergearray, timecountarray, timeheaparray, timequickarray,
                timeradixarray):
    plt.xlim(1, 14)
    plt.ylim(0, 500, 5)
    plt.xlabel('Array size 2^n')
    plt.ylabel('Time in milliseconds')
    plt.plot(timebubblearray, label="bubble sort")
    plt.plot(timeinsertionarray, label="insertion sort")
    plt.plot(timemergearray, label="merge sort")
    plt.plot(timecountarray, label="count sort")
    plt.plot(timeheaparray, label="heap sort")
    plt.plot(timequickarray, label="quick sort")
    plt.plot(timeradixarray, label="radix sort")
    plt.legend()
    plt.show()
  