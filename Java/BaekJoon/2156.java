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


// -------------------------------------------------------------------------------------- //

import java.io.*;
import java.util.Arrays;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine().strip());
    int [] wines = new int[n + 1];
    int[] dp = new int[n + 1];
    for (int i = 1; i < n + 1; i++){
      wines[i] = Integer.parseInt(br.readLine().strip());
    }

    dp[1] = wines[1];
    if (n != 1)
      dp[2] = wines[1] + wines[2];
    
    for (int i = 3; i < n + 1; i++){
      // 날 안고르는게 나은 경우
      dp[i] = dp[i - 1];

      // 바로 이전 안고른 경우
      if (dp[i - 2] + wines[i] > dp[i])
        dp[i] = dp[i - 2] + wines[i];
      
      // 이전 고른 경우
      if (dp[i - 3] + wines[i - 1] + wines[i] > dp[i])
        dp[i] = dp[i - 3] + wines[i - 1] + wines[i];
    }
    System.out.println(Arrays.stream(dp).max().getAsInt());
  }
}