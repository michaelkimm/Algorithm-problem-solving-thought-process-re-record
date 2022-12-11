import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static int N;
    static int[] record;
    static int answer = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().strip();
        N = Integer.valueOf(input);

        record = new int[N];

        getQueenAvailableCaseCnt(0);
        System.out.println(answer);
        // 퀸 둘 수 있는 남은 자리
        // 남은 둬야할 퀸 개수
    }

    static void getQueenAvailableCaseCnt(int depth) {
        // depth는 열
        if (depth == N) {
            answer += 1;
            return;
        }
        // 행
        for (int i = 0; i < N; i++) {
            if (!checkQueenPossible(i, depth)) {
                continue;
            }
            // depth열 i번째 행에 queen이 있음
            record[depth] = i;
            getQueenAvailableCaseCnt(depth + 1);
        }
    }

    static boolean checkQueenPossible(int qi, int qj) {
        for (int j = 0; j < qj; j++) {
            if (record[j] == qi) {
                return false;
            }
            if (Math.abs(j - qj) == Math.abs(record[j] - qi)) {
                return false;
            }
        }
        return true;
    }
}