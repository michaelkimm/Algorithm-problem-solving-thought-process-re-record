import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int E;
    static int EM;
    static int M;
    static int MH;
    static int H;

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bufferedReader.readLine().split(" ");
        E = Integer.parseInt(input[0]);
        EM = Integer.parseInt(input[1]);
        M = Integer.parseInt(input[2]);
        MH = Integer.parseInt(input[3]);
        H = Integer.parseInt(input[4]);

        /*
         * 1. E, M, H를 먼저 배정
         * 2. E가 없으면 EM을 배정, H가 없으면 MH를 배정, M이 없으면 EM과 MH중 크기가 더 큰 것 배정
         * 3. M이 없을 때 EM과 MH 크기가 같을 땐? MH 먼저 배정, 그래야 EM 배정할게 남는다.
         */

        int answer = 0;
        while (decreaseHigh()) {
            answer += 1;
        }
        System.out.println(answer);

    }

    static boolean decreaseHigh() {
        if (H > 0) {
            H -= 1;
            if (decreaseMid()) {
                return true;
            } else {
                H += 1;
                return false;
            }
        } else if (MH > 0) {
            MH -= 1;
            if (decreaseMid()) {
                return true;
            } else {
                MH += 1;
                return false;
            }
        } else {
            return false;
        }
    }

    static boolean decreaseMid() {
        if (M > 0) {
            M -= 1;
            if (decreaseEasy()) {
                return true;
            } else {
                M += 1;
                return false;
            }
        } else {
            if (MH == 0 && EM == 0) {
                return false;
            }
            if (MH >= EM) {
                MH -= 1;
                if (decreaseEasy()) {
                    return true;
                } else {
                    MH += 1;
                    return false;
                }
            } else {
                EM -= 1;
                if (decreaseEasy()) {
                    return true;
                } else {
                    EM += 1;
                    return false;
                }
            }
        }
    }

    static boolean decreaseEasy() {
        if (E > 0) {
            E -= 1;
            return true;
        } else if (EM > 0) {
            EM -= 1;
            return true;
        } else {
            return false;
        }
    }
}
