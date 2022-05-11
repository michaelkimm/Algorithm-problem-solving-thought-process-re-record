import java.io.*;
import java.util.*;

class Main {
    public static Long[] borderNums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().strip());


        borderNums = new Long[46342];
        borderNums[0] = 1L;
        for (int i = 1; i < 46342; i++) {
            borderNums[i] = 2 * (Long.valueOf(i) * Long.valueOf(i + 1)) / 2L + 1L;
        }

        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < T; i++) {
            String[] testCase = br.readLine().split(" ");
            int x = Integer.parseInt(testCase[0]);
            int y = Integer.parseInt(testCase[1]);
            results.add(GetMinMovement(x, y));
        }

        for (int i = 0; i < T; i++) {
            System.out.println(results.get(i));
        }
    }
    public static int GetMinMovement(int x, int y) {
        int n = bisectRight(y - x) - 1;
        Long criteria = (borderNums[n] + borderNums[n + 1] - 1L) / 2L;
        int belongedN = n + 1;
        int result;
        if (Long.valueOf(y - x) <= criteria)
            result = 2 * belongedN - 1;
        else
            result = 2 * belongedN;
        return result;
    }

    public static int bisectRight(int key) {
        int mid = 0;
        int low = 0;
        int high = borderNums.length;
        while (low < high) {
            mid = (low + high) / 2;
            if (key < borderNums[mid]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}