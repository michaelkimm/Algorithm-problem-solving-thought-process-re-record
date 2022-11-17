import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine().strip());
        int K = Integer.parseInt(bufferedReader.readLine().strip());
        Integer[] sensors = new Integer[N];
        String[] inputs = bufferedReader.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            sensors[i] = Integer.parseInt(inputs[i]);
        }
        Arrays.sort(sensors);

        Integer[] distances = new Integer[N - 1];
        for (int i = 1; i < N; i++) {
            distances[i - 1] = sensors[i] - sensors[i - 1];
        }
        Arrays.sort(distances, Collections.reverseOrder());

        if (K >= N) {
            System.out.println(0);
            return;
        }

        // k = 1인 경우
        Integer sum = Arrays.stream(distances)
                .reduce(0, Integer::sum);
        K -= 1;

        for (int i = 0; i < K; i++) {
            sum -= distances[i];
        }

        System.out.println(sum);
    }
}