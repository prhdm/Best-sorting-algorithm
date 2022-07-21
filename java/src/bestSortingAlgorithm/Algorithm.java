package bestSortingAlgorithm;

public class Algorithm {
    static int numbofAscending = 0;
    static int numbofDescending = 0;
    static boolean hasNegative = false;
    static int maxValue = 0;
    static int maxNumberOfDigits = 0;
    public static String algorithm(int[] array) {
        numbofAscending = 0;
        numbofDescending = 0;
        hasNegative = false;
        maxValue = 0;
        maxNumberOfDigits = 0;
        dataAnalysis(array);
        System.out.println("numbofAscending: " + numbofAscending);
        System.out.println("numbofDescending: " + numbofDescending);
        if (numbofAscending < array.length/2 && numbofDescending < array.length/2) {
            return "Quick Sort";
        }
        if (!hasNegative) {
            System.out.println(maxNumberOfDigits);
            System.out.println(Math.log(array.length));
            double nLogn = array.length * Math.log(array.length);
            if (maxValue < nLogn) {
                return "Count Sort";
            }
            else if (maxNumberOfDigits < nLogn) {
                return "Radix Sort";
            }
        }
        if (numbofAscending+1 == array.length) {
            return "Insertion Sort";
        }
        if (numbofDescending+1 == array.length) {
            return "Merge Sort";
        }
        return "Heap Sort";
    }

    private static void dataAnalysis(int[] array) {
        for (int i = 0; i < array.length-1; i++) {
            if (array[i] < 0) {
                hasNegative = true;
            }
            if (array[i] > array[i + 1]) {
                numbofAscending++;
                numbofDescending--;
            } else if (array[i] < array[i + 1]) {
                numbofDescending++;
                numbofAscending--;
            } else {
                numbofAscending++;
                numbofDescending++;
            }
            maxValue = Math.max(maxValue, array[i]);
            maxNumberOfDigits = Math.max(maxNumberOfDigits, String.valueOf(array[i]).length());
        }
        maxValue = Math.max(maxValue, array[array.length-1]);
        maxNumberOfDigits = Math.max(maxNumberOfDigits, String.valueOf(array[array.length-1]).length());
    }
}
