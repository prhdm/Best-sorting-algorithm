import test.TestAlgorithms;
import test.TestGenerator;

public class Main {
    public static void main(String[] args) {
        int countCorrectCases = 0;
        for (int i = 1; i < 100; i++) {
            int[] array = new TestGenerator(1000*i).array;
            if (new TestAlgorithms(array).correct)
                countCorrectCases++;
        }
        System.out.println(countCorrectCases);
    }
}
