import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {
    static int N;
    static int K;

    static int answer = 0;

    static HashSet<Integer> mustNeededAlphabets = new HashSet(Arrays.asList(97, 99, 105, 110, 116));

    static boolean[] alphabetUsed = new boolean[26];

    static ArrayList<String> wordList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().split(" ");
        N = Integer.valueOf(inputs[0]);
        K = Integer.valueOf(inputs[1]);
        for (int i = 0; i < N; i++) {
            String input = bufferedReader.readLine().strip();
            wordList.add(input);
        }
        if (K < 5) {
            System.out.println(0);
            return;
        }

        K -= 5;
        // antic
        for (Integer alphabetInteger : mustNeededAlphabets) {
            alphabetUsed[alphabetInteger.intValue() - 97] = true;
        }

        permutation(-1, 0);
        System.out.println(answer);
    }

    static void permutation(int before, int depth) {
        if (depth == K) {
            int readableWordCnt = getReadableWordCnt();
            answer = Math.max(answer, readableWordCnt);
            return;
        }

        for (int i = before + 1; i < 26; i++) {
            if (mustNeededAlphabets.contains(i + 97)) {
                continue;
            }
            alphabetUsed[i] = true;
            permutation(i, depth + 1);
            alphabetUsed[i] = false;
        }
    }

    static int getReadableWordCnt() {
        int ret = 0;
        for (String word : wordList) {
            ret += 1;
            for (int i = 4; i <= word.length() - 5; i++) {
                int charAscii = (int) word.charAt(i) - 97;
                if (!alphabetUsed[charAscii]) {
                    ret -= 1;
                    break;
                }
            }
        }
        return ret;
    }

}