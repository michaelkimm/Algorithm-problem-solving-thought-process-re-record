
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.System.exit;

public class Main {
    static class Point2D {
        int i;
        int j;
        public Point2D(int i, int j){
            this.i = i;
            this.j = j;
        }
    }
    static int[][] board = new int[9][9];
    static List<Point2D> zeroPts = new ArrayList<>();
    static boolean[][] rowExists = new boolean[9][10];
    static boolean[][] colExists = new boolean[9][10];
    static boolean[][] areaExists = new boolean[9][10];

    static void recursive(int ck) {
        if (ck == zeroPts.size()) {
            Arrays.stream(board)
                    .forEach(ary -> {
                        Arrays.stream(ary).forEach(System.out::print);
                        System.out.println();
                    });
            exit(0);
        }

        int i = zeroPts.get(ck).i;
        int j = zeroPts.get(ck).j;

        for (int num = 1; num <= 9; num++) {
            if (rowExists[i][num] || colExists[j][num] || areaExists[getAreaId(i, j)][num]) {
                continue;
            }
            rowExists[i][num] = true;
            colExists[j][num] = true;
            areaExists[getAreaId(i, j)][num] = true;
            board[i][j] = num;

            recursive(ck + 1);

            rowExists[i][num] = false;
            colExists[j][num] = false;
            areaExists[getAreaId(i, j)][num] = false;
            board[i][j] = 0;
        }
    }

    static int getAreaId(int i, int j) {
        return ((int)(i / 3)) * 3 + (int)(j / 3);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            char[] charArray = br.readLine().strip().toCharArray();
            for (int j = 0; j < 9; j++) {
                board[i][j] = Character.getNumericValue(charArray[j]);
                if (board[i][j] != 0) {
                    rowExists[i][board[i][j]] = true;
                    colExists[j][board[i][j]] = true;
                    areaExists[getAreaId(i, j)][board[i][j]] = true;
                } else {
                    zeroPts.add(new Point2D(i, j));
                }
            }
        }
        recursive(0);
    }
}
