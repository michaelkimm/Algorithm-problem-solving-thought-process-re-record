import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        // 예제
        // 1 2 3 5 8 13 21

        // 엣지 케이스
        // f(1) -> 1, f(2) -> 2

        // 알고리즘 선정 및 시간복잡도
        // 1. 재귀 : 상위 문제가 하위 문제로 나뉠수 있기 때문, 공간 복잡도
        // - 시간 복잡도 : (재귀 횟수)^깊이 = O(2^k)
        // - 공간 복잡도 : O(N)
        // 2. dp
        // - 시간 복잡도 : O(N)
        // - 공간 복잡도 : O(N)
        // 3. tabulation
        // - 시간 복잡도 : O(N)
        // - 공간 복잡도 : O(1)

        // 구현

        // 예제 적용

        // 엣지 적용
        for (int k = 1; k < 10; k++) {
            int[] dp = new int[k + 1];
            System.out.println(fibonazzi(k, dp));
        }
    }

    public static int fibonazzi(int k) {
        // 탈출 조건
        if (k <= 1) {
            return k;
        }
        // 재귀
        return fibonazzi(k - 1) + fibonazzi(k - 2);
    }

    public static int fibonazzi(int k, int[] dp) {
        // 탈출 조건
        if (k <= 1) {
            dp[k] = k;
            return k;
        } else if (dp[k] > 0) {
            return dp[k];
        }

        // 재귀
        dp[k] = fibonazzi(k - 1, dp) + fibonazzi(k - 2, dp);
        return dp[k];
    }

    public static int tabulation(int k) {
        if (k <= 2) {
            return k;
        }
        int before = 1;
        int beforeBefore = 1;
        int current = 0;
        // for k - 2 번 실행
        for (int i = 0; i < k - 2; i++) {
            current = before + beforeBefore;
            beforeBefore = before;
            before = current;
        }
        return current;
    }
}
