import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {

    // 동서남북
    public static int[] di = {0, 0, 1, -1};
    public static int[] dj = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bufferedReader.readLine().split(" ");
        int L = Integer.parseInt(input[0]);
        int W = Integer.parseInt(input[1]);

        char[][] map = new char[L][W];
        for (int i = 0; i < L; i++) {
            char[] mapInput = bufferedReader.readLine().toCharArray();
            for (int j = 0; j < W; j++) {
                map[i][j] = mapInput[j];
            }
        }

        // 규칙
        // - 격자 내 움직임
        // - 같은 곳 두번 이동x
        // - 최단 거리 이동

        // 목표
        // - 보물이 묻혀 있는 두 곳 사이를 최단 거리
        // - 보물이 묻혀 있는 두 곳 : [보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.]

        // 1. 일반 케이스(실제로 해보기)
        // - 영역 내 칸이 두개 이상

        // 2. 예외 케이스(ex.엣지)
        // - 영역 내 칸이 한개 -> 한칸에 모두 묻힐 수 있나?

        // 3. 알고리즘 선택, 시간 복잡도 계산
        // - bfs, (50 * 50)^3 = 625만
        // - 시간 제한은 몇인가요?
        // - 1초에 1억번이라고 생각해도 괜찮을까요?

        // 4. 구현
        int answer = 0;
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < W; j++) {
                if (map[i][j] == 'W') {
                    continue;
                }
                int tempTreasureLength = getAvailableTreasureLengthBfs(i, j, map);
                answer = Math.max(tempTreasureLength, answer);
            }
        }
        // 5. 일반 케이스 적용
        // 6. 예외 케이스 적용
        System.out.println(answer);
    }

    public static int getAvailableTreasureLengthBfs(int si, int sj, char[][] map) {
        boolean[][] visited = new boolean[map.length][map[0].length];
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(si, sj, 0));
        visited[si][sj] = true;
        int result = 0;
        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            result = Math.max(curNode.cost, result);
            for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
                int ni = curNode.i + di[dirIdx];
                int nj = curNode.j + dj[dirIdx];

                if (ni < 0 || ni >= map.length || nj < 0 || nj >= map[0].length) {
                    continue;
                }
                if (map[ni][nj] == 'W') {
                    continue;
                }
                if (visited[ni][nj]) {
                    continue;
                }

                queue.add(new Node(ni, nj, curNode.cost + 1));
                visited[ni][nj] = true;
            }
        }
        return result;
    }

    static class Node {
        int i;
        int j;
        int cost;

        public Node(int i, int j, int cost) {
            this.i = i;
            this.j = j;
            this.cost = cost;
        }
    }

}