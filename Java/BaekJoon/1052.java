import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    static LinkedList<Integer> stack;
    static Deque<Integer> deque;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int K = Integer.parseInt(inputs[1]);

        stack = new LinkedList<>();
        deque = new LinkedList<>();

        if (N <= K) {
            System.out.println(0);
            return;
        }
        // 1. 물병 합치기 N % 2. N % 2 != 0이면 합쳐지지 않은 물병 존재.
        //
        while (true) {
            int result = 0;
            int tempN = N;
            while (tempN != 0) {
                if (tempN % 2 != 0) {
                    result += 1;
                }
                tempN /= 2;
            }
            if (result <= K) {
                break;
            }
            N += 1;
            answer += 1;
        }

        System.out.println(answer);
    }
}
