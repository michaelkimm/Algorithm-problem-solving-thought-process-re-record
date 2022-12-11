import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static class Point3D {
        int k;
        int i;
        int j;

        public Point3D(int k, int i, int j) {
            this.k = k;
            this.i = i;
            this.j = j;
        }
    }


    static int M;
    static int N;
    static int H;

    static int daysPassed = 0;

    // 앞뒤좌우상하
    static int[] di = {-1, 1, 0, 0, 0, 0};
    static int[] dj = {0, 0, -1, 1, 0, 0};
    static int[] dk = {0, 0, 0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        M = Integer.valueOf(input[0]);
        N = Integer.valueOf(input[1]);
        H = Integer.valueOf(input[2]);
        int[][][] farm = new int[H][N][M];
        Queue<Point3D> queue = new LinkedList<>();
        boolean didTomatoRipened = false;
        for (int k = 0; k < H; k++) {
            for (int i = 0; i < N; i++) {
                input = br.readLine().split(" ");
                for (int j = 0; j < M; j++) {
                    farm[k][i][j] = Integer.valueOf(input[j]);
                    if (farm[k][i][j] == 1) {
                        queue.add(new Point3D(k, i, j));
                    }
                }
            }
        }

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Point3D curPt = queue.poll();
                for (int idx = 0; idx < 6; idx++) {
                    int nk = curPt.k + dk[idx];
                    int ni = curPt.i + di[idx];
                    int nj = curPt.j + dj[idx];

                    if (nk < 0 || nk >= H || ni < 0 || ni >= N || nj < 0 || nj >= M) {
                        continue;
                    }
                    if (farm[nk][ni][nj] != 0) {
                        continue;
                    }
                    farm[nk][ni][nj] = 1;
                    queue.add(new Point3D(nk, ni, nj));
                    didTomatoRipened = true;
                }
            }
            daysPassed += 1;
        }


        // 출력
        // - 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력
        // 예외처리
        // - 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력
        if (isRawTomatoLeft(farm)) {
            System.out.println(-1);
        } else {
            if (didTomatoRipened) {
                System.out.println(daysPassed - 1);
            } else {
                System.out.println(0);
            }
        }
    }

    static boolean isRawTomatoLeft(int[][][] farm) {
        for (int[][] ints : farm) {
            for (int[] anInt : ints) {
                for (int i : anInt) {
                    if (i == 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}