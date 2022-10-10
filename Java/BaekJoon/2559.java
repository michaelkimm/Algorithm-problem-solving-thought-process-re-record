import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);

        input = br.readLine().split(" ");
        int[] temperatures = new int[N];
        for (int i = 0; i < N; i++) {
            temperatures[i] = Integer.parseInt(input[i]);
        }

        int[] culmulativeSum = getCumulativeSum(temperatures);

        int left = -1;
        int right = K - 1;
        int maxTemperatureSum = Integer.MIN_VALUE;
        while (right < N) {
            int sum = 0;
            if (left >= 0) {
                sum = culmulativeSum[right] - culmulativeSum[left];
            } else {
                sum = culmulativeSum[right];
            }
            maxTemperatureSum = sum > maxTemperatureSum ? sum : maxTemperatureSum;
            left += 1;
            right += 1;
        }

        System.out.println(maxTemperatureSum);
    }

    public static int[] getCumulativeSum(int[] ary) {
        int[] dp = new int[ary.length];
        for (int i = 0; i < ary.length; i++) {
            if (i == 0) {
                dp[i] = ary[0];
                continue;
            }
            dp[i] = dp[i - 1] + ary[i];
        }
        return dp;
    }
}