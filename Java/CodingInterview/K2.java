import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Set;

class Main {
    public static void main(String[] args) {
        int[] T = {0,0,0,0,2,3,3};
        int[] A = {2,5,6};
        System.out.println(solution(T, A));
    }
    // T = [0,0,1,1], A = [2]
    public static int solution(int[] T, int[] A) {
        boolean[] visited = new boolean[T.length];
        int visitedCnt = 1;
        visited[0] = true;
        for (int end : A) {
            if (visited[end]) {
                continue;
            }
            // 끝점 방문
            visited[end] = true;
            visitedCnt += 1;
            // 다음 점 가기
            int from = T[end];
            if (visited[from]) {
                continue;
            }
            while (from != 0) {
                visited[from] = true;
                visitedCnt += 1;
                from = T[from];
                if (visited[from]) {
                    continue;
                }
            }
        }
        return visitedCnt;
    }

//    public static int solution(int[] T, int[] A) {
//        // write your code in Java SE 8
//        if (A.length == 0) {
//            return 0;
//        }
//
//        // 0번 노드에서 각 노드까지 가는 경로
//        ArrayList<ArrayList<Integer>> graph = getStartToTargetGraphBfs(T);
//        boolean[] visited = new boolean[T.length];
//
//        int visitedCnt = 0;
//        // 시작 방문
//        visited[0] = true;
//        visitedCnt += 1;
//        for (int skill : A) {
//            ArrayList<Integer> path = graph.get(skill);
//            for (Integer skillNode : path) {
//                if (!visited[skillNode]) {
//                    visited[skillNode] = true;
//                    visitedCnt += 1;
//                }
//            }
//        }
//        return visitedCnt;
//    }

    // target 점까지 포함해서 return
    public static ArrayList<ArrayList<Integer>> getStartToTargetGraphBfs(int[] T) {
        // 인접 리스트 생성
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= T.length; i++)
            graph.add(new ArrayList<>());
        // 인접 리스트 초기화
        for (int to = 1; to < T.length; to++) {
            int from = T[to];
            graph.get(from).add(to);
        }


        // bfs로 경로 계산
        LinkedList<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[T.length];
        int[] before = new int[T.length];
        int start = 0;
        queue.add(start);
        visited[start] = true;
        while (queue.size() > 0) {
            int curSkillNum = queue.pollFirst();

            for (int i = 0; i < graph.get(curSkillNum).size(); i++) {
                Integer nextSkillNum = graph.get(curSkillNum).get(i);
                if (visited[nextSkillNum]) {
                    continue;
                }
                visited[nextSkillNum] = true;
                before[nextSkillNum] = curSkillNum;
                queue.add(nextSkillNum);
            }
        }

        // before로 returnGraph 생성
        return getStartToTargetGraph(before);
    }

    public static ArrayList<ArrayList<Integer>> getStartToTargetGraph(int[] before) {
        // start to target 경로
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= before.length; i++)
            graph.add(new ArrayList<>());

        int source = 0;
        for (int target = 0; target < before.length; target++) {
            graph.get(target).add(target);
            int from = before[target];
            while (from != source) {
                graph.get(target).add(from);
                from = before[from];
            }
            Collections.reverse(graph.get(target));
        }
        return graph;
    }

}
