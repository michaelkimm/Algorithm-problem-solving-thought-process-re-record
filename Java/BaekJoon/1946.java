import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(bufferedReader.readLine().strip());

        while (T > 0) {
            int N = Integer.parseInt(bufferedReader.readLine().strip());
            int[] nodes = new int[N + 1];
            for (int i = 1; i < N + 1; i++) {
                String[] inputs = bufferedReader.readLine().split(" ");
                nodes[Integer.parseInt(inputs[0])] = Integer.parseInt(inputs[1]);
            }
            T -= 1;

            int result = 0;
            int prevTopInterviewRank = Integer.MAX_VALUE;
            for (int i = 1; i < N + 1; i++) {
                int interviewRank = nodes[i];
                if (interviewRank < prevTopInterviewRank) {
                    result += 1;
                    prevTopInterviewRank = interviewRank;
                }
            }
            sb.append(result);
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}