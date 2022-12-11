import java.util.*;

class Main {
    public static void main(String[] args) {

        int n1 = 6;
        int k1 = 17;
        int[][] roads1 = {{5, 4, 6}, {5, 2, 5}, {0, 4, 2}, {2, 3, 3}, {1, 2, 7}, {0, 1, 3}};

        int n2 = 4;
        int k2 = 10;
        int[][] roads2 = {{0, 1, 2}, {0, 2, 3}};

        int n3 = 4;
        int k3 = 11;
        int[][] roads3 = {{0,1,2}, {1,2,7}, {2,3,10}, {3,0,9}};
        for (int i : solution(n3, k3, roads3)) {
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
        int[] none = {-1};
        if (answer.isEmpty()) {
            return none;
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
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Node)) return false;
            Node node = (Node) o;
            return id == node.id && dist == node.dist;
        }

        @Override
        public int hashCode() {
            return Objects.hash(id, dist);
        }
    }
}