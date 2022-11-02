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

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Point3D)) return false;
            Point3D point3D = (Point3D) o;
            return k == point3D.k && i == point3D.i && j == point3D.j;
        }

        @Override
        public int hashCode() {
            return Objects.hash(k, i, j);
        }
    }
    static int M;
    static int N;
    static int H;

    static int rawTomatoCnt = 0;
    static int daysPassed = 0;
    static Set<Point3D> ripablePts;

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
        for (int k = 0; k < H; k++) {
            for (int i = 0; i < N; i++) {
                input = br.readLine().split(" ");
                for (int j = 0; j < M; j++) {
                    farm[k][i][j] = Integer.valueOf(input[j]);
                }
            }
        }

        ripablePts = getRipablePts(farm);
        rawTomatoCnt = getRawTomatoCount(farm);
        while (!ripablePts.isEmpty()) {
            // 토마토 익히기
            ripablePts = ripenTomato(farm);
            daysPassed += 1;
        }
        
        // 출력
        // - 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력
        // 예외처리
        // - 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력
        if (rawTomatoCnt > 0) {
            System.out.println(-1);
        } else {
            System.out.println(daysPassed);
        }
    }

    static void checkRipable(int k, int i, int j, int[][][] farm, Set<Point3D> set) {
        for (int idx = 0; idx < 6; idx++) {
            int nk = k + dk[idx];
            int ni = i + di[idx];
            int nj = j + dj[idx];
            if (nk < 0 || nk >= H || ni < 0 || ni >= N || nj < 0 || nj >= M) {
                continue;
            }

            if (farm[nk][ni][nj] != 0) {
                continue;
            }

            Point3D nextPt = new Point3D(nk, ni, nj);
            if (set.contains(nextPt)) {
                continue;
            }
            set.add(nextPt);
        }
    }

    static Set<Point3D> getRipablePts(int[][][] farm) {
        HashSet<Point3D> ripablePts = new HashSet<>();
        for (int k = 0; k < farm.length; k++) {
            for (int i = 0; i < farm[0].length; i++) {
                for (int j = 0; j < farm[0][0].length; j++) {
                    if (farm[k][i][j] != 1) {
                        continue;
                    }
                    checkRipable(k, i, j, farm, ripablePts);
                }
            }
        }
        return ripablePts;
    }

    static Set<Point3D> ripenTomato(int[][][] farm) {
        int h = farm.length;
        int n = farm[0].length;
        int m = farm[0][0].length;
        HashSet<Point3D> newRipablePts = new HashSet<>();
        for (Point3D ripablePt : ripablePts) {
            if (farm[ripablePt.k][ripablePt.i][ripablePt.j] == 0) {
                farm[ripablePt.k][ripablePt.i][ripablePt.j] = 1;
                rawTomatoCnt -= 1;
            }
        }

        for (Point3D ripablePt : ripablePts) {
            checkRipable(ripablePt.k, ripablePt.i, ripablePt.j, farm, newRipablePts);
        }
        return newRipablePts;
    }

    static int getRawTomatoCount(int[][][] farm) {
        int cnt = 0;
        for (int[][] ints : farm) {
            for (int[] anInt : ints) {
                for (int i : anInt) {
                    if (i == 0) {
                        cnt += 1;
                    }
                }
            }
        }
        return cnt;
    }
}