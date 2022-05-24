import java.io.*;
import java.util.Arrays;
import java.util.Comparator;

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

    // max
    for (int i = 1; i < N; i++) {
      // decide left
      maxLines[i][0] = maxLines[i][0] + Math.max(maxLines[i - 1][0], maxLines[i - 1][1]);

      // decide right
      maxLines[i][2] = maxLines[i][2] + Math.max(maxLines[i - 1][1], maxLines[i - 1][2]);

      // decide mid
      maxLines[i][1] = maxLines[i][1] + Math.max(Math.max(maxLines[i - 1][0], maxLines[i - 1][1]), maxLines[i - 1][2]);
    }

    // min
    for (int i = 1; i < N; i++) {
      // decide left
      minLines[i][0] = minLines[i][0] + Math.min(minLines[i - 1][0], minLines[i - 1][1]);

      // decide right
      minLines[i][2] = minLines[i][2] + Math.min(minLines[i - 1][1], minLines[i - 1][2]);

      // decide mid
      minLines[i][1] = minLines[i][1] + Math.min(Math.min(minLines[i - 1][0], minLines[i - 1][1]), minLines[i - 1][2]);
    }

    System.out.println(Arrays.stream(maxLines[N - 1]).max().getAsInt() + " " + Arrays.stream(minLines[N - 1]).min().getAsInt());
  }

  static void printAry(int[][] ary) {
    for (int[] ints : ary) {
      for (int v : ints) {
        System.out.print(v + " ");
      }
      System.out.println();
    }
    System.out.println();
  }
}