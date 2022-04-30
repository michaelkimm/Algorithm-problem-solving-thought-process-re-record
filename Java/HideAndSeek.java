import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner myScanner = new Scanner(System.in);
    int N = myScanner.nextInt();
    int K = myScanner.nextInt();
    int cnt = 0;
    if (K > N)
      cnt = myFunction(K, N, cnt);
    else
      cnt = N - K;
    System.out.println(cnt);
  }
  private static int myFunction(int bigNum, int smallNum, int cnt)
  {
    if (bigNum == smallNum)
      return cnt;
    // 짝수인 경우
    if (bigNum % 2 == 0)
    {
      int expectedHalf = (int)(bigNum / 2);
      if (expectedHalf > smallNum)
      {
        // 반토막
        bigNum = expectedHalf;
      }
      else
      {
        // end - start번 Move
        cnt += (bigNum - smallNum);
      }
    }
    // 홀수인 경우
    else
      bigNum -= 1;
    cnt += 1;
    return myFunction(bigNum, smallNum, cnt);
  }
}