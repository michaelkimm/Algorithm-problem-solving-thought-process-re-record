import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int[] liquids = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    Arrays.sort(liquids);

    int ans1 = 0;
    int ans2 = 0;
    int left = 0;
    int right = N - 1;
    int minValue = Integer.MAX_VALUE;
    while (left < right) {
      int mixed = getMixed(liquids, left, right);
      int mixedAbs = Math.abs(mixed);
      if (mixedAbs < minValue) {
        minValue = mixedAbs;
        ans1 = liquids[left];
        ans2 = liquids[right];
      }

      if (mixed > 0)
        right -= 1;
      else
        left += 1;
    }

    System.out.println(ans1 + " " + ans2);
  }

  private static int getMixed(int[] liquids, int left, int right) {
    return liquids[left] + liquids[right];
  }
}