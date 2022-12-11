import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int X = Integer.parseInt(input[1]);

        input = br.readLine().split(" ");
        int[] visitorCnt = new int[N];
        for (int i = 0; i < N; i++) {
            visitorCnt[i] = Integer.parseInt(input[i]);
        }

        int[] cumulativeSum = getCumulativeSum(visitorCnt);
        int left = -1;
        int right = X - 1;
        int maxSum = 0;
        int maxSumCnt = 0;
        while (right < N) {
            int result = 0;
            if (left >= 0) {
                result = cumulativeSum[right] - cumulativeSum[left];
            } else {
                result = cumulativeSum[right];
            }
            if (result > maxSum) {
                maxSum = result;
                maxSumCnt = 1;
            } else if (result == maxSum) {
                maxSumCnt += 1;
            }
            left += 1;
            right += 1;
        }
        if (maxSum == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(maxSum);
            System.out.println(maxSumCnt);
        }
    }

    public static int[] getCumulativeSum(int[] ary) {
        int[] dp = new int[ary.length];
        for (int i = 0; i < ary.length; i++) {
            if (i == 0) {
                dp[i] = ary[i];
                continue;
            }
            dp[i] = dp[i - 1] + ary[i];
        }
        return dp;
    }
}
