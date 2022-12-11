import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) throws IOException {
        // 1. 일반 케이스
        // - 인접 : 상하좌우

        // 2. 예외 케이스
        // - 왔던 곳 안오기
        // - 그리드 밖 안가기

        // 3. 알고리즘 선정 및 시간 복잡도 계산
        // - dfs, bfs : 시간 복잡도 = O(M*N), 공간 복잡도 = O(M*N)

        // 4. 구현
        int[][] a = {{1,2,3,3,2},{2,1,2,3,3},{2,3,3,3,3},{3,2,1,1,3},{1,3,2,3,3}};
        determineBiggestColorSpot(0, 0, a);

        // 5. 일반 케이스 적용
        // 6. 예외 케이스 적용
    }

    static int biggestColorSpotSize = 0;
    static int color = 0;
    static int colorSize = 0;
    // 상하좌우
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};

    public static void determineBiggestColorSpot(int cols, int rows, int a[][]) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                if (a[i][j] < 0) {
                    continue;
                }
                color = a[i][j];
                getColorSpot(i, j, a);
                if (colorSize > biggestColorSpotSize) {
                    biggestColorSpotSize = colorSize;
                }
                colorSize = 0;
            }
        }
        System.out.println(biggestColorSpotSize);
    }

    public static void getColorSpot(int i, int j, int a[][]) {
        // 갈 수 있고 방문하지 않은 곳일 때 들어올 수 있음
        colorSize += 1;
        a[i][j] *= -1;
        
        for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
            int ni = i + di[dirIdx];
            int nj = j + dj[dirIdx];
            if (ni < 0 || ni >= a.length || nj < 0 || nj >= a[0].length) {
                continue;
            }
            if (a[ni][nj] < 0) {
                continue;
            }
            if (a[ni][nj] != color) {
                continue;
            }
            // 그리드 안이고, 방문한 적 없고, 같은 색깔인 곳
            getColorSpot(ni, nj, a);
        }
    }

}
