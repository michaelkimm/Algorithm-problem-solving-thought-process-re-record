import java.io.*;
import java.util.Arrays;
import java.util.Comparator;

class Main {
  public static void printAry(int[][] ary){
    for (int i = 0; i < ary.length; i++){
      System.out.printf("%d, %d\n", ary[i][0], ary[i][1]);
    }
    System.out.println("");
  }
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine().strip());
    int[][] reservations = new int[N][2];
    for (int i = 0; i < N; i++){
      String[] line = br.readLine().split(" ");
      reservations[i][0] = Integer.parseInt(line[0]);
      reservations[i][1] = Integer.parseInt(line[1]);
    }
    Arrays.sort(reservations, new Comparator<int[]>() {
      @Override
      public int compare(int[] o1, int[] o2){
        if (o1[1] == o2[1])
          return o1[0] - o2[0];
        else
          return o1[1] - o2[1];
      }
    });
    // printAry(reservations);
    int cur_start_time = 0;
    int cur_end_time = 0;
    int answer = 0;
    for (int i = 0; i < N; i++){
      if (reservations[i][0] >= cur_end_time){
        cur_start_time = reservations[i][0];
        cur_end_time = reservations[i][1];
        answer += 1;
      }
    }
    System.out.println(answer);
  }
}