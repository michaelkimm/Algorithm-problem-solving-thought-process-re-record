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
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        PriorityQueue<Long> priorityQueue = new PriorityQueue<>();

        long[] cards = new long[n];
        inputs = bufferedReader.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            priorityQueue.add(Long.parseLong(inputs[i]));
        }

        while (m > 0) {
            Long card1 = priorityQueue.poll();
            Long card2 = priorityQueue.poll();
            long sum = card1 + card2;
            priorityQueue.add(sum);
            priorityQueue.add(sum);
            m -= 1;
        }

        long answer = 0L;
        for (Long val : priorityQueue) {
            answer += val;
        }
        System.out.println(answer);
    }
}