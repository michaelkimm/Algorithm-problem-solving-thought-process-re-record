import java.util.*;

class Main {
    public static void main(String[] args) {

        int n = 4;
        int k = 10;
        int[][] roads = {{0,1,2}, {0,2,3}};
        for (int i : solution(n, k, roads)) {
            System.out.println(i);
        }
    }


    public static int[] solution(int n, int k, int[][] roads) {
        // 연결 리스트 생성
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<Node>());
        }
        for (int i = 0; i < roads.length; i++) {
            int u = roads[i][0];
            int v = roads[i][1];
            int t = roads[i][2];
            graph.get(u).add(new Node(v, t));
            graph.get(v).add(new Node(u, t));
        }
        TreeSet<Integer> answer = new TreeSet<>();

        LinkedList<Node> queue = new LinkedList<>();
        Node startNode = new Node(0, 0);
        queue.add(startNode);
        // 방문
        HashSet<Node> visited = new HashSet<>();
        visited.add(startNode);

        while (queue.size() > 0) {
            Node curNode = queue.poll();
            if (curNode.dist == k) {
                answer.add(curNode.id);
                continue;
            }
            for (Node nextNode : graph.get(curNode.id)) {
                int newDist = curNode.dist + nextNode.dist;
                if (newDist > k) {
                    continue;
                }
                Node newNode = new Node(nextNode.id, newDist);
                if (visited.contains(newNode)) {
                    continue;
                }
                queue.add(newNode);
                visited.add(newNode);
            }

        }
        if (answer.isEmpty()) {
            return {-1};
        } else {
            return answer.stream().mapToInt(i->i).toArray();
        }
    }

    static class Node {
        int id;
        int dist;

        public Node(int id, int dist) {
            this.id = id;
            this.dist = dist;
        }



        @Override
        public boolean equals(Object obj) {
            Node cmp = (Node) obj;
            return id == cmp.id && dist == cmp.dist;
        }
    }
}