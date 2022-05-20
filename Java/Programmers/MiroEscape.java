import java.io.*;
import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        int id;
        int distance;
        ArrayList<Node>[] graph;

        public Node(int id, int distance, ArrayList<Node>[] graph) {
            this.id = id;
            this.distance = distance;
            this.graph = graph;
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

        @Override
        protected Object clone() throws CloneNotSupportedException {
            Node newNode = new Node(this.id, this.distance, this.graph);
            return newNode;
        }
    }

    public static void main(String[] args) throws IOException, CloneNotSupportedException{
        int[] ns = {3, 4};
        int[] starts = {1, 1};
        int[] ends = {3, 4};
        int[][][] roads = {{{1,2,2}, {3,2,3}}, {{1,2,1}, {3,2,1}, {2,4,1}}};
        int[][] traps = {{2}, {2, 3}};
        for (int i = 0; i < ns.length; i++) {
            System.out.println(solution(ns[i], starts[i], ends[i], roads[i], traps[i]));
        }
    }

    public static int solution(int n, int start, int end, int[][] roads, int[] traps) throws CloneNotSupportedException {
        // initialize graph
//        @SuppressWarnings("unchecked")
//        ArrayList<Integer>[][] graph = new ArrayList[n + 1][n + 1];
        @SuppressWarnings("unchecked")
        ArrayList<Node>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<Node>();
        }

        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int cost = road[2];
            graph[u].add(new Node(v, cost, graph));
        }

        ArrayList<Integer> trapList = new ArrayList<>();
        for (int trap : traps) {
            trapList.add(trap);
        }
        // List<Integer> trapAryView = Arrays.asList(trapTmps);
        int answer = dijkstra(start, end, n, trapList, graph);
        return answer;
    }

    static int dijkstra(int start, int end, int n, List<Integer> traps,  ArrayList<Node>[] graph) {
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        int[] dist = new int[n + 1];

        pq.offer(new Node(start, 0, graph));
        Arrays.fill(dist, Integer.MAX_VALUE);

        System.out.println("new");
        int result = -1;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            System.out.println("node.id = " + node.id + "\tnode.d = " + node.distance);
            if (dist[node.id] < node.distance)
                continue;
            if (node.id == end) {
                result = node.distance;
                break;
            }

            // trap node
            ArrayList<Node>[] newGraph = copyArray(graph);
            if (traps.contains(node.id)) {
                // node to i and i to node exchange
                for (int i = 1; i <= n; i++) {
//                    reverseDirection(graph, node, i);
                }
            }


        }
        return result;
    }

    private static ArrayList<Node>[] copyArray(ArrayList<Node>[] graph) {
        @SuppressWarnings("unchecked")
        ArrayList<Node>[] newGraph = new ArrayList[graph.length];
        for (int i = 0; i < graph.length; i++) {
            newGraph[i] = new ArrayList<>(graph[i]);
        }
        return newGraph;
    }

    private static void reverseDirection(ArrayList<Node>[] graph, int start, int end) {
        ArrayList<Node> tmpNodes = graph[end];
        graph[end] = graph[start]
    }
}