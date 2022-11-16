import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    static class Node implements Comparable<Node> {
        int tasteOf5000;
        int tasteOf1000;

        public Node(int tasteOf5000, int tasteOf1000) {
            this.tasteOf5000 = tasteOf5000;
            this.tasteOf1000 = tasteOf1000;
        }

        @Override
        public int compareTo(Main.Node o) {
            return (this.tasteOf5000 - this.tasteOf1000) - (o.tasteOf5000 - o.tasteOf1000);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int X = Integer.parseInt(inputs[1]);

        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            inputs = bufferedReader.readLine().split(" ");
            Node node = new Node(Integer.parseInt(inputs[0]), Integer.parseInt(inputs[1]));
            nodes[i] = node;
        }
        Arrays.sort(nodes, Collections.reverseOrder());

        int satisfaction = 0;
        // 천원짜리 다 사기
        X -= (1000 * N);
        for (Node node : nodes) {
            satisfaction += node.tasteOf1000;
        }
        // (오천 만족도 - 천 만족도) 큰 순서대로 돈이 있는한 바꿔치기
        for (Node node : nodes) {
            int tmpX = X + 1000 - 5000;
            if (tmpX < 0) {
                continue;
            }

            int dTasteProfit = node.tasteOf5000 - node.tasteOf1000;
            if (dTasteProfit <= 0) {
                continue;
            }

            X = tmpX;
            satisfaction += dTasteProfit;
        }

        System.out.println(satisfaction);
    }
}