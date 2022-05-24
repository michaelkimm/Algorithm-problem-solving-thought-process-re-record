import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.function.BinaryOperator;
import java.util.function.Predicate;
import java.util.stream.Stream;

class Main {

  static int[][] minLines;
  static int[][] maxLines;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine().strip());
    minLines = new int[N][3];
    maxLines = new int[N][3];

    for (int i = 0; i < N; i++) {
      String[] line = br.readLine().split(" ");
      int left = Integer.parseInt(line[0]);
      int middle = Integer.parseInt(line[1]);
      int right = Integer.parseInt(line[2]);
      maxLines[i][0] = left;
      maxLines[i][1] = middle;
      maxLines[i][2] = right;

      minLines[i][0] = left;
      minLines[i][1] = middle;
      minLines[i][2] = right;
    }

    BinaryOperator<Integer> minOperator = (a, b) -> a < b ? a : b;
    BinaryOperator<Integer> maxOperator = (a, b) -> a > b ? a : b;
    process(minLines, minOperator);
    process(maxLines, maxOperator);

    System.out.println(Arrays.stream(maxLines[N - 1]).max().getAsInt() + " " + Arrays.stream(minLines[N - 1]).min().getAsInt());
  }

  public static void process(int[][] lines, BinaryOperator<Integer> myOperator) {
    for (int i = 1; i < lines.length; i++) {
      // decide left
      lines[i][0] = lines[i][0] + myOperator.apply(lines[i - 1][0], lines[i - 1][1]);
      Stream
      // decide right
      lines[i][2] = lines[i][2] + myOperator.apply(lines[i - 1][1], lines[i - 1][2]);

      // decide mid
      lines[i][1] = lines[i][1] + myOperator.apply(myOperator.apply(lines[i - 1][0], lines[i - 1][1]), lines[i - 1][2]);
    }
  }
}