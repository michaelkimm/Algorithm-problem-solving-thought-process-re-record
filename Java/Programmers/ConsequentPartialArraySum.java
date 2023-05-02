import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0, 0};
        int answerLength = Integer.MAX_VALUE;
        int[] dp = new int[sequence.length];
        dp[0] = sequence[0];
        for (int i = 1; i < sequence.length; i++) {
            dp[i] = dp[i - 1] + sequence[i];
        }
        int left = -1;
        int right = 0;
        
        while (left < sequence.length && right < sequence.length) {
            int partialArraySum = dp[right];
            if (left != -1) {
                partialArraySum -= dp[left];
            }
            if (partialArraySum == k) {
                int newAnswerLength = right - (left + 1) + 1;
                if (answerLength <= newAnswerLength) {
                    right += 1;
                    continue;
                }
                answer[0] = left + 1;
                answer[1] = right;
                answerLength = newAnswerLength;
                right += 1;
            } else if (partialArraySum < k) {
                right += 1;
            } else {
                left += 1;
            }
        }
        return answer;
    }
}