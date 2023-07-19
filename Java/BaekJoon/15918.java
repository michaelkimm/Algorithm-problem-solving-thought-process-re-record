import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.stream.Collectors;

public class Main {

    static int[] numbers;
    static boolean[] used = new boolean[13];

    static int n;
    static int x;
    static int y;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        n = Integer.valueOf(inputs[0]);
        x = Integer.valueOf(inputs[1]) - 1;
        y = Integer.valueOf(inputs[2]) - 1;
        numbers = new int[2 * n];
        used[y - x - 1] = true;
        numbers[x] = y - x - 1;
        numbers[y] = y - x - 1;

        recursive(0);
        System.out.println(answer);
    }

    private static void recursive(int cIdx) {
        if (cIdx == 2 * n) {
            answer += 1;
            return;
        }
        if (numbers[cIdx] == 0) {
            for (int num = 1; num <= n; num++) {
                if (used[num]) {
                    continue;
                }
                if (cIdx + num + 1 >= 2 * n || numbers[cIdx + num + 1] != 0) {
                    continue;
                }

                used[num] = true;
                numbers[cIdx] = num;
                numbers[cIdx + num + 1] = num;
                recursive(cIdx + 1);
                used[num] = false;
                numbers[cIdx] = 0;
                numbers[cIdx + num + 1] = 0;
            }
        } else {
            recursive(cIdx + 1);
        }
    }
}