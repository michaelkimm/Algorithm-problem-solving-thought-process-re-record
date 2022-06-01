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
    int T = Integer.parseInt(br.readLine());
    int N = Integer.parseInt(br.readLine());
    String[] ns = br.readLine().split(" ");
    int[] A = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = Integer.parseInt(ns[i]);
    }

    int M = Integer.parseInt(br.readLine());
    String[] ms = br.readLine().split(" ");
    int[] B = new int[M];
    for (int i = 0; i < M; i++) {
      B[i] = Integer.parseInt(ms[i]);
    }

    int[][] cumulativeSum = new int[M + 1][N + 1];
    // cumulate A
    for (int j = 1; j <= N; j++) {
      cumulativeSum[0][j] = cumulativeSum[0][j - 1];
      cumulativeSum[0][j] += A[j - 1];
    }
    // cumulate B with A
    for (int i = 1; i <= M; i++) {
      for (int j = 0; j <= N; j++) {
        cumulativeSum[i][j] = cumulativeSum[i - 1][j];
        cumulativeSum[i][j] += B[i - 1];
      }
    }
    // two pointer on 2d array
//    int left = 0;
//    int right = N * M - 1;
//    while (left < right) {
//
//    }

    for (int[] ints : cumulativeSum) {
      for (int anInt : ints) {
        System.out.print(anInt + " ");
      }
      System.out.println();
    }
    int answer = 0;
    System.out.println(answer);
  }
}