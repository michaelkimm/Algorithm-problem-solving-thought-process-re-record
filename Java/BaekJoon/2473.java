import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    long[] liquids = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
    Arrays.sort(liquids);

    long minValue = Long.MAX_VALUE;
    long[] answer = new long[3];
    for (int left = 0; left <= N - 3; left++) {
      int mid = left + 1;
      int right = N - 1;
      while (mid < right) {
        long mixed = liquids[left] + liquids[mid] + liquids[right];
        long mixedAbs = Math.abs(mixed);
        if (mixedAbs < minValue) {
          minValue = mixedAbs;
          answer[0] = liquids[left];
          answer[1] = liquids[mid];
          answer[2] = liquids[right];
        }
        if (mixed > 0)
          right -= 1;
        else if (mixed < 0)
          mid += 1;
        else
          break;
      }
    }
    System.out.println(answer[0] + " " + answer[1] + " " + answer[2]);
  }

  private static int getMixed(int[] liquids, int left, int right) {
    return liquids[left] + liquids[right];
  }
}