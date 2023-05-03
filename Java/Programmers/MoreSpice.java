import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Arrays.stream(scoville).forEach(sco -> {
           pq.offer(sco); 
        });

        int answer = 0;
        while (pq.size() >= 2 && pq.peek() < K) {
            int weakestVal = pq.poll();
            int secondWeakestVal = pq.poll();
            int newVal = weakestVal + 2 * secondWeakestVal;
            pq.offer(newVal);
            answer += 1;
        }
        
        
        if (pq.size() <= 1 && pq.peek() < K) {
            answer = -1;
        }        
        
        return answer;
    }
}