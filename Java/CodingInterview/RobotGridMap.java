import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;

class Main {
    public static void main(String[] args) throws IOException {
        // 1. 일반 케이스
        // 빈칸 지나가기, RRURURRUR

        // 2. 예외 케이스
        // 그리드 밖, 미로 안에서 움직이기

        // 3. 알고리즘 선정 및 시간 복잡도 분석
        //      1) 목표하는 곳 까지 가능 방법은 그 인접한 칸으로 움직일 수 있는 곳까지 오는 하위 문제로 나눌 수 있다.
        //          -> 재귀로 풀 수 있음
        //          -> 시간 복잡도 : O(함수 내 재귀 발생 횟수)^깊이 = O(2^(m + n))
        //          -> 공간 복잡도 : O(m + n)
        //          -> f(i, j) = f(i - 1, j), f(i, j - 1)
        //      2) 목적지를 '탐색'하는 과정이기 때문에 dps, bfs로 풀 수 있음
        //          -> 시간 복잡도 : O(N*M)
        //          -> 공간 복잡도 : O(1)


        // 4. 구현
        // 스택

        // 5. 일반 케이스 적용
        // 6. 예외 케이스 적용
    }

    public static boolean compute(int i, int j, boolean[][] maze, Set<Point> path) {

        if !(i >= 0 && i < maze.length && j >= 0 && j < maze[0].length) {
            return false;
        }

        if (!(maze[i][j])) {
            return false;
        }

        if ((i == 0 && j == 0) || compute((i - 1), j, maze) || compute(i, j - 1, maze)) {
            path.add(new Point(i, j));
            return true;
        }

        return false;
    }
}
