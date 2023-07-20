package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] board;
    static int answer = 0;

    static void recursive(int cIdx) {
        if (cIdx == N * M) {
            answer += 1;
            return;
        }

        recursive(cIdx + 1);

        int i = (int)(cIdx / M);
        int j = cIdx % M;
        if (i - 1 < 0 || j - 1 < 0 || board[i - 1][j] != 1 || board[i][j - 1] != 1 || board[i - 1][j - 1] != 1) {
            board[i][j] = 1;
            recursive(cIdx + 1);
            board[i][j] = 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        N = Integer.valueOf(inputs[0]);
        M = Integer.valueOf(inputs[1]);
        board = new int[N][M];

        recursive(0);
        System.out.println(answer);
    }
}
