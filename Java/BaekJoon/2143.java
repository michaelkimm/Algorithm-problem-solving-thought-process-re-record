import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    int N = Integer.parseInt(br.readLine());
    String[] ns = br.readLine().split(" ");
    int[] A = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(ns[i]);
    }

    int M = Integer.parseInt(br.readLine());
    String[] ms = br.readLine().split(" ");
    int[] B = new int[M];
    for (int i = 0; i < M; i++) {
      B[i] = Integer.parseInt(ms[i]);
    }

    int[] cumulativeA = getCumulative(A);
    int[] ccA = getRangeSum(cumulativeA);
    int[] cumulativeB = getCumulative(B);
    int[] ccB = getRangeSum(cumulativeB);

//    System.out.println("cca");
//    printAry(ccA);
//
//    System.out.println("ccb");
//    printAry(ccB);

    Map<Integer, Integer> ccAfreqMap = getNumberFrequency(ccA);
    Map<Integer, Integer> ccBfreqMap = getNumberFrequency(ccB);

    Set<Integer> ccANumSet = new HashSet<>(Arrays.stream(ccA).boxed().collect(Collectors.toList()));
    List<Integer> ccAUniqNums = ccANumSet.stream().collect(Collectors.toList());
    Collections.sort(ccAUniqNums);
    Set<Integer> ccBNumSet = new HashSet<>(Arrays.stream(ccB).boxed().collect(Collectors.toList()));
    List<Integer> ccBUniqNums = ccBNumSet.stream().collect(Collectors.toList());
    Collections.sort(ccBUniqNums);

//    System.out.println("ccAUniqNums");
//    printAry(ccAUniqNums);
//    printMap(ccAfreqMap);
//    System.out.println();
//
//
//    System.out.println("ccBUniqNums");
//    printAry(ccBUniqNums);
//    printMap(ccBfreqMap);
//    System.out.println();

    int answer = 0;
    int left = 0;
    int right = ccBUniqNums.size() - 1;
    while (left < ccAUniqNums.size() && right >= 0) {
      int leftNum = ccAUniqNums.get(left);
      int rightNum = ccBUniqNums.get(right);
      int sum = leftNum + rightNum;
      if (sum == T) {
        answer += ccAfreqMap.get(leftNum) * ccBfreqMap.get(rightNum);
        right -= 1;
      } else if (sum > T) {
        right -= 1;
      } else if (sum < T) {
        left += 1;
      }
    }

    System.out.println(answer);
  }

  private static int[] getRangeSum(int[] ary) {
    int N = ary.length;
    int[] result = new int[(N * (N - 1)) / 2];
    int idx = 0;
    for (int left = 0; left < N; left++) {
      for (int right = left + 1; right < N; right++) {
        result[idx++] = (ary[right] - ary[left]);
      }
    }
    Arrays.sort(result);
    return result;
  }

  private static int[] getCumulative(int[] ary) {
    int[] cumulative = new int[ary.length + 1];
    for (int i = 1; i <= ary.length; i++) {
      cumulative[i] = cumulative[i - 1];
      cumulative[i] += ary[i - 1];
    }
    return cumulative;
  }

  private static Map<Integer, Integer> getNumberFrequency(int[] ary) {
    HashMap<Integer, Integer> freqMap = new HashMap<>();
    for (int number : ary) {
      if (freqMap.containsKey(number))
        freqMap.put(number, freqMap.get(number) + 1);
      else
        freqMap.put(number, 1);
    }
    return freqMap;
  }

  private static void printAry(int[] ary) {
    for (int i = 0; i < ary.length; i++) {
      System.out.print(ary[i] + " ");
    }
    System.out.println();
  }

  private static void printAry(List<Integer> ary) {
    for (int i = 0; i < ary.size(); i++) {
      System.out.print(ary.get(i) + " ");
    }
    System.out.println();
  }
  private static void printMap(Map<Integer, Integer> map) {
    for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
      System.out.println("Key = " + entry.getKey() + ",Value = " + entry.getValue());
    }
  }
}