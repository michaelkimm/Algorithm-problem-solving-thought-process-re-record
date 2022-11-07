import java.awt.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static int N;
    static int M;

    static LinkedList<Integer> list;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.valueOf(input[0]);
        M = Integer.valueOf(input[1]);

        list = new LinkedList<>();

        getPermutation(0);
        System.out.println(sb.toString());
    }

    static void getPermutation(int pickedCnt) {
        if (pickedCnt == M) {
            for (Integer integer : list) {
                sb.append(integer.toString() + " ");
            }
            sb.append("\n");
            return;
        }
        for (int i = 1; i <= N; i++) {
            list.add(i);
            getPermutation(pickedCnt + 1);
            list.pollLast();
        }
        return;
    }
}