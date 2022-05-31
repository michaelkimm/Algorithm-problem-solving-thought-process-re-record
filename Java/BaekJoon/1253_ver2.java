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
      int right = 1;
      int sum = numbers[left] + numbers[right];
      if (sum == numbers[target_idx]) {
        answer += 1;
      }
    }
    System.out.println(answer);
  }
}