package test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TestGenerator {
    public int[] array;
    public TestGenerator(int length) {
        array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = (int) (Math.random()*10 * length);
        }
        Collections.shuffle(List.of(array));
    }

    public void generateTestWithNegativeNumbers(int length) {
        array = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = (int) (Math.random()*10 * length);
        }
        Collections.shuffle(List.of(array));
        for (int i = 0; i < length; i++) {
            if (Math.random() < 0.5) {
                array[i] = -array[i];
            }
        }
    }

    public void generateTestInSpecificRange(int length)  {
        int hi = (int) (Math.random()*10 * length);
        int lo = (int) (Math.random()*10 * length);
        hi = Math.max(hi, lo);
        lo = Math.min(hi, lo);
        array = new int[length];
        for (int i = 0; i < length; i++) {
            int num = (int) (Math.random()*10*(hi-lo) + lo);
            array[i] = num;
        }
    }
}
