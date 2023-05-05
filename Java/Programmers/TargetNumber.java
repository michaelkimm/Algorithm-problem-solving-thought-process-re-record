class Solution {
    static int N;
    static int answer = 0;
    static int globalTarget = 0;
    
    void dfs(int[] numbers, int total, int operCnt) {
        if (operCnt == N) {
            if (total == globalTarget) {
                answer += 1;
            }
            return;
        }
        
        for (int i = 0; i < 2; i++) {
            char operation = "+-".charAt(i);
            int tmpTotal = 0;
            if (operation == '+') {
                tmpTotal = total + numbers[operCnt];
            } else if (operation == '-') {
                tmpTotal = total - numbers[operCnt];
            }
            dfs(numbers, tmpTotal, operCnt + 1);
        }
    }
    
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        globalTarget = target;
        dfs(numbers, 0, 0);
        return answer;
    }
}