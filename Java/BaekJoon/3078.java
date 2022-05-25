import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {

  static int N;
  static int K;
  static String[] namesInGradeOrder;
  static int[][] cumulationAry;
  static long answer = 0L;

  public static void main(String[] args) throws IOException {
    // read
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] configInfo = br.readLine().split(" ");
    N = Integer.parseInt(configInfo[0]);
    K = Integer.parseInt(configInfo[1]);

    namesInGradeOrder = new String[N + 1];
    for (int order = 1; order <= N; order++) {
      namesInGradeOrder[order] = br.readLine().strip();
    }

    // initialize
    cumulationAry = new int[21][N + 1];
    for (int order = 1; order <= N; order++) {
      // update one value
      cumulationAry[namesInGradeOrder[order].length()][order] += 1;

      // update all value
      for (int size = 2; size <= 20; size++) {
        if (order + 1 >= N + 1)
          continue;
        cumulationAry[size][order + 1] = cumulationAry[size][order];
      }
    }

    // calculate
    for (int order = 1; order <= N; order++) {
      int right = order + K <= N ? order + K : N;
      int size = namesInGradeOrder[order].length();
      int count = cumulationAry[size][right] - cumulationAry[size][order];
      answer += (long)count;
    }
    System.out.println(answer);
  }
}