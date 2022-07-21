package sortingAlgorithms;

public class RadixSort {
    public static void sort(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        int exp = 1;
        while (max / exp > 0) {
            countSort(arr, exp);
            exp *= 10;
        }
    }
    public static void countSort(int[] arr, int exp) {
        int[] output = new int[arr.length];
        int[] count = new int[10];
        for (int j : arr) {
            count[(j / exp) % 10]++;
        }
        for (int i = 1; i < count.length; i++) {
            count[i] += count[i - 1];
        }
        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
        System.arraycopy(output, 0, arr, 0, arr.length);
    }
}
