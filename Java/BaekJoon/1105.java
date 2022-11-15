import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().split(" ");
        int L = Integer.parseInt(inputs[0]);
        int R = Integer.parseInt(inputs[1]);

        int answer = Integer.MAX_VALUE;
        while (L <= R) {
            int cnt = get8Count(L);
            answer = Math.min(cnt, answer);

            int less8CntNum = getLess8CntNum(L);
            if (L == less8CntNum) {
                break;
            } else {
                L = less8CntNum;
            }
        }
        System.out.println(answer);
    }

    static int get8Count(int value) {
        int cnt = 0;
        String valueInString = String.valueOf(value);
        for (int i = 0; i < valueInString.length(); i++) {
            if (valueInString.charAt(i) == '8') {
                cnt += 1;
            }
        }
        return cnt;
    }

    static int getLess8CntNum(int value) {
        char[] chars = String.valueOf(value).toCharArray();
        for (int i = chars.length - 1; i >= 0; i--) {
            if (chars[i] == '8') {
                chars[i] = '9';
                // 이전 값 전부 0
                for (int j = chars.length - 1; j > i; j--) {
                    chars[j] = '0';
                }
                break;
            }
        }
        return Integer.parseInt(String.valueOf(chars));
    }
}