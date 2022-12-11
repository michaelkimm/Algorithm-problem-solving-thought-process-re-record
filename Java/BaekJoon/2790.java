import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;

    static Integer[] scoreBeforeLast;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        N = Integer.parseInt(input);

        scoreBeforeLast = new Integer[N];
        for (int i = 0; i < N; i++) {
            scoreBeforeLast[i] = Integer.parseInt(bufferedReader.readLine().strip());
        }

        Arrays.sort(scoreBeforeLast, Collections.reverseOrder());
        int answer = 1;
        int maxScore = scoreBeforeLast[0] + 1;
        for (int i = 1; i < N; i++) {
            if (scoreBeforeLast[i] + N >= maxScore) {
                answer += 1;
            }
            maxScore = Math.max(maxScore, scoreBeforeLast[i] + i + 1);
        }
        System.out.println(answer);
    }
}
