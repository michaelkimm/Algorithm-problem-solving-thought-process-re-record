import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.stream.Collectors;

public class Main {

    static Set<String> visited = new HashSet<>();
    static int answer = 0;
    static String nString;
    static LinkedList<Character> deque = new LinkedList<>();
    static LinkedList<String> stack = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        nString = br.readLine().strip();
        for (char c : nString.toCharArray()) {
            deque.add(c);
        }

        recursive();
        System.out.println(answer);
    }

    private static String convertToStringByStack(LinkedList<String> stack) {
        StringBuilder sb = new StringBuilder();
        stack.stream()
                .forEach(s -> sb.append(s));
        return sb.toString();
    }

    static String convertToString(LinkedList<Character> deque) {
        return deque.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
    }

    private static void recursive() {
        if (deque.size() == 0) {
            answer += 1;
            return;
        }

        // 앞 빼기
        Character polled = deque.pollFirst();
        if (!visited.contains(convertToStringByStack(stack))) {
            System.out.println(convertToStringByStack(stack));
            visited.add(convertToStringByStack(stack));
            stack.addLast(convertToString(deque));
            recursive();
            stack.pollLast();
        }
        deque.addFirst(polled);

        // 뒤 빼기
        polled = deque.pollLast();
        if (!visited.contains(convertToStringByStack(stack))) {
            System.out.println(convertToStringByStack(stack));
            visited.add(convertToStringByStack(stack));
            stack.addLast(convertToString(deque));
            recursive();
            stack.pollLast();
        }
        deque.addLast(polled);
    }
}