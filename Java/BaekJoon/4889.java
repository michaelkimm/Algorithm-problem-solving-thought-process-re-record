import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        ArrayList<Integer> results = new ArrayList<>();
        while (!(input = br.readLine()).startsWith("-")) {
            results.add(getTransformCnt(input));
        }
        for (int i = 0; i < results.size(); i++) {
            System.out.println(Integer.valueOf(i + 1) + ". " + results.get(i));
        }
    }

    public static int getTransformCnt(String source) {
        LinkedList<Character> stack = new LinkedList<>();
        int cnt = 0;
        for (char ch : source.toCharArray()) {
            if (ch == '{') {
                stack.add(ch);
            } else if (ch == '}') {
                if (stack.size() == 0) {
                    cnt += 1;
                    stack.add('{');
                } else {
                    stack.pollLast();
                }
            }
        }
        return cnt + (int)(stack.size() / 2);
    }
}