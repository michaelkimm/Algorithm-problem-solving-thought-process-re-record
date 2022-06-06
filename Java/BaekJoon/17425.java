import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine().strip());
    int[] numbers = new int[T];


    for (int i = 0; i < T; i++) {
      int value = Integer.parseInt(br.readLine());
      numbers[i] = value;
    }

    int MAX_VALUE = Arrays.stream(numbers).max().getAsInt() + 1;

    // get fx
    long[] f = new long[MAX_VALUE];
    Arrays.fill(f, 1L);
    for (int num = 2; num < f.length; num++) {
      for (int i = 1; i * num < f.length; i++) {
        f[num * i] += num;
      }
    }

    // cumulative sum
    long[] cumulativeSum = new long[MAX_VALUE];
    for (int num = 1; num < cumulativeSum.length; num++) {
      cumulativeSum[num] += (cumulativeSum[num - 1] + f[num]);
    }

    StringBuffer sb = new StringBuffer();
    for (int i = 0; i < numbers.length; i++) {
//      System.out.println(cumulativeSum[numbers[i]]);
      sb.append(cumulativeSum[numbers[i]]).append("\n");
    }
    System.out.println(sb);
  }
}