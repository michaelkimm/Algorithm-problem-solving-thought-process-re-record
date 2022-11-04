import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static class Node {
        int ri;
        int rj;
        int bi;
        int bj;
        int moveCnt;

        public Node(int ri, int rj, int bi, int bj, int moveCnt) {
            this.ri = ri;
            this.rj = rj;
            this.bi = bi;
            this.bj = bj;
            this.moveCnt = moveCnt;
        }
    }

    // 상하좌우
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};

    static int N;
    static int M;
    static int ei;
    static int ej;
    static char[][] board;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.valueOf(input[0]);
        M = Integer.valueOf(input[1]);

        board = new char[N][M];
        int ri = 0;
        int rj = 0;
        int bi = 0;
        int bj = 0;
        for (int i = 0; i < N; i++) {
            char[] chars = br.readLine().strip().toCharArray();
            for (int j = 0; j < M; j++) {
                board[i][j] = chars[j];
                if (board[i][j] == 'O') {
                    ei = i;
                    ej = j;
                } else if (board[i][j] == 'R') {
                    ri = i;
                    rj = j;
                } else if (board[i][j] == 'B') {
                    bi = i;
                    bj = j;
                }
            }
        }

        Node startNode = new Node(ri, rj, bi, bj, 0);
        Queue<Node> queue = new LinkedList<>();
        queue.add(startNode);
        boolean[][][][] visited = new boolean[N][M][N][M];
        visited[ri][rj][bi][bj] = true;
        int answer = -1;
        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int cri = curNode.ri;
            int crj = curNode.rj;
            int cbi = curNode.bi;
            int cbj = curNode.bj;
            if (curNode.ri == ei && curNode.rj == ej) {
                answer = curNode.moveCnt;
                break;
            }
            for (int idx = 0; idx < 4; idx++) {
                int nri = cri;
                int nrj = crj;
                int nbi = cbi;
                int nbj = cbj;
                boolean redInHole = false;
                boolean blueInHole = false;
                // 빨강 굴리기
                while (board[nri][nrj] != '#') {
                    nri += di[idx];
                    nrj += dj[idx];
                    if (board[nri][nrj] == 'O') {
                        redInHole = true;
                        break;
                    }
                }
                if (!redInHole) {
                    nri -= di[idx];
                    nrj -= dj[idx];
                }
                // 파랑 굴리기
                while (board[nbi][nbj] != '#') {
                    nbi += di[idx];
                    nbj += dj[idx];
                    if (board[nbi][nbj] == 'O') {
                        blueInHole = true;
                        break;
                    }
                }
                if (!blueInHole) {
                    nbi -= di[idx];
                    nbj -= dj[idx];
                }
                // 위로 갈 경우
                if (idx == 0) {
                    // 빨강이 파랑보다 위에 있던 경우
                    if (cri < cbi) {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nbi += 1;
                        }
                    } else {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nri += 1;
                        }
                    }
                } else if (idx == 1) {
                    // 파랑이 빨강보다 아래에 있을 경우
                    if (cri < cbi) {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nri -= 1;
                        }
                    } else {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nbi -= 1;
                        }
                    }
                } else if (idx == 2) {
                    // 빨강이 파랑보다 왼쪽에 있는 경우
                    if (crj < cbj) {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nbj += 1;
                        }
                    } else {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nrj += 1;
                        }
                    }
                } else if (idx == 3) {
                    // 파랑이 빨강보다 오른쪽에 있는 경우
                    if (crj < cbj) {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nrj -= 1;
                        }
                    } else {
                        // 움직인 후 위치가 같아진 경우
                        if (nri == nbi && nrj == nbj) {
                            nbj -= 1;
                        }
                    }
                }

                if (blueInHole) {
                    continue;
                }
                if (!visited[nri][nrj][nbi][nbj]) {
                    if (curNode.moveCnt + 1 > 10) {
                        continue;
                    }
                    Node nextNode = new Node(nri, nrj, nbi, nbj, curNode.moveCnt + 1);
                    queue.add(nextNode);
                    visited[nri][nrj][nbi][nbj] = true;
                }

            }
        }
        System.out.println(answer);
    }
}