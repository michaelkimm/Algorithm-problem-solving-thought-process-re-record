import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine().strip());
        HashMap<String, Integer> map = new HashMap<>();
        while (N > 0) {
            String[] split = bufferedReader.readLine().split("\\.");
            String fileExtension = split[1];
            if (map.containsKey(fileExtension)) {
                map.put(fileExtension, map.get(fileExtension) + 1);
            } else {
                map.put(fileExtension, 1);
            }
            N--;
        }
        ArrayList<Map.Entry<String, Integer>> arrayList = new ArrayList<>(map.entrySet());
        arrayList.sort((o1, o2) -> {
            return o1.getKey().compareTo(o2.getKey());
        });

        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i).getKey() + " " + arrayList.get(i).getValue());
        }

        bufferedReader.close();
    }
}