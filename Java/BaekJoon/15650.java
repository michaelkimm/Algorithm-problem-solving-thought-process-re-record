import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static int N;
    static int M;

    static boolean[] visited;

    static LinkedList<Integer> list;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.valueOf(input[0]);
        M = Integer.valueOf(input[1]);

        list = new LinkedList<>();
        visited = new boolean[N + 1];

        getPermutation(0, 0);
    }

    static void getPermutation(int before, int pickedCnt) {
        if (pickedCnt == M) {
            for (Integer integer : list) {
                System.out.print(integer.toString() + " ");
            }
            System.out.println();
            return;
        }
        for (int i = before + 1; i <= N; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            list.add(i);
            getPermutation(i, pickedCnt + 1);
            visited[i] = false;
            list.pollLast();
        }
        return;
    }
}