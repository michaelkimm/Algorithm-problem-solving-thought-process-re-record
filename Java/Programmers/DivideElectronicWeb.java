class Solution {
    
    int[][] map;
    int answer = Integer.MAX_VALUE;
    int tmpResult = 0;
    boolean[] visited;
    
    public void dfs(int n, int[][] wires, int curNode) {
        for (int i = 1; i <= n; i++) {
            if (visited[i]) {
                continue;
            }
            if (map[curNode][i] == 0) {
                continue;
            }
            
            visited[i] = true;
            tmpResult += 1;
            dfs(n, wires, i);
            visited[i] = false;
        }
    }
    
    public int solution(int n, int[][] wires) {
        visited = new boolean[n + 1];
        map = new int[n + 1][n + 1];
        for (int[] wire : wires) {
            int u = wire[0];
            int v = wire[1];
            map[u][v] = 1;
            map[v][u] = 1;
        }
        
        for (int i = 0; i < wires.length; i++) {
            visited[wires[i][0]] = true;
            visited[wires[i][1]] = true;
            map[wires[i][0]][wires[i][1]] = 0;
            map[wires[i][1]][wires[i][0]] = 0;
            
            tmpResult = 1;
            dfs(n, wires, wires[i][0]);
            int result1 = tmpResult;
            tmpResult = 1;
            dfs(n, wires, wires[i][1]);
            int result2 = tmpResult;
            answer = Math.min(answer, Math.abs(result1 - result2));
            
            visited[wires[i][0]] = false;
            visited[wires[i][1]] = false;
            map[wires[i][0]][wires[i][1]] = 1;
            map[wires[i][1]][wires[i][0]] = 1;
        }
        
        
        return answer;
    }
}