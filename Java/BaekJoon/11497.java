import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int T;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        T = Integer.parseInt(input);

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(bufferedReader.readLine().strip());
            String[] inputs = bufferedReader.readLine().split(" ");
            Integer[] src = new Integer[N];
            for (int j = 0; j < N; j++) {
                src[j] = Integer.parseInt(inputs[j]);
            }
            Arrays.sort(src, Collections.reverseOrder());
            Deque<Integer> deque = new LinkedList<>();
            boolean leftPushed = false;
            for (int j = 0; j < N; j++) {
                if (leftPushed) {
                    deque.addLast(src[j]);
                    leftPushed = false;
                } else {
                    deque.addFirst(src[j]);
                    leftPushed = true;
                }
            }

            // 인접 최소 값 계산
            int adjMax = Math.abs(deque.getLast() - deque.getFirst());
            int beforeVal = deque.pollFirst();
            while (!deque.isEmpty()) {
                int curVal = deque.pollFirst();
                adjMax = Math.max(adjMax, Math.abs(beforeVal - curVal));
                beforeVal = curVal;
            }
            sb.append(adjMax);
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}
