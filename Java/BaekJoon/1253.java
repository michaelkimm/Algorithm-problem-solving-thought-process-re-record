import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;


class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    int[] numbers = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    Arrays.sort(numbers);
    int answer = 0;

    for (int target_idx = 0; target_idx < N; target_idx++) {
      int left = 0;
      if (left == target_idx)
        left += 1;
      int right = N - 1;
      if (right == target_idx)
        right -= 1;
      while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum < numbers[target_idx]){
          left += 1;
          if (left == target_idx)
            left += 1;
        } else if (sum > numbers[target_idx]) {
          right -= 1;
          if (right == target_idx)
            right -= 1;
        }
        else {
          answer += 1;
          break;
        }
      }
    }
    System.out.println(answer);
  }
}