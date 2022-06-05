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
    Arrays.sort(numbers);

    int maxNumber = numbers[numbers.length - 1];
    long[] f = new long[maxNumber + 1];
    for (int num = 1; num <= maxNumber; num++) {
      f[num] = getDivisorSum((long)num);
    }

    // cumulative sum
    long[] cumulativeSum = new long[maxNumber + 1];
    for (int num = 1; num <= maxNumber; num++) {
      cumulativeSum[num] = cumulativeSum[num - 1];
      cumulativeSum[num] += f[num];
    }

    for (int i = 0; i < numbers.length; i++) {
      System.out.println(cumulativeSum[numbers[i]]);
    }
  }

  static long getDivisorSum(long number) {
    long sum = 0L;
    for (long divNum = 1; divNum * divNum <= number; divNum++) {
      if (number % divNum == 0) {
        if (divNum == number / divNum)
          sum += divNum;
        else
          sum += (divNum + number / divNum);
      }
    }
    return sum;
  }
}