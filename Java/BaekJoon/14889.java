import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static int N;
    static int[][] table;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().strip();
        N = Integer.valueOf(input);
        table = new int[N][N];
        visited = new boolean[N];
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                table[i][j] = Integer.valueOf(inputs[j]);
            }
        }

        combination(-1, 0);
        System.out.println(answer);
    }

    static void combination(int before, int depth) {
        if (depth == N / 2) {
            answer = Math.min(answer, getDiff(visited));
            return;
        }

        for (int i = before + 1; i < N; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            combination(i, depth + 1);
            visited[i] = false;
        }
    }

    static int getDiff(boolean[] memberIncludes) {

        int sum1 = 0;
        int sum2 = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (memberIncludes[i] && memberIncludes[j]) {
                    sum1 += table[i][j];
                } else if (!memberIncludes[i] && !memberIncludes[j]) {
                    sum2 += table[i][j];
                }
            }
        }
        return Math.abs(sum1 - sum2);
    }
}