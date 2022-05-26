import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {

  static int N;
  static List<Long> liquids;
  static Long[] answer;
  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    liquids = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).boxed().collect(Collectors.toList());
    Collections.sort(liquids);

    liquids.stream().forEach(System.out::println);
    answer = new Long[2];

    int left = 0;
    int right = 1;
    long minValue = Long.MAX_VALUE;
    // left fixed, right move right
    while (right < liquids.size()) {
      long mixed = getMixed(left, right);

      if (mixed < minValue) {
        minValue = mixed;
        right += 1;
      }
      else
        break;
    }
    right -= 1;
    updateAnswer(left, right);

    // left move right, right move left
    while (left < liquids.size()) {
      // left move right
      left += 1;
      // right move left until mixed is bigger than minValue
      long mixed = getMixed(left, right);
      while (mixed > minValue ||) {
        right -= 1;
        mixed = getMixed(left, right);
      }
      right += 1;
      updateAnswer(left, right);
    }

    System.out.println("left = " + left);
    System.out.println("right = " + right);
    System.out.println("minValue = " + minValue);
  }

  private static void updateAnswer(int left, int right) {
    answer[0] = liquids.get(left);
    answer[1] = liquids.get(right);
  }

  private static long getMixed(int left, int right) {
    long mixed = Math.abs(liquids.get(left) + liquids.get(right));
    return mixed;
  }
}