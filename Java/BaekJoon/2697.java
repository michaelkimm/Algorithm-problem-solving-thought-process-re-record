import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        N = Integer.parseInt(input);
        for (int i = 0; i < N; i++) {
            char[] src = bufferedReader.readLine().strip().toCharArray();
            sb.append(getNextNum(src));
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }

    static String getNextNum(char[] srcNumber) {
        int descendStartIdx = -1;
        for (int i = 1; i < srcNumber.length; i++) {
            if (srcNumber[i] > srcNumber[i - 1]) {
                descendStartIdx = i;
            }
        }
        if (descendStartIdx == -1) {
            return "BIGGEST";
        }
        char[] chars = new char[srcNumber.length - descendStartIdx];
        for (int i = 0; i < chars.length; i++) {
            chars[i] = srcNumber[descendStartIdx + i];
        }
        Arrays.sort(chars);

        char src = srcNumber[descendStartIdx - 1];
        int targetIdx = 0;
        for (int i = 0; i < chars.length; i++) {
            if (src < chars[i]) {
                targetIdx = i;
                break;
            }
        }
        char target = chars[targetIdx];
        chars[targetIdx] = src;
        src = target;

        // chars 값 src에 넣기
        for (int i = 0; i < chars.length; i++) {
            srcNumber[descendStartIdx + i] = chars[i];
        }
        srcNumber[descendStartIdx - 1] = src;

        return String.valueOf(srcNumber);
    }
}
