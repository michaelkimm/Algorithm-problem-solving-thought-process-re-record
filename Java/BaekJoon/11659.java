import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int[] numbers = new int[N];
        input = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(input[i]);
        }

        int[] cumulativeSum = getCumulativeSum(numbers);

        while (M > 0) {
            input = br.readLine().split(" ");
            int i = Integer.parseInt(input[0]) - 2;
            int j = Integer.parseInt(input[1]) - 1;

            int result = 0;
            if (i >= 0) {
                result = cumulativeSum[j] - cumulativeSum[i];
            } else {
                result = cumulativeSum[j];
            }
            System.out.println(result);
            M--;
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
