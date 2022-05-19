import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;


class Main {
    static class Node implements Comparable<Node> {
        int i;
        int j;
        int distance;

        public Node(int i, int j, int distance) {
            this.i = i;
            this.j = j;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            if (this.distance < o.distance)
                return -1;
            else if (this.distance == o.distance)
                return 0;
            else
                return 1;
        }
    }

    // e,w,s,n
    static int[] di = {0, 0, 1, -1};
    static int[] dj = {-1, 1, 0, 0};
    static int N;
    static int M;
    static int T;
    static int D;
    static int[][] graph;
    static int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        // Input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] config = br.readLine().split(" ");
        N = Integer.parseInt(config[0]);
        M = Integer.parseInt(config[1]);
        T = Integer.parseInt(config[2]);
        D = Integer.parseInt(config[3]);

        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            String row = br.readLine().strip();
            for (int j = 0; j < M; j++) {
                char ch = row.charAt(j);
                graph[i][j] = getHeight(ch);
            }
        }

        int maxValue = Integer.MIN_VALUE;
        int[][] upMap = dijkstra(0, 0);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int[][] downMap = dijkstra(i, j);
                if (upMap[i][j] == INF || downMap[i][j] == INF)
                    continue;

                int upDownCost = upMap[i][j] + downMap[0][0];
                if (upDownCost > D)
                    continue;
                maxValue = Math.max(maxValue, graph[i][j]);
            }
        }

        System.out.println(maxValue);
    }

    static int getHeight(char id) {
        if (id >= 'a')
            return id - 'a' + 26;
        else
            return id - 'A';
    }

    static int[][] dijkstra(int si, int sj) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.offer(new Node(si, sj, 0));

        int[][] dist = new int[N][M];
        for (int[] ints : dist) {
            Arrays.fill(ints, Integer.MAX_VALUE);
        }
        dist[si][sj] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (dist[node.i][node.j] < node.distance)
                continue;

            for (int idx = 0; idx < 4; idx++) {
                int ni = node.i + di[idx];
                int nj = node.j + dj[idx];
                if (ni < 0 || ni >= N || nj < 0 || nj >= M)
                    continue;
                // cant go
                if (Math.abs(graph[ni][nj] - graph[node.i][node.j]) > T)
                    continue;

                if (graph[ni][nj] <= graph[node.i][node.j]) {
                    int newDist = node.distance + 1;
                    if (newDist < dist[ni][nj])
                    {
                        pq.offer(new Node(ni, nj, newDist));
                        dist[ni][nj] = newDist;
                    }
                }
                else {
                    int newDist = node.distance + Math.abs(graph[ni][nj] - graph[node.i][node.j]) * Math.abs(graph[ni][nj] - graph[node.i][node.j]);
                    if (newDist < dist[ni][nj])
                    {
                        pq.offer(new Node(ni, nj, newDist));
                        dist[ni][nj] = newDist;
                    }
                }
            }
        }
        return dist;
    }
}