import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;

class Prob1162 {
    static class Node implements Comparable<Node> {
        private int arrive_id;
        private int distance;
        private int wrappedCnt;

        public Node(int arrive_id, int distance, int wrappedCnt) {
            this.arrive_id = arrive_id;
            this.distance = distance;
            this.wrappedCnt = wrappedCnt;
        }

        public int getArrive_id() {
            return arrive_id;
        }

        public int getDistance() {
            return distance;
        }

        public int getWrappedCnt() {
            return wrappedCnt;
        }

        @Override
        public int compareTo(Node o) {
            if (this.distance < o.distance)
                return -1;
            return 1;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "arrive_id=" + arrive_id +
                    ", distance=" + distance +
                    ", wrappedCnt=" + wrappedCnt +
                    '}';
        }
    }
    static final int INF = Integer.MAX_VALUE;
    static ArrayList<ArrayList<Node>> graph;
    static int[][] dist;
    static int N;
    static int M;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] graphMetaData = br.readLine().split(" ");
        N = Integer.parseInt(graphMetaData[0]);
        M = Integer.parseInt(graphMetaData[1]);
        K = Integer.parseInt(graphMetaData[2]);
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<Node>());
        }
        for (int i = 0; i < M; i++) {
            String[] lineData = br.readLine().split(" ");
            int u = Integer.parseInt(lineData[0]);
            int v = Integer.parseInt(lineData[1]);
            int c = Integer.parseInt(lineData[2]);
            graph.get(u).add(new Node(v, c, 0));
            graph.get(v).add(new Node(u, c, 0));
        }

        dist = new int[K + 1][N + 1];
        for (int i = 0; i < dist.length; i++) {
            Arrays.fill(dist[i], INF);
        }
        dijkstra(1);

        int min = INF;
        for (int i = 0; i < dist.length; i++) {
            int probableMin = dist[i][N];
            min = probableMin < min ? probableMin : min;
        }
        System.out.println(min);
    }

    public static void printResult() {
        for (int k = 0; k < K + 1; k++) {
            System.out.print("k: " + k + " / ");
            for (int i = 0; i < dist[0].length; i++) {
                System.out.print(dist[k][i] + ". ");
            }
            System.out.println();
        }
        System.out.println();
    }
    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0,0));
        for (int i = 0; i < K + 1; i++) {
            dist[i][start] = 0;
        }

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int distance = curNode.getDistance();
            int now = curNode.getArrive_id();
            int wrappedCnt = curNode.getWrappedCnt();

            if (dist[wrappedCnt][now] < distance)
                continue;

            for (int i = 0; i < graph.get(now).size(); i++) {
                int newCost = dist[wrappedCnt][now] + graph.get(now).get(i).getDistance();
                int newArrive = graph.get(now).get(i).getArrive_id();
                if (newCost < dist[wrappedCnt][newArrive]) {
                    dist[wrappedCnt][newArrive] = newCost;
                    pq.add(new Node(newArrive, newCost, wrappedCnt));
                }

                int newWrappedCnt = curNode.getWrappedCnt() + 1;
                if (newWrappedCnt <= K) {
                    newCost = dist[wrappedCnt][now] + 0;
                    if (newCost < dist[newWrappedCnt][newArrive]) {
                        dist[newWrappedCnt][newArrive] = newCost;
                        pq.add(new Node(newArrive, newCost, newWrappedCnt));
                    }
                }
            }
        }
    }
}
