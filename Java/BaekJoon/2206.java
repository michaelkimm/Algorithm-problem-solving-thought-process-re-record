import java.io.*;
import java.util.*;

class Main {
    public static int[] di = {-1, 1, 0, 0};
    public static int[] dj = {0, 0, -1, 1};

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
        int count = 1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{si, sj, count, 0});

        boolean[][][] visitedAry = new boolean[2][N][M];
        visitedAry[0][si][sj]= true;

        int answer = -1;
        while (q.size() > 0) {
            int[] curInfo = q.poll();

            if (curInfo[0] == ei && curInfo[1] == ej) {
                answer = curInfo[2];
                break;
            }
            for (int idx = 0; idx < 4; idx++) {
                int ni = curInfo[0] + di[idx];
                int nj = curInfo[1] + dj[idx];
                if (ni < 0 || ni >= N || nj < 0 || nj >= M)
                    continue;
                if (graph[ni][nj] == 0) {
                    if (visitedAry[curInfo[3]][ni][nj])
                        continue;
                    q.offer(new int[]{ni, nj, curInfo[2] + 1, curInfo[3]});
                    visitedAry[curInfo[3]][ni][nj] = true;
                }

                if (graph[ni][nj] == 1) {
                    if (curInfo[3] == 1)
                        continue;
                    if (visitedAry[curInfo[3]][ni][nj])
                        continue;
                    q.offer(new int[]{ni, nj, curInfo[2] + 1, 1});
                    visitedAry[1][ni][nj] = true;
                }
            }

        }
        System.out.println(answer);
    }
}