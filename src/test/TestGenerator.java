package test;

public class TestGenerator {
    public int[] array;
    public TestGenerator(int length) {
        array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = (int) (Math.random() * 100000000);
        }
    }
}
