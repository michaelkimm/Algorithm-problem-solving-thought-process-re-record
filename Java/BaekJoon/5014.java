import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

    static class Node {
        int stair;
        int movedCnt;

        public Node(int stair, int movedCnt) {
            this.stair = stair;
            this.movedCnt = movedCnt;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int F = Integer.valueOf(input[0]);
        int S = Integer.valueOf(input[1]);
        int G = Integer.valueOf(input[2]);
        int U = Integer.valueOf(input[3]);
        int D = Integer.valueOf(input[4]);

        boolean[] visited = new boolean[F + 1];
        visited[0] = true;
        visited[S] = true;

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(S, 0));
        boolean reachable = false;
        int answer = -1;
        while (!q.isEmpty()) {
            Node curNode = q.poll();
            if (curNode.stair == G) {
                reachable = true;
                answer = curNode.movedCnt;
                break;
            }
            // 위
            int upMovedStair = curNode.stair + U;
            if (upMovedStair <= F && !visited[upMovedStair]) {
                q.add(new Node(upMovedStair, curNode.movedCnt + 1));
                visited[upMovedStair] = true;
            }
            // 아래
            int downMovedStair = curNode.stair - D;
            if (downMovedStair >= 1 && !visited[downMovedStair]) {
                q.add(new Node(downMovedStair, curNode.movedCnt + 1));
                visited[downMovedStair] = true;
            }
        }
        if (reachable) {
            System.out.println(answer);
        } else {
            System.out.println("use the stairs");
        }
    }
}