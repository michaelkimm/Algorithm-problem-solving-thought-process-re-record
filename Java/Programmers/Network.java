import java.util.*;

class Solution {
    boolean[] visited;
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;
        
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            
            answer += 1;
            
            visited[i] = true;
            LinkedList<Integer> stack = new LinkedList<>();
            stack.add(i);
            while (stack.size() > 0) {
                Integer curNode = stack.pollLast();
                for (int j = 0; j < n; j++) {
                    if (visited[j] || computers[curNode.intValue()][j] == 0) {
                        continue;
                    }
                    visited[j] = true;
                    stack.add(j);
                }
            }
            
        }
        
        return answer;
    }
}