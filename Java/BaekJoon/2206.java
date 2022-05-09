import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Main {
    static class Node {
        public int i;
        public int j;
        public boolean hasPower;
        public int[][] graph;

        public Node(int i, int j, boolean hasPower, int[][] graph) {
            this.i = i;
            this.j = j;
            this.hasPower = hasPower;
            this.graph = graph;
        }
    }

    public static void print2DAry(int[][] ary) {
        for (int i = 0; i < ary.length; i++) {
            for (int j = 0; j < ary[0].length; j++) {
                System.out.print(ary[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[] di = {-1, 1, 0, 0};
    public static int[] dj = {0, 0, -1, 1};
    public static int[][] copy2DArray(int[][] ary) {
        int[][] result = new int[ary.length][ary[0].length];
        for (int i = 0; i < ary.length; i++) {
            for (int j = 0; j < ary[0].length; j++) {
                result[i][j] = ary[i][j];
            }
        }
        return result;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] rowCol = br.readLine().split(" ");
        int N = Integer.parseInt(rowCol[0]);
        int M = Integer.parseInt(rowCol[1]);
        int[][] graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine().strip();
            for (int j = 0; j < M; j++) {
                graph[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }

        int si = 0;
        int sj = 0;
        int ei = N - 1;
        int ej = M - 1;
        int count = 0;
        Queue<Node> q = new LinkedList<>(Arrays.asList(new Node(si, sj, true, copy2DArray(graph))));
        Queue<Integer> countQ = new LinkedList<>(Arrays.asList(count));
        Set<Node> visited = new HashSet<>(Arrays.asList(new Node(si, sj, true, copy2DArray(graph))));
        int answer = -1;
        while (q.size() > 0) {
            Node curNode = q.remove();
            count = countQ.remove();

            if (curNode.i == ei && curNode.j == ej) {
                answer = count;
                break;
            }
            for (int idx = 0; idx < 4; idx++) {
                int ni = curNode.i + di[idx];
                int nj = curNode.j + dj[idx];
                if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
                    if (curNode.graph[ni][nj] == 0) {
                        Node newNode = new Node(ni, nj, curNode.hasPower, copy2DArray(curNode.graph));
                        if (visited.contains(newNode))
                            continue;
                        q.add(newNode);
                        visited.add(newNode);
                        countQ.add(count + 1);
                    }

                    if (curNode.graph[ni][nj] == 1) {
                        if (curNode.hasPower) {
                            int[][] newGraph = copy2DArray(curNode.graph);
                            newGraph[ni][nj] = 0;
                            Node breakableNode = new Node(ni, nj, false, newGraph);
                            if (visited.contains(breakableNode))
                                continue;
                            q.add(breakableNode);
                            visited.add(breakableNode);
                            countQ.add(count + 1);
                        }
                    }
                }
            }

        }
        print2DAry(graph);

        System.out.println();
        System.out.println(answer);
    }
}