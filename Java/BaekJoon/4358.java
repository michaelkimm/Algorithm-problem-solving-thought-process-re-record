import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        TreeSet<String> treeSet = new TreeSet<>();
        HashMap<String, Integer> map = new HashMap<>();
        String input;
        int totalCnt = 0;
        while ((input = br.readLine()) != null && input.length() > 0) {
            totalCnt += 1;
            treeSet.add(input);
            map.put(input, map.getOrDefault(input, 0) + 1);
        }

        for (String name : treeSet) {
            double ratio = (double)map.get(name) / totalCnt * 100;
            System.out.println(name + " " + String.format("%.4f", ratio));
        }
        br.close();
    }
}