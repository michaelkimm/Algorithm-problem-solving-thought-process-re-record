import java.util.*;

class Node {
    int cost;
    int i;
    int j;
    public Node(int cost, int i, int j) {
        this.cost = cost;
        this.i = i;
        this.j = j;    
    }
}

class Solution {
    
    // 동서남북
    static int[] di = { 0, 0, 1, -1 };
    static int[] dj = { 1, -1, 0, 0 };
    
    public int solution(int[][] maps) {
        int answer = -1;
        int N = maps.length;
        int M = maps[0].length;
        
        boolean[][] visited = new boolean[N][M];
        // cost, 현재 위치
        LinkedList<Node> queue = new LinkedList<>();
        queue.add(new Node(1, 0, 0));
        visited[0][0] = true;
        while (queue.size() > 0) {
            Node curNode = queue.pollFirst();
            if (curNode.i == (N - 1) && curNode.j == (M - 1)) {
                answer = curNode.cost;
                break;
            }
            for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
                int ni = curNode.i + di[dirIdx];
                int nj = curNode.j + dj[dirIdx];
                if (ni < 0 || ni >= N || nj < 0 || nj >= M) {
                    continue;
                }
                if (visited[ni][nj]) {
                    continue;
                }
                if (maps[ni][nj] == 0) {
                    continue;
                }
                visited[ni][nj] = true;
                queue.add(new Node(curNode.cost + 1, ni, nj));
            }
        }
        
        
        return answer;
    }
}