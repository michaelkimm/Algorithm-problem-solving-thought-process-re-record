import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static void main(String[] args) throws IOException {
        printJosephus(15, 3);
    }

    public static void printJosephus(int n, int k) {
        Queue<Integer> circle = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            circle.add(i);
        }

        while (circle.size() != 1) {
            for (int i = 1; i <= k; i++) {
                Integer eliminated = circle.poll();
                if (i == k) {
                    System.out.println("Eliminated: " + eliminated.toString());
                    break;
                }
                circle.add(eliminated);
            }
        }
        System.out.println("Last one is " + circle.peek().toString());
    }
}
