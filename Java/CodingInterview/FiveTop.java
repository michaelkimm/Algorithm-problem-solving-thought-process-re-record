import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

class Main {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        Integer[] ary = {3, 2, 1, 4, 5};
        Integer[][] ary2D = {{2, 6}, {1, 5}, {1, 3}};

        Arrays.sort(ary2D, (v1, v2) -> {
            if (v1[0] == v2[0]) {
                return Integer.compare(v1[1], v2[1]);
            } else {
                return Integer.compare(v1[0], v2[0]);
            }
        });
        print2DArray(ary2D);
    }

    public static void printAry(Integer[] ary) {
        Arrays.stream(ary).forEach(System.out::println);
    }

    public static void print2DArray(Integer[][] ary) {
        for (int i = 0; i < ary.length; i++) {
            Arrays.stream(ary[i]).forEach(System.out::print);
        }
    }



}
