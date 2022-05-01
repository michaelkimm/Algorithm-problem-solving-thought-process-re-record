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

// ------------------------------------------------------------- //
import java.util.LinkedList;
import java.util.Queue;
import java.util.HashSet;
import java.util.Scanner;

  class Main {
    public static class Node{
    public int number;
    public int count;
    public Node() {}
    public Node(int number, int count)
    {
      this.number = number;
      this.count = count;
    }
  }
  
  public static void main(String[] args) {
    Scanner myScanner = new Scanner(System.in);
    int N = myScanner.nextInt();
    int K = myScanner.nextInt();
    int cnt = 0;
    Queue<Node> q = new LinkedList<Node>();
    HashSet<Integer> visited = new HashSet<Integer>();
    if (K > N){
      Node newNode = new Node(K, cnt);
      q.add(newNode);
      visited.add(newNode.number);
    }
      
    else
      cnt = N - K;
    while (q.size() > 0){
      Node node = q.remove();
      // System.out.println(node.number + "- " + node.count);
      if (node.number == N){
        cnt = node.count;
        break;
      }
      // 간선
      Node newNode = null;
      if (node.number % 2 == 0 && node.number != 0)
      {
        newNode = new Node((int)(node.number / 2), node.count + 1);
        if (!visited.contains(newNode.number)){
          q.add(newNode);
          visited.add(newNode.number);
        }
      }  
      newNode = new Node(node.number - 1, node.count + 1);
      if (!visited.contains(newNode.number) && newNode.number >= 0){
        q.add(newNode);
        visited.add(newNode.number);
      }
      
      newNode = new Node(node.number + 1, node.count + 1);
      if (!visited.contains(newNode.number) && newNode.number <= 100000){
        q.add(newNode);
        visited.add(newNode.number);
      }
    }
    System.out.println(cnt);
  }
}