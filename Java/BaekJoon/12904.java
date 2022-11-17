import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String S = bufferedReader.readLine().strip();
        String T = bufferedReader.readLine().strip();

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(T);
        int answer = 0;
        while (stringBuilder.length() > 0) {
            int idx = stringBuilder.length() - 1;
            char lastChar = stringBuilder.charAt(idx);
            if (lastChar == 'B') {
                stringBuilder.deleteCharAt(idx);
                stringBuilder.reverse();
            } else {
                stringBuilder.deleteCharAt(idx);
            }
            if (stringBuilder.toString().equals(S)) {
                answer = 1;
                break;
            }
        }
        System.out.println(answer);
    }
}