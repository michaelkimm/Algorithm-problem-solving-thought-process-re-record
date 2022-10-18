import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bufferedReader.readLine().split(" ");
        int V = Integer.parseInt(input[0]);
        int E = Integer.parseInt(input[1]);

        int K = Integer.parseInt(bufferedReader.readLine());
        ArrayList<Node>[] graph = new ArrayList[V + 1];
        for (int i = 0; i < V + 1; i++) {
            graph[i] = new ArrayList<Node>();
        }
        for (int i = 0; i < E; i++) {
            input = bufferedReader.readLine().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);
            int c = Integer.parseInt(input[2]);
            graph[u].add(new Node(v, c));
        }

        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node(K, 0));
        int[] distance = new int[V + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[K] = 0;
        while (!priorityQueue.isEmpty()) {
            Node curNode = priorityQueue.poll();
            if (distance[curNode.vertex] < curNode.weight) {
                continue;
            }
            for (Node nextNode : graph[curNode.vertex]) {
                int newCost = nextNode.weight + curNode.weight;
                if (newCost < distance[nextNode.vertex]) {
                    priorityQueue.add(new Node(nextNode.vertex, newCost));
                    distance[nextNode.vertex] = newCost;
                }
            }
        }

        for (int i = 1; i < distance.length; i++) {
            int dist = distance[i];
            if (dist == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dist);
            }
        }
    }

    static class Node implements Comparable<Node> {
        int vertex;
        int weight;

        public Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return this.weight - o.weight;
        }
    }

}