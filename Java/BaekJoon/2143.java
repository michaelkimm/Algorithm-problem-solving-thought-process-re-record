import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


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
    List<Integer> ccA = getRangeSum(cumulativeA);
    int[] cumulativeB = getCumulative(B);

    System.out.println("ca");
    printAry(cumulativeA);

    System.out.println("cca");
    printAry(ccA);

    System.out.println("cb");
    printAry(cumulativeB);

    int answer = 0;
    System.out.println(answer);
  }

  private static List<Integer> getRangeSum(int[] ary) {
    int N = ary.length;
    ArrayList<Integer> result = new ArrayList<>();
    for (int left = 0; left < N; left++) {
      for (int right = left + 1; right < N; right++) {
        result.add(ary[right] - ary[left]);
      }
    }
    Collections.sort(result);
    return result;
  }

  private static int[] getCumulative(int[] ary) {
    int[] cumulative = new int[ary.length];
    for (int i = 0; i < ary.length; i++) {
      if (i != 0)
        cumulative[i] = cumulative[i - 1];
      cumulative[i] += ary[i];
    }
    return cumulative;
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
}