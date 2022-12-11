import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {
    static int L;
    static int C;
    static char[] alphabets;
    static char[] collected;
    static StringBuilder stringBuilder = new StringBuilder();
    static Set<Character> vowel = new HashSet(Arrays.asList('a', 'e', 'i', 'o', 'u'));

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bufferedReader.readLine().split(" ");
        L = Integer.parseInt(input[0]);
        C = Integer.parseInt(input[1]);

        alphabets = Arrays.stream(bufferedReader.readLine().split(" "))
                .collect(Collectors.joining())
                .toCharArray();
        Arrays.sort(alphabets);
        collected = new char[L];

        permutation(-1, 0);
        System.out.println(stringBuilder.toString());
    }

    static void permutation(int before, int depth) {
        if (depth == L) {
            if (!meetCondition()) {
                return;
            }
            stringBuilder.append(collected);
            stringBuilder.append('\n');
            return;
        }

        for (int i = before + 1; i < C; i++) {
            collected[depth] = alphabets[i];
            permutation(i, depth + 1);
        }
        return;
    }

    static boolean meetCondition() {
        int vowelCnt = 0;
        int nonVowelCnt = 0;

        for (char c : collected) {
            if (vowel.contains(c)) {
                vowelCnt += 1;
            } else {
                nonVowelCnt += 1;
            }
        }
        if (vowelCnt == 0 || nonVowelCnt <= 1) {
            return false;
        }
        return true;
    }
}