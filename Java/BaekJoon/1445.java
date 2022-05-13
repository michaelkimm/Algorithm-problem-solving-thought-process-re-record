import java.io.*;
import java.util.*;

class Main {
    static class Node {
        private int arriveId;
        private long distance;

        public Node(int arriveId, long distance) {
            this.arriveId = arriveId;
            this.distance = distance;
        }

        public int getArriveId() {
            return arriveId;
        }

        public long getDistance() {
            return distance;
        }
    }
    static int N;
    static int M;
    static int D;
    static int E;
    static int[] heights;
    static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList>();
    static long[] startToEndCosts;
    static long[] endToTargetCosts;
    static long INF = Long.MAX_VALUE;

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // N, M, D, E
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        // heights
        st = new StringTokenizer(br.readLine());
        heights = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
            graph.add(new ArrayList<Node>());
        }
        // lines
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, c));
            graph.get(v).add(new Node(u, c));
        }

        // Initialization
        startToEndCosts = new long[N + 1];
        endToTargetCosts = new long[N + 1];
        Arrays.fill(startToEndCosts, 0);
        Arrays.fill(endToTargetCosts, INF);

        // Get endToTargetCosts value by dijkstra

        // Get startToEndCosts value dijkstra
    }
}