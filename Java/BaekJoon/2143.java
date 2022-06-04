import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    long T = Long.parseLong(br.readLine());
    int N = Integer.parseInt(br.readLine());
    String[] ns = br.readLine().split(" ");
    long[] A = new long[N];
    for (int i = 0; i < N; i++) {
      A[i] = Long.parseLong(ns[i]);
    }

    int M = Integer.parseInt(br.readLine());
    String[] ms = br.readLine().split(" ");
    long[] B = new long[M];
    for (int i = 0; i < M; i++) {
      B[i] = Long.parseLong(ms[i]);
    }

    long[] cumulativeA = getCumulative(A);
    long[] ccA = getRangeSum(cumulativeA);
    long[] cumulativeB = getCumulative(B);
    long[] ccB = getRangeSum(cumulativeB);

    long answer = 0;
    int left = 0;
    int right = ccB.length - 1;
    int leftCnt = 0;
    int rightCnt = 0;
    while (left < ccA.length && right >= 0) {
      long sum = ccA[left] + ccB[right];
      if (sum == T) {
        // move right
        while (sum == T) {
          rightCnt += 1;
          right -= 1;
          if (right < 0)
            break;
          sum = ccA[left] + ccB[right];
        }
        right += 1;
        // move left
        sum = ccA[left] + ccB[right];
        while (sum == T) {
          leftCnt += 1;
          left += 1;
          if (left >= ccA.length)
            break;
          sum = ccA[left] + ccB[right];
        }
        left -= 1;
        answer += ((long)rightCnt * (long)leftCnt);
        right -= 1;
      } else if (sum > T) {
        right -= 1;
      } else if (sum < T) {
        left += 1;
      }
      leftCnt = 0;
      rightCnt = 0;
    }

    System.out.println(answer);
  }

  private static long[] getRangeSum(long[] ary) {
    int N = ary.length;
    long[] result = new long[(N * (N - 1)) / 2];
    int idx = 0;
    for (int left = 0; left < N; left++) {
      for (int right = left + 1; right < N; right++) {
        result[idx++] = (ary[right] - ary[left]);
      }
    }
    Arrays.sort(result);
    return result;
  }

  private static long[] getCumulative(long[] ary) {
    long[] cumulative = new long[ary.length + 1];
    for (int i = 1; i <= ary.length; i++) {
      cumulative[i] = cumulative[i - 1];
      cumulative[i] += ary[i - 1];
    }
    return cumulative;
  }
}