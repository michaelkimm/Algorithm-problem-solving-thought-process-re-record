import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    static List<Character> word;
    static List<Integer> underLineIdxList;
    static long answer = 0;

    static Set<Character> vowelSet = Set.of('A', 'E', 'I', 'O', 'U');
    static Set<Character> consonantSet = Set.of('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z');

    public static void recursive(int curIdx, long cnt) {
        if (curIdx >= underLineIdxList.size()) {
            if (word.contains('L')) {
                answer += cnt;
            }
            return;
        }

        if (checkAppendable(word, underLineIdxList.get(curIdx), vowelSet)) {
            word.set(underLineIdxList.get(curIdx), 'A');
            recursive(curIdx + 1, cnt * 5);
            word.set(underLineIdxList.get(curIdx), '_');
        }

        if (checkAppendable(word, underLineIdxList.get(curIdx), consonantSet)) {
            word.set(underLineIdxList.get(curIdx), 'B');
            recursive(curIdx + 1, cnt * 20);
            word.set(underLineIdxList.get(curIdx), '_');
        }

        if (checkAppendable(word, underLineIdxList.get(curIdx), consonantSet)) {
            word.set(underLineIdxList.get(curIdx), 'L');
            recursive(curIdx + 1, cnt);
            word.set(underLineIdxList.get(curIdx), '_');
        }
    }

    private static boolean checkAppendable(List<Character> word, int chIdx, Set<Character> checkSet) {
        // curIdx가 맨 오른쪽, 3개 연속
        if (chIdx >= 2) {
            if (checkSet.contains(word.get(chIdx - 2)) && checkSet.contains(word.get(chIdx - 1))) {
                return false;
            }
        }
        // curIdx가 중간, 3개 연속
        if (chIdx >= 1 && chIdx < word.size() - 1) {
            if (checkSet.contains(word.get(chIdx - 1)) && checkSet.contains(word.get(chIdx + 1))) {
                return false;
            }
        }
        // curIdx가 맨 왼쪽, 3개 연속
        if (chIdx <= word.size() - 3) {
            if (checkSet.contains(word.get(chIdx + 1)) && checkSet.contains(word.get(chIdx + 2))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        word = br.readLine().chars()
                .mapToObj(c -> (char)c)
                .collect(Collectors.toList());

        underLineIdxList = IntStream.range(0, word.size())
                .filter(i -> word.get(i) == '_')
                .boxed()
                .collect(Collectors.toList());

        recursive(0, 1L);
        System.out.println(answer);
    }
}