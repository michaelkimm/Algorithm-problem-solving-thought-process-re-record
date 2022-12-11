import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String input = bufferedReader.readLine().strip();
        int N = Integer.parseInt(input);
        char[] balls = bufferedReader.readLine().strip().toCharArray();

        // 빨강, 파랑 볼 개수 세기
        int blueCnt = 0;
        int redCnt = 0;
        for (int i = 0; i < N; i++) {
            if (balls[i] == 'B') {
                blueCnt += 1;
            } else {
                redCnt += 1;
            }
        }
        
        // 개수가 적은 공 옮기기
        int answer = Math.min(redCnt, blueCnt);

        // 왼쪽으로 전부 모으는 경우
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if (balls[i] == balls[0]) {
                cnt += 1;
            } else {
                break;
            }
        }
        if (balls[0] == 'R') {
            answer = Math.min(redCnt - cnt, answer);
        } else {
            answer = Math.min(blueCnt - cnt, answer);
        }

        // 오른쪽으로 전부 모으는 경우
        cnt = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (balls[i] == balls[N - 1]) {
                cnt += 1;
            } else {
                break;
            }
        }
        if (balls[N - 1] == 'R') {
            answer = Math.min(redCnt - cnt, answer);
        } else {
            answer = Math.min(blueCnt - cnt, answer);
        }

        System.out.println(answer);
    }
}