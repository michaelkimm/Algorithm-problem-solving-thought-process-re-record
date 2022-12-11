import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;
    static int[] collected;
    static int[] numbers = {1, 2, 3};

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        N = Integer.parseInt(input);
        collected = new int[N];

        permutationOfReputation(0);

        StringBuilder stringBuilder = new StringBuilder();
        for (int num : collected) {
            stringBuilder.append(num);
        }
        System.out.println(stringBuilder.toString());
    }

    static boolean permutationOfReputation(int depth) {
        if (depth == N) {
            return true;
        }

        for (int i = 0; i < 3; i++) {
            collected[depth] = numbers[i];
            if (!checkGoodPermutation(depth + 1)) {
                continue;
            }
            if (permutationOfReputation(depth + 1)) {
                return true;
            }
        }
        return false;
    }

    static boolean checkGoodPermutation(int cnt) {
        for (int size = 1; size <= cnt / 2; size++) {
            int left = cnt - size * 2;
            int right = cnt - size;
            int equalCnt = 0;
            for (int d = 0; d < size; d++) {
                if (collected[left + d] == collected[right + d]) {
                    equalCnt += 1;
                }
            }
            if (equalCnt == size) {
                return false;
            }
        }
        return true;
    }
}