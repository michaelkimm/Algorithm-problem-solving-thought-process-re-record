import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static boolean[][] visited = new boolean[5][5];
    static int K;
    static int answer = 0;

    static int[] di = {0, 0, 1, -1};
    static int[] dj = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.valueOf(br.readLine()).intValue();

        for (int i = 0; i < K; i++) {
            String[] inputs = br.readLine().split(" ");
            int ki = Integer.valueOf(inputs[0]).intValue() - 1;
            int kj = Integer.valueOf(inputs[1]).intValue() - 1;
            visited[ki][kj] = true;
        }

        visited[0][0] = true;
        visited[4][4] = true;
        recursive(0, 0, 1, 4, 4, 1);
        System.out.println(answer);
    }

    private static void recursive(int gi, int gj, int gc, int hi, int hj, int hc) {
        if (gi == hi && gj == hj) {
            // 같은 위치면 사과 수확을 중복해서 했을 것이기 때문에 (25 - K)에 1을 뺴줘야함
            if ((gc + hc) == (25 - K - 1)) {
                answer += 1;
            }
            return;
        }

        for (int gDirIdx = 0; gDirIdx < 4; gDirIdx++) {
            int ngi = gi + di[gDirIdx];
            int ngj = gj + dj[gDirIdx];
            if (ngi < 0 || ngi >= 5 || ngj < 0 || ngj >= 5) {
                continue;
            }
            for (int hDirIdx = 0; hDirIdx < 4; hDirIdx++) {
                int nhi = hi + di[hDirIdx];
                int nhj = hj + dj[hDirIdx];
                if (nhi < 0 || nhi >= 5 || nhj < 0 || nhj >= 5) {
                    continue;
                }
                if (visited[ngi][ngj] || visited[nhi][nhj]) {
                    continue;
                }
                visited[nhi][nhj] = true;
                visited[ngi][ngj] = true;
                recursive(ngi, ngj, gc + 1, nhi, nhj, hc + 1);
                visited[nhi][nhj] = false;
                visited[ngi][ngj] = false;
            }
        }
    }
}