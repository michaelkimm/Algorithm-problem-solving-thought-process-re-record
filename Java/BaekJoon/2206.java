import java.io.*;
import java.util.LinkedList;

class Main {
    static class Node {
        public int i;
        public int j;
        public boolean hasPower;    // 벽 부술 힘

        public Node(int i, int j, boolean hasPower) {
            this.i = i;
            this.j = j;
            this.hasPower = hasPower;
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
        LinkedList<>
        print2DAry(graph);

    }
}