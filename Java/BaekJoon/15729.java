import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;
    static int[] list;

    static int[] targetList;

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        N = Integer.parseInt(input);
        list = new int[N];
        targetList = new int[N];
        String[] inputs = bufferedReader.readLine().split(" ");
        for (int i = 0; i < inputs.length; i++) {
            targetList[i] = Integer.parseInt(inputs[i]);
        }
        int answer = 0;
        for (int pt = 0; pt < N; pt++) {
            if (targetList[pt] == list[pt]) {
                continue;
            }
            pressButton(pt);
            answer += 1;
        }
        System.out.println(answer);
    }

    static void pressButton(int idx) {
        int pressedCnt = 0;
        while (pressedCnt < 3 && idx < N) {
            if (list[idx] == 1) {
                list[idx] = 0;
            } else {
                list[idx] = 1;
            }
            idx += 1;
            pressedCnt += 1;
        }
    }
}