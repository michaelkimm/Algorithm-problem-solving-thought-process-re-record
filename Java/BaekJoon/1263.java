import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    static class Node implements Comparable<Node> {
        int T;
        int S;
        int mustStartBeforeTime;

        public Node(int t, int s) {
            T = t;
            S = s;
            this.mustStartBeforeTime = S - T;
        }

        @Override
        public int compareTo(Main.Node o) {
            if (this.S != o.S) {
                return this.S - o.S;
            } else {
                return this.mustStartBeforeTime - o.mustStartBeforeTime;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        int N = Integer.parseInt(input);
        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            String[] inputs = bufferedReader.readLine().split(" ");
            nodes[i] = new Node(Integer.parseInt(inputs[0]), Integer.parseInt(inputs[1]));
        }
        Arrays.sort(nodes, Comparator.reverseOrder());

        int curTime = -1;
        for (int idx = 0; idx < N; idx++) {
            int endTime = curTime;
            if (curTime == -1 || nodes[idx].S < curTime) {
                endTime = nodes[idx].S;
            }
            int startTime = endTime - nodes[idx].T;
            curTime = startTime;
        }
        if (curTime < 0) {
            System.out.println(-1);
        } else {
            System.out.println(curTime);
        }
    }
}