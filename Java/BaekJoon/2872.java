import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;

    static int[] list;

    static int maxNum = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        N = Integer.valueOf(input);
        list = new int[N];

        for (int i = 0; i < N; i++) {
            input = bufferedReader.readLine().strip();
            int bookId = Integer.parseInt(input);
            list[i] = bookId;
            maxNum = Math.max(bookId, maxNum);
        }

        int nextBiggestNum = findBiggestPickNeededNum();
        int answer = nextBiggestNum;
        System.out.println(answer);
    }

    static int findBiggestPickNeededNum() {
        int nextBiggestNum = maxNum;
        for (int i = list.length - 1; i >= 0; i--) {
            if (list[i] == nextBiggestNum) {
                nextBiggestNum -= 1;
            }
        }
        return nextBiggestNum;
    }
}