import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

class Site{
    public int i;
    public int j;
    Site() {}
    Site(int i, int j){
      this.i = i;
      this.j = j;
    }
  }

class Main {
  public static int[] di = {-1, 1, 0, 0};  // 상하좌우
  public static int[] dj = {0, 0, -1, 1}; 
  public static int answer = 0;
  public static void printAry(int[][] ary, int N, int M)
  {
    for (int i = 0; i < N; i++)
    {
      for (int j  = 0; j < M; j++)
      {
        System.out.print(ary[i][j] + " ");
      }
      System.out.println("");
    }
  }
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] sizeInput = br.readLine().split(" ");
    int M = Integer.parseInt(sizeInput[0]);
    int N = Integer.parseInt(sizeInput[1]);

    Queue<Site> growableSites = new LinkedList<Site>();
    int nonPollutedCount = 0;
    int[][] farm = new int[N][M];
    for (int i = 0; i < N; i++)
    {
      String[] mapInput = br.readLine().split(" ");
      for (int j  = 0; j < M; j++)
      {
        farm[i][j] = Integer.parseInt(mapInput[j]);
        if (farm[i][j] == 1)
          growableSites.add(new Site(i, j));
        else if (farm[i][j] == 0)
          nonPollutedCount += 1;
      }
    }
    Pollute(farm, N, M, growableSites, nonPollutedCount);
    System.out.println(answer);
  }
  public static void Pollute(int[][] farm, int N, int M, Queue<Site> growableSites, int nonPollutedCount){
    if (nonPollutedCount == 0)
      return;
    
    Queue<Site> nextPollutableSite = new LinkedList<Site>();
    while (growableSites.size() > 0){
      answer += 1;
      Site pollutableSite = growableSites.remove();
      // 상하좌우 움직임
      for (int i = 0; i < 4; i++){
        int ni = pollutableSite.i + di[i];
        int nj = pollutableSite.j + dj[i];
        if (0 <= ni && ni < N && 0 <= nj && nj < M){
          if (farm[pollutableSite.i][pollutableSite.j] == 0) {
            farm[pollutableSite.i][pollutableSite.j] = 1;
            nextPollutableSite.add(new Site(pollutableSite.i, pollutableSite.j));
            nonPollutedCount -= 1;
          }
        }
      }
    }
    Pollute(farm, N, M, nextPollutableSite, nonPollutedCount);
  }
}



// -------------------------------------------------------------------- //

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

class Site{
    public int i;
    public int j;
    Site() {}
    Site(int i, int j){
      this.i = i;
      this.j = j;
    }
  }

class Main {
  public static int[] di = {-1, 1, 0, 0};  // 상하좌우
  public static int[] dj = {0, 0, -1, 1}; 
  public static int answer = 0;
  public static void printAry(int[][] ary, int N, int M)
  {
    for (int i = 0; i < N; i++)
    {
      for (int j  = 0; j < M; j++)
      {
        System.out.print(ary[i][j] + " ");
      }
      System.out.println("");
    }
  }
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] sizeInput = br.readLine().split(" ");
    int M = Integer.parseInt(sizeInput[0]);
    int N = Integer.parseInt(sizeInput[1]);

    Queue<Site> growableSites = new LinkedList<Site>();
    int nonPollutedCount = 0;
    int[][] farm = new int[N][M];
    for (int i = 0; i < N; i++)
    {
      String[] mapInput = br.readLine().split(" ");
      for (int j  = 0; j < M; j++)
      {
        farm[i][j] = Integer.parseInt(mapInput[j]);
        if (farm[i][j] == 1)
          growableSites.add(new Site(i, j));
        else if (farm[i][j] == 0)
          nonPollutedCount += 1;
      }
    }
    Pollute(farm, N, M, growableSites, nonPollutedCount);
    System.out.println(answer);
  }
  public static void Pollute(int[][] farm, int N, int M, Queue<Site> growableSites, int nonPollutedCount){
    if (growableSites.size() == 0 || nonPollutedCount == 0)
    {
      if (nonPollutedCount != 0)
        answer = -1;
      return;
    }
    answer += 1;
    Queue<Site> nextPollutableSite = new LinkedList<Site>();
    while (growableSites.size() > 0){
      Site pollutableSite = growableSites.remove();
      // 상하좌우 움직임
      for (int i = 0; i < 4; i++){
        int ni = pollutableSite.i + di[i];
        int nj = pollutableSite.j + dj[i];
        if (0 <= ni && ni < N && 0 <= nj && nj < M){
          if (farm[ni][nj] == 0) {
            farm[ni][nj] = 1;
            nextPollutableSite.add(new Site(ni, nj));
            nonPollutedCount -= 1;
          }
        }
      }
    }
    Pollute(farm, N, M, nextPollutableSite, nonPollutedCount);
  }
}

// -------------------------------------------------------------------- //

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

class Site{
    public int i;
    public int j;
    Site() {}
    Site(int i, int j){
      this.i = i;
      this.j = j;
    }
  }

class Main {
  public static int[] di = {-1, 1, 0, 0};  // 상하좌우
  public static int[] dj = {0, 0, -1, 1}; 
  public static int answer = 0;
  public static void printAry(int[][] ary, int N, int M)
  {
    for (int i = 0; i < N; i++)
    {
      for (int j  = 0; j < M; j++)
      {
        System.out.print(ary[i][j] + " ");
      }
      System.out.println("");
    }
  }
  
  public static void main(String[] args) throws IOException {
    // 입력 처리
    // 2차원 배열 크기 입력
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] sizeInput = br.readLine().split(" ");
    int M = Integer.parseInt(sizeInput[0]);
    int N = Integer.parseInt(sizeInput[1]);

    // 2차원 배열 입력
    Queue<Site> growableSites = new LinkedList<Site>();
    int nonPollutedCount = 0;
    int[][] farm = new int[N][M];
    for (int i = 0; i < N; i++)
    {
      String[] mapInput = br.readLine().split(" ");
      for (int j  = 0; j < M; j++)
      {
        farm[i][j] = Integer.parseInt(mapInput[j]);
        if (farm[i][j] == 1)
          growableSites.add(new Site(i, j));
        else if (farm[i][j] == 0)
          nonPollutedCount += 1;
      }
    }

    while (growableSites.size() > 0)
    {
      growableSites = Pollute(farm, N, M, growableSites, nonPollutedCount);
      answer += 1;
    }
    if (nonPollutedCount != 0)
      answer = -1;
    System.out.println(answer);
  }

  public static Queue<Site> Pollute(int[][] farm, int N, int M, Queue<Site> growableSites, int nonPollutedCount){
    Queue<Site> nextPollutableSite = new LinkedList<Site>();
    while (growableSites.size() > 0){
      Site pollutableSite = growableSites.remove();
      // 상하좌우 움직임
      for (int i = 0; i < 4; i++){
        int ni = pollutableSite.i + di[i];
        int nj = pollutableSite.j + dj[i];
        if (0 <= ni && ni < N && 0 <= nj && nj < M){
          if (farm[ni][nj] == 0) {
            farm[ni][nj] = 1;
            nextPollutableSite.add(new Site(ni, nj));
            nonPollutedCount -= 1;
          }
        }
      }
    }
    return nextPollutableSite;
  }
}

// ============================================================================= 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

class Site{
    public int i;
    public int j;
    Site() {}
    Site(int i, int j){
      this.i = i;
      this.j = j;
    }
    public String toString(){
      return Integer.toString(i) + ", " + Integer.toString(j); 
    }
  }

class Main {
  public static final int[] di = {-1, 1, 0, 0};  // 상하좌우
  public static final int[] dj = {0, 0, -1, 1}; 
  public static void printAry(int[][] ary, int N, int M)
  {
    for (int i = 0; i < N; i++)
    {
      for (int j  = 0; j < M; j++)
      {
        System.out.print(ary[i][j] + " ");
      }
      System.out.println("");
    }
  }
  
  public static void main(String[] args) throws IOException {
    int answer = 0;
    // 입력 처리
    // 2차원 배열 크기 입력
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] sizeInput = br.readLine().split(" ");
    int M = Integer.parseInt(sizeInput[0]);
    int N = Integer.parseInt(sizeInput[1]);

    // 2차원 배열 입력
    Queue<Site> growableSites = new LinkedList<Site>();
    int[][] farm = new int[N][M];
    for (int i = 0; i < N; i++)
    {
      String[] mapInput = br.readLine().split(" ");
      for (int j  = 0; j < M; j++)
      {
        farm[i][j] = Integer.parseInt(mapInput[j]);
        if (farm[i][j] == 1)
          growableSites.add(new Site(i, j));
      }
    }

    while (growableSites.size() > 0)
    {
      growableSites = Pollute(farm, N, M, growableSites);
      // 확장을 했었으면 시간 추가
      if (growableSites.size() != 0)
        answer += 1;
    }

    for (int i = 0; i < N; i++){
      for (int j = 0; j < M; j++){
        // 확장 못한 곳이 한곳이라도 있는지 확인
        if (farm[i][j] == 0){
          answer = -1;
        }
      }
    }
    System.out.println(answer);
  }

  public static Queue<Site> Pollute(int[][] farm, int N, int M, Queue<Site> growableSites){
    // 다음 자랄 수 있는 곳
    Queue<Site> nextPollutableSite = new LinkedList<Site>();

    // 현재 자랄 수 있는 곳
    for (Site site : growableSites){
      // 상하좌우
      for (int i = 0; i < 4; i++){
        int ni = site.i + di[i];
        int nj = site.j + dj[i];
        if (0 <= ni && ni < N && 0 <= nj && nj < M){
          // 자라날 수 있는 경우
          if (farm[ni][nj] == 0) {
            farm[ni][nj] = 1;
            nextPollutableSite.add(new Site(ni, nj));
          }
        }
      }
    }
    return nextPollutableSite;
  }
}