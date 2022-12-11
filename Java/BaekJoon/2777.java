import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int T;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        T = Integer.parseInt(input);
        for (int i = 0; i < T; i++) {
            int src = Integer.parseInt(bufferedReader.readLine().strip());
            sb.append(solution(src));
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }

    static int solution(int srcNumber) {
        if (srcNumber == 1) {
            return 1;
        }
        int div = 9;
        int ret = 0;
        while (div > 1) {
            if (srcNumber % div == 0) {
                srcNumber /= div;
                ret += 1;
                continue;
            }
            div -= 1;
        }
        if (srcNumber != 1) {
            return -1;
        } else {
            return ret;
        }
    }
}
