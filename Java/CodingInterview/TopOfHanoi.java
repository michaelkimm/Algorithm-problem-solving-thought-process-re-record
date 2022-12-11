import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;

class Main {
    public static void main(String[] args) throws IOException {
        // 1. 일반 케이스

        // 2. 예외 케이스

        // 3. 알고리즘 선정 및 시간 복잡도 게산
        //  (n개를 source->목표 옮기기) = (n-1개를 source->중간 옮기기) + (아래 1개를 source ->목표 옮기기) + (n -1개를 중간->목표 옮기기)
        //  -> 시간 복잡도 : O(함수 내 재귀 발생 횟수)^깊이 = O(2^n)
        // 4. 구현
        runHanoiTop(3, 1, 2, 3);
        // 5. 일반 케이스 적용

        // 6. 예외 케이스 적용
    }

    public static void runHanoiTop(int n, int source, int intermediate, int target) {
        // 예외 케이스
        if (n <= 0) {
            return;
        }
        runHanoiTop(n - 1, source, target, intermediate);
        System.out.println("Move " + Integer.toString(n) + ' ' + "from " + Integer.toString(source) + " to " + Integer.toString(target));
        runHanoiTop(n - 1, intermediate, source, target);
    }
}
