import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int A = Integer.valueOf(input[0]);
        int B = Integer.valueOf(input[1]);


        int answer = 1;
        while (B > A) {
            if (B % 10 == 1) {
                // 예외 처리 필요할 수도 있음
                B /= 10;
            } else if (B % 2 == 0) {
                B >>= 1;
            }
            else {
                break;
            }

            answer += 1;
        }

        System.out.println(A == B ? answer : -1);
    }
}