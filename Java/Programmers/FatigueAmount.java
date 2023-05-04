import java.util.*;

class Solution {
    
    public static boolean[] visited;
    public static int answer = 0;
    
    public void dfs(int k, int[][] dungeons, int passedCnt) {
    
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i] || k < dungeons[i][0]) {
                continue;
            }        
            visited[i] = true;
            dfs(k - dungeons[i][1], dungeons, passedCnt + 1);
            visited[i] = false;
        }
        answer = Math.max(answer, passedCnt);    
    }
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];    
        dfs(k, dungeons, 0);
        return answer;
    }
}