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
        char[] S = bufferedReader.readLine().strip().toCharArray();
        char[] T = bufferedReader.readLine().strip().toCharArray();

        // 0번 누르는 경우
        char[] tmpS1 = S.clone();
        press(tmpS1, 0);
        int answer1 = getMinCnt(tmpS1, T, 1);
        // 0번 누르지 않는 경우
        char[] tmpS2 = S.clone();
        int answer2 = getMinCnt(tmpS2, T, 0);
        // 둘다 -1이면 -1뱉기
        if (answer1 == -1 && answer2 == -1) System.out.println(-1);
        else if (answer1 == -1) System.out.println(answer2);
        else if (answer2 == -1) System.out.println(answer1);
        else System.out.println(Math.min(answer1, answer2));
    }

    public static int getMinCnt(char[] ary, char[] target, int pressStartCnt) {
        int pressedCnt = pressStartCnt;
        for (int curPt = 1; curPt < ary.length; curPt++) {
            if (ary[curPt - 1] == target[curPt - 1]) {
                continue;
            } else {
                press(ary, curPt);
                pressedCnt += 1;
            }
        }

        if (String.valueOf(ary).equals(String.valueOf(target))) {
            return pressedCnt;
        } else {
            return -1;
        }
    }

    public static void press(char[] bulbs, int pressedpt) {
        if (pressedpt != 0) {
            bulbs[pressedpt - 1] = getFlipedState(bulbs[pressedpt - 1]);
        }
        bulbs[pressedpt] = getFlipedState(bulbs[pressedpt]);
        if (pressedpt != bulbs.length - 1) {
            bulbs[pressedpt + 1] = getFlipedState(bulbs[pressedpt + 1]);
        }
        return;
    }

    public static char getFlipedState(char state) {
        return state == '1' ? '0' : '1';
    }
}