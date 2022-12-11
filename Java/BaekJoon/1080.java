import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        char[][] source = new char[N][M];
        for (int i = 0; i < N; i++) {
            char[] array = bufferedReader.readLine().strip().toCharArray();
            for (int j = 0; j < M; j++) {
                source[i][j] = array[j];
            }
        }

        char[][] target = new char[N][M];
        for (int i = 0; i < N; i++) {
            char[] array = bufferedReader.readLine().strip().toCharArray();
            for (int j = 0; j < M; j++) {
                target[i][j] = array[j];
            }
        }

        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (source[i][j] == target[i][j]) {
                    continue;
                }
                flip(i, j, source);
                answer += 1;
            }
        }
        if (isSame(source, target)) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }

    static void flip(int si, int sj, char[][] source) {
        if (si + 3 > source.length || sj + 3 > source[0].length) {
            return;
        }
        for (int di = 0; di < 3; di++) {
            for (int dj = 0; dj < 3; dj++) {
                if (source[si + di][sj + dj] == '1') {
                    source[si + di][sj + dj] = '0';
                } else {
                    source[si + di][sj + dj] = '1';
                }
            }
        }
        return;
    }

    static boolean isSame(char[][] source, char[][] target) {
        int N = source.length;;
        int M = source[0].length;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (source[i][j] != target[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}