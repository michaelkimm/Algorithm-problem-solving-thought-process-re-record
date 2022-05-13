import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static class Node implements Comparable<Node> {
        private int arrive_id;
        private long distance;
        private int wrappedCnt;

        public Node(int arrive_id, long distance, int wrappedCnt) {
            this.arrive_id = arrive_id;
            this.distance = distance;
            this.wrappedCnt = wrappedCnt;
        }

        public int getArrive_id() {
            return arrive_id;
        }

        public long getDistance() {
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
    static final long INF = Long.MAX_VALUE;
    static ArrayList<ArrayList<Node>> graph;
    static long[][] dist;
    static int N;
    static int M;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<Node>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, c, 0));
            graph.get(v).add(new Node(u, c, 0));
        }

        dist = new long[K + 1][N + 1];
        for (int i = 0; i < dist.length; i++) {
            Arrays.fill(dist[i], INF);
        }
        dijkstra(1);

        long min = INF;
        for (int k = 1; k <= K; k++) {
            long probableMin = dist[k][N];
            min = probableMin < min ? probableMin : min;
        }
        System.out.println(min);
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0L,0));
        for (int i = 0; i < K + 1; i++) {
            dist[i][start] = 0L;
        }

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            long distance = curNode.getDistance();
            int now = curNode.getArrive_id();
            int wrappedCnt = curNode.getWrappedCnt();

            if (dist[wrappedCnt][now] < distance)
                continue;

            for (int i = 0; i < graph.get(now).size(); i++) {
                long newCost = dist[wrappedCnt][now] + graph.get(now).get(i).getDistance();
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
