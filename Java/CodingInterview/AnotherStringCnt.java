import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String s = bufferedReader.readLine().strip();

        HashSet<String> set = new HashSet<>();
        for (int left = 0; left < s.length(); left++) {
            for (int right = left + 1; right <= s.length(); right++) {
                set.add(s.substring(left, right));
            }
        }
        System.out.println(set.size());
    }
}
