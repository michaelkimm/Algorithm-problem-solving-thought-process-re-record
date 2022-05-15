import java.io.*;
import java.util.*;

class Main {
    static class Node implements Comparable<Node> {
        int id;
        long distance;

        public Node(int id, long distance) {
            this.id = id;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            if (this.distance < o.getDistance())
                return -1;
            else if (this.distance == o.getDistance())
                return 0;
            else
                return 1;
        }
    }
    static int N;
    static int M;
    static long D;
    static long E;
    static long[] heights;
    static ArrayList<Node>[] graph;
    static long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // N, M, D, E
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Long.parseLong(st.nextToken());
        E = Long.parseLong(st.nextToken());
        // heights
        st = new StringTokenizer(br.readLine());
        heights = new long[N + 1];
        graph = new ArrayList[N];
        for (int i = 1; i < N + 1; i++) {
            heights[i] = Long.parseLong(st.nextToken());
            graph[i] = new ArrayList<Node>();
        }

        // lines
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());
            graph[u].add(new Node(v, c));
            graph[v].add(new Node(u, c));
        }

        // get cost
        long[] endToTargetCosts = dijkstra(N);
        long[] startToTargetCosts = dijkstra(1);

        // get max cost
        long maxValue = Long.MIN_VALUE;
        for (int i = 0; i <= N; i++) {
            if (endToTargetCosts[i] == INF || startToTargetCosts[i] == INF)
                continue;
            maxValue = Math.max(maxValue, heights[i] * E - (startToTargetCosts[i] + endToTargetCosts[i]) * D);
        }

        if (maxValue == Long.MIN_VALUE)
            System.out.println("Impossible");
        else
            System.out.println(maxValue);
    }

    static long[] dijkstra(int start) {
        long[] dist = new long[N + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();

            if (dist[curNode.getId()] < curNode.getDistance()) {
                break;
            }

            for (Node nextNode : graph[curNode.getId()]) {
                // if next node height is lower
                if (heights[curNode.getId()] >= heights[nextNode.getId()])
                    continue;
                long newDist = curNode.getDistance() + nextNode.getDistance();

                if (newDist < dist[nextNode.getId()]) {
                    dist[nextNode.getId()] = newDist;
                    pq.offer(new Node(nextNode.getId(), dist[nextNode.getId()]));
                }
            }
        }
        return dist;
    }
}