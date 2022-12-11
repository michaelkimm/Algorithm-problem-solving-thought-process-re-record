import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;

class Main {
    public static void main(String[] args) {
        System.out.println(solution("bbaabd"));
    }

    public static String solution(String source) {
        String dest = "";
        while (source.length() != 0) {
            char[] chars = source.toCharArray();
            // 알파벳 종류 구하기
            HashSet<Character> characters = new HashSet<Character>();
            for (char c : chars){
                characters.add(c);
            }
            // source에서 알파벳 없애기
            StringBuilder stringBuilder = new StringBuilder(source);
            for (Character c : characters) {
                int indexOf = source.indexOf(c.toString());
                source = source.substring(0, indexOf) + source.substring(indexOf + 1);
            }

            // dest에 알파벳 붙이기
            chars = new char[characters.size()];
            ArrayList<Character> characterArrayList = new ArrayList<Character>();
            characterArrayList.addAll(characters);
            characterArrayList.sort(Comparator.naturalOrder());
            String result = characterArrayList.stream()
                    .map(e -> e.toString())
                    .reduce((ret, e) -> ret + e)
                    .get();
            dest += result;
        }
        return dest;
    }
}
