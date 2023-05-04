import java.util.*;

class Solution {
    
    int[][] map;
    
    int answer = Integer.MAX_VALUE;
  
    public int bfs(int n, int[][] wires, int startNode, int[] ignoreLine) {
        LinkedList<Integer> stack = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        int cnt = 1;
        visited[startNode] = true;
        stack.add(startNode);
        while (stack.size() > 0) {
            int curNode = stack.pollLast().intValue();
            for (int nextNode = 1; nextNode <= n; nextNode++) {
                if (visited[nextNode] || map[curNode][nextNode] == 0) {
                    continue;
                }
                if ((ignoreLine[0] == curNode && ignoreLine[1] == nextNode) || (ignoreLine[1] == curNode && ignoreLine[0] == nextNode)) {
                    continue;
                }
               
                visited[nextNode] = true;
                stack.add(nextNode);
                cnt += 1;
            }
        }
        return cnt;
    }
    
    public int solution(int n, int[][] wires) {
        map = new int[n + 1][n + 1];
        for (int[] wire : wires) {
            int u = wire[0];
            int v = wire[1];
            map[u][v] = 1;
            map[v][u] = 1;
        }
        
        for (int i = 0; i < wires.length; i++) {
            int n1 = wires[i][0];
            int n2 = wires[i][1];
            
            int[] ignoreLine = wires[i];
            int result1 = bfs(n, wires, n1, ignoreLine);
            int result2 = bfs(n, wires, n2, ignoreLine);
            answer = Math.min(answer, Math.abs(result1 - result2));
        }
        
        return answer;
    }
}