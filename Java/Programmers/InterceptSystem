import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        
        Arrays.sort(targets, (o1, o2) -> { return o1[0] - o2[0]; });
        int[] curTargetRange = {targets[0][0], targets[0][1]};
        int answer = 1;
        for (int i = 1; i < targets.length; i++) {
            int curS = curTargetRange[0];
            int curE = curTargetRange[1];
            int newS = targets[i][0];
            int newE = targets[i][1];
            if (curE <= newS) {
                curTargetRange[0] = newS;
                curTargetRange[1] = newE;
                answer += 1;
            } else if ((newS < curE) && (newE >= curE)) {
                curTargetRange[0] = newS;
                curTargetRange[1] = curE;
            } else {
                curTargetRange[0] = newS;
                curTargetRange[1] = newE;
            }
        }
        
        return answer;
    }
}