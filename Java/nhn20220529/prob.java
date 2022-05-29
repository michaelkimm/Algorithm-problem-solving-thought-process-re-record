import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    String[] snowsStr = br.readLine().split(" ");
    ArrayList<Long> snows = new ArrayList<>();
    for (int i = 0; i < N; i++) {
      snows.add(Long.parseLong(snowsStr[i]));
    }
    Collections.sort(snows);

    long minValue = Long.MAX_VALUE;
    for (int s1 = 0; s1 <= N - 4; s1++) {
      for (int s2 = s1 + 1; s2 <= N - 3; s2++) {
        int s3 = s2 + 1;
        int s4 = N - 1;
        while (s3 < s4) {
          // (1,4), (2,3)
          long dheight = getDheight(snows, s1, s4, s2, s3);
          if (Math.abs(dheight) < minValue)
            minValue = Math.abs(dheight);
          if (dheight > 0L)
            s4 -= 1;
          else if (dheight < 0L)
            s3 += 1;
          else{
            System.out.println(0);
            return;
          }
        }
      }
    }

    for (int s1 = 0; s1 <= N - 4; s1++) {
      for (int s2 = s1 + 1; s2 <= N - 3; s2++) {
        int s3 = s2 + 1;
        int s4 = N - 1;
        while (s3 < s4) {
          // (1,3), (2,4)
          long dheight = getDheight(snows, s1, s3, s2, s4);
          if (Math.abs(dheight) < minValue)
            minValue = Math.abs(dheight);
          if (dheight > 0L)
            s4 -= 1;
          else if (dheight < 0L)
            s3 += 1;
          else{
            System.out.println(0);
            return;
          }
        }
      }
    }
    System.out.println(minValue);
  }

  static long getDheight(ArrayList<Long> snows, int a1, int a2, int b1, int b2) {
    return (snows.get(a1) + snows.get(a2)) - (snows.get(b1) + snows.get(b2));
  }
}