import test
import plot


timebubblearray=[]
timeinsertionarray=[]
timemergearray=[]

def printresults(n,timemerge,timeinsertion,timebubble):
    print("*************************************************")
    print("for n = "+str(pow(2,n))+":")
    print("Merge Sort Running time: "+str(timemerge)+" milliseconds")
    print("Insertion Sort Running time: "+str(timeinsertion)+" milliseconds")
    print("Bubble Sort Running time: "+str(timebubble)+" milliseconds")
    print("*************************************************"+"\n")

def writeresults(n,timemerge,timeinsertion,timebubble):
    f = open("results.txt","a")
    f.write("*************************************************"+"\n")
    f.write("for n = "+str(pow(2,n))+":\n")
    f.write("Merge Sort Running time: "+str(timemerge)+" milliseconds\n")
    f.write("Insertion Sort Running time: "+str(timeinsertion)+" milliseconds\n")
    f.write("Bubble Sort Running time: "+str(timebubble)+" milliseconds\n")
    f.write("*************************************************"+"\n"+"\n")
    f.close()



for i in range(1,14):
    test.tester(i,timebubblearray,timeinsertionarray,timemergearray)
    printresults(i,timemergearray[i-1],timeinsertionarray[i-1],timebubblearray[i-1])
    writeresults(i,timemergearray[i-1],timeinsertionarray[i-1],timebubblearray[i-1])

plot.plotresults(timebubblearray, timeinsertionarray, timemergearray)

