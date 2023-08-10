import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    static int n;
    static StringBuffer sb = new StringBuffer();
    static char[] operations = {' ', '+', '-'};

    public static int calculate(String equation) {
        equation = equation.replaceAll(" ", "");
        String[] nums = equation.split("[+-]");
        String[] operations = equation.split("[0-9]+");

        int sum = Integer.valueOf(nums[0]);
        for (int i = 1; i < operations.length; i++) {
            if (operations[i].equals("+")) {
                sum += Integer.valueOf(nums[i]);
            } else {
                sum -= Integer.valueOf(nums[i]);
            }
        }
        return sum;
    }

    public static void recursive(int cNum) {
        if (cNum == n + 1) {
            String equation = sb.toString();
            if (calculate(equation) == 0) {
                System.out.println(equation);
            }
            return;
        }

        for (int i = 0; i < operations.length; i++) {
            char operation = operations[i];
            sb.append(operation);
            sb.append(cNum++);
            recursive(cNum);
            sb.delete(sb.length() - 2, sb.length());
            cNum--;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer count = Integer.valueOf(br.readLine().strip());
        sb.append(1);
        for (int i = 0; i < count; i++) {
            n = Integer.valueOf(br.readLine().strip()).intValue();
            recursive(2);
            System.out.println();
        }
    }
}