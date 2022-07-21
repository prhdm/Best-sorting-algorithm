package test;

import bestSortingAlgorithm.Algorithm;
import sortingAlgorithms.*;

import java.util.Arrays;

public class TestAlgorithms {
    String bestAlgorithm;
    public boolean correct;
    public TestAlgorithms(int[] array) {
        Test(array);
    }

    private void Test(int[] array) {
        String bestAlgo = Algorithm.algorithm(array);
        int[] array2 = Arrays.copyOf(array, array.length);
        long timeBubbleSort = testBubbleSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeCountSort = testCountSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeHeapSort = testHeapSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeInsertionSort = testInsertionSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeMergeSort = testMergeSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeQuickSort = testQuickSort(array2);
        array2 = Arrays.copyOf(array, array.length);
        long timeRadixSort = testRadixSort(array2);
        String bestFromTest = checkBest(timeBubbleSort, timeCountSort, timeHeapSort, timeInsertionSort, timeMergeSort, timeQuickSort, timeRadixSort);
        System.out.println(Arrays.toString(array));
        printResults(bestAlgo, bestFromTest, timeBubbleSort, timeCountSort, timeHeapSort, timeInsertionSort, timeMergeSort, timeQuickSort, timeRadixSort);
        correct = bestAlgo.contains(bestFromTest);
        System.out.println("Correct: " + correct);
        System.out.println("############################################################################");
    }

    private void printResults(String bestAlgo, String bestFromTest, long timeBubbleSort, long timeCountSort, long timeHeapSort, long timeInsertionSort, long timeMergeSort, long timeQuickSort, long timeRadixSort) {
        System.out.println("==========================================================");
        System.out.println("Bubble Sort: " + timeBubbleSort + " ms");
        System.out.println("Count Sort: " + timeCountSort + " ms");
        System.out.println("Heap Sort: " + timeHeapSort + " ms");
        System.out.println("Insertion Sort: " + timeInsertionSort + " ms");
        System.out.println("Merge Sort: " + timeMergeSort + " ms");
        System.out.println("Quick Sort: " + timeQuickSort + " ms");
        System.out.println("Radix Sort: " + timeRadixSort + " ms");
        System.out.println("Best algorithm: " + bestAlgo);
        System.out.println("Best algorithm from test: " + bestFromTest);
        System.out.println("==========================================================");
    }

    private String checkBest(long timeBubbleSort, long timeCountSort, long timeHeapSort, long timeInsertionSort, long timeMergeSort, long timeQuickSort, long timeRadixSort) {
        if (timeBubbleSort < timeCountSort && timeBubbleSort < timeHeapSort && timeBubbleSort < timeInsertionSort && timeBubbleSort < timeMergeSort && timeBubbleSort < timeQuickSort && timeBubbleSort < timeRadixSort) {
             return  "Bubble Sort";
        } else if (timeCountSort < timeBubbleSort && timeCountSort < timeHeapSort && timeCountSort < timeInsertionSort && timeCountSort < timeMergeSort && timeCountSort < timeQuickSort && timeCountSort < timeRadixSort) {
            return "Count Sort";
        } else if (timeHeapSort < timeBubbleSort && timeHeapSort < timeCountSort && timeHeapSort < timeInsertionSort && timeHeapSort < timeMergeSort && timeHeapSort < timeQuickSort && timeHeapSort < timeRadixSort) {
            return  "Heap Sort";
        } else if (timeInsertionSort < timeBubbleSort && timeInsertionSort < timeCountSort && timeInsertionSort < timeHeapSort && timeInsertionSort < timeMergeSort && timeInsertionSort < timeQuickSort && timeInsertionSort < timeRadixSort) {
            return  "Insertion Sort";
        } else if (timeMergeSort < timeBubbleSort && timeMergeSort < timeCountSort && timeMergeSort < timeHeapSort && timeMergeSort < timeInsertionSort && timeMergeSort < timeQuickSort && timeMergeSort < timeRadixSort) {
            return   "Merge Sort";
        } else if (timeQuickSort < timeBubbleSort && timeQuickSort < timeCountSort && timeQuickSort < timeHeapSort && timeQuickSort < timeInsertionSort && timeQuickSort < timeMergeSort && timeQuickSort < timeRadixSort) {
            return  "Quick Sort";
        } else if (timeRadixSort < timeBubbleSort && timeRadixSort < timeCountSort && timeRadixSort < timeHeapSort && timeRadixSort < timeInsertionSort && timeRadixSort < timeMergeSort && timeRadixSort < timeQuickSort) {
            return  "Radix Sort";
        } else {
            return "Merge Sort";
        }
    }

    private long testRadixSort(int[] array) {
        long startTime = System.nanoTime();
        RadixSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testQuickSort(int[] array) {
        long startTime = System.nanoTime();
        QuickSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testMergeSort(int[] array) {
        long startTime = System.nanoTime();
        MergeSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testInsertionSort(int[] array) {
        long startTime = System.nanoTime();
        InsertionSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testHeapSort(int[] array) {
        long startTime = System.nanoTime();
        HeapSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testCountSort(int[] array) {
        long startTime = System.nanoTime();
        CountSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }

    private long testBubbleSort(int[] array) {
        long startTime = System.nanoTime();
        BubbleSort.sort(array);
        long endTime = System.nanoTime();
        return endTime - startTime;
    }
}
