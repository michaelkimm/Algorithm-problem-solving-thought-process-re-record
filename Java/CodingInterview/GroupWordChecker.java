import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.valueOf(bufferedReader.readLine());

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            String input = bufferedReader.readLine().strip();
            if (isGroupWord(input)) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }

    public static boolean isGroupWord(String s) {
        boolean[] check = new boolean[26];
        int prev = 0;
        boolean answer = true;
        for (int now = 0; now < s.length(); now++) {
            char ch = s.charAt(now);
            if (check[ch - 'a']) {
                if (s.charAt(prev) != ch) {
                    answer = false;
                    break;
                }
            } else {
                check[ch - 'a'] = true;
                prev = now;
            }
        }
        return answer;
    }
}
