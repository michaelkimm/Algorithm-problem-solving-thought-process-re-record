import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) throws IOException {
        // {25,10,5,1}
        // 1. 일반 케이스
        // 1 -> {0,0,0,1}
        // 2 -> {0,0,0,2}
        // 6 -> {0,0,0,6}, {0,0,1,1}

        // 2. 예외 케이스

        // 3. 알고리즘 선택 및 시간복잡도 계산
        // 재귀
        // -> n원을 만드는 경우 = [(n - 1원) 만드는 경우 + {0,0,0,1}] + [(n - 5원) 만드는 경우 + {0,0,1,0}] + [(n - 10원) 만드는 경우 + {0,1,0,0}] + ..
        // -> 매모이제이션 ->
        // 4. 구현
        // 5. 일반 케이스 적용
        for (int cost = 1; cost < 10; cost++) {
            System.out.println("case : " + Integer.toString(cost));
            int[] cache = new int[cost + 1];
            System.out.println(getAllMakableCombinations(cost, cache));
            System.out.println(calculateChangeMemoization(cost));
            System.out.println("================");
        }
        // 6. 예외 케이스 적용
    }

    public static int[] coinType = {1, 5, 10, 25};

    public static int getAllMakableCombinations(int cost, int[] cache) {
        // 탈출 조건

        if (cost == 1) {
            return 1;
        } else if (cost == 0) {
            return 0;
        } else if (cost < 0) {
            return -1;
        }

        if (cache[cost] > 0) {
            return cache[cost];
        }

        // 재귀
        int ret = 0;
        for (int i = 0; i < coinType.length; i++) {
            int newCost = cost - coinType[i];
            int makableCnt = getAllMakableCombinations(newCost, cache);
            if (makableCnt == -1) {
                continue;
            }

            ret += (makableCnt + 1);
        }

        cache[cost] = ret;
        return ret;
    }

    public static int calculateChangeMemoization(int n) {
        int[] coins = {25, 10, 5, 1};
        int[][] cache = new int[n + 1][coins.length];
        return calculateChangeMemoization(n, coins, 0, cache);
    }

    public static int calculateChangeMemoization(int amount, int[] coins, int position, int[][] cache) {
        if (cache[amount][position] > 0) {
            return cache[amount][position];
        }
        if (position >= coins.length - 1) {
            return 1;
        }

        int coin = coins[position];
        int count = 0;
        for (int i = 0; i * coin <= amount; i++)  {
            int remaining = amount - i * coin;
            count += calculateChangeMemoization(remaining, coins, position + 1, cache);
        }

        cache[amount][position] = count;
        return count;
    }
}
