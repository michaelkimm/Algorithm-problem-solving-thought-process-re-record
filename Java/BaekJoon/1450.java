import java.awt.*;
import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int N;
    static double child = 0;
    // 동서남북
    static int[] di = {0, 0, 1, -1};
    static int[] dj = {1, -1, 0, 0};
    static double[] movementCosts = new double[4];
    static boolean[][] visited;

    public static void recursive(int ci, int cj, int cN, double percent) {
        if (cN == N) {
            child += percent;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int ni = ci + di[i];
            int nj = cj + dj[i];
            if (visited[ni][nj]) {
                continue;
            }
            visited[ni][nj] = true;
            recursive(ni, nj, cN + 1, percent * movementCosts[i]);
            visited[ni][nj] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.valueOf(inputs[0]);
        movementCosts[0] = Double.valueOf(inputs[1]) / 100;
        movementCosts[1] = Double.valueOf(inputs[2]) / 100;
        movementCosts[2] = Double.valueOf(inputs[3]) / 100;
        movementCosts[3] = Double.valueOf(inputs[4]) / 100;

        visited = new boolean[2 * N + 1][2 * N + 1];
        visited[N][N] = true;
        recursive(N, N, 0, 1);
        System.out.println(child);
    }
}