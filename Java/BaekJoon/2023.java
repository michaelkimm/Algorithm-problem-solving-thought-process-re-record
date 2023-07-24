import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    static int N;
    static LinkedList<Integer> stack = new LinkedList<>();
    static List<Integer> answers = new ArrayList<>();

    public static boolean isPrimeNumber(int value) {
        if (value == 1) {
            return false;
        }
        if (value == 2 || value == 3 || value == 5 || value == 7) {
            return true;
        }
        for (int i = 2; i <= (int)Math.sqrt(value); i++) {
            if (value % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static Integer stackToInteger(List<Integer> stack) {
        String collected = stack.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
        return Integer.valueOf(collected);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.valueOf(br.readLine().strip());

        recursive(0);
        Collections.sort(answers);
        answers.forEach(System.out::println);
    }

    private static void recursive(int curSize) {
        if (curSize == N) {
            answers.add(stackToInteger(stack));
            return;
        }

        for (int i = 1; i < 10; i++) {
            stack.add(i);
            if (makesCoolPrimeNumber(stack)) {
                recursive(curSize + 1);
            }
            stack.pollLast();
        }
    }

    private static boolean makesCoolPrimeNumber(LinkedList<Integer> stack) {
        Integer integer = stackToInteger(stack);
        return isPrimeNumber(integer);
    }
}