import java.io.*;
import java.util.Arrays;

class Main {
  public static void printAry(int[][] ary){
    for (int i = 0; i < ary.length; i++){
      System.out.printf("%d, %d\n", ary[i][0], ary[i][1]);
    }
    System.out.println("");
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine().strip());
    int [] wines = new int[n];
    int[] twoBeforeAndNow = new int[n];
    int[] beforeAndNow = new int[n];
    int f2 = 0;
    int f1 = 0;
    int ff2 = 0;
    for (int i = 0; i < n; i++){
      wines[i] = Integer.parseInt(br.readLine().strip());
      f2 = i - 2 >= 0 ? (twoBeforeAndNow[i - 2] > f2 ? twoBeforeAndNow[i - 2] : f2) : f2;
      f1 = i - 1 >= 0 ? (twoBeforeAndNow[i - 1] > f2 ? twoBeforeAndNow[i - 1] : f2) : f2;
      ff2 = i - 2 >= 0 ? (beforeAndNow[i - 2] > ff2 ? beforeAndNow[i - 2] : ff2) : ff2;
      beforeAndNow[i] = i - 1 >= 0 ? f1 + wines[i] : wines[i]; 
      twoBeforeAndNow[i] = i - 2 >= 0 ? (ff2 > f2 ? ff2 : f2) + wines[i] : wines[i]; 
    }
    int twoBeforeMax = Arrays.stream(twoBeforeAndNow).max().getAsInt();
    int oneBeforeMax = Arrays.stream(beforeAndNow).max().getAsInt();
    System.out.println(twoBeforeMax > oneBeforeMax ? twoBeforeMax : oneBeforeMax);
    
  }
}