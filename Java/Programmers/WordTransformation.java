import java.util.*;

class Node {
    String source;
    int cost;
    
    public Node(String source, int cost) {
        this.source = source;
        this.cost = cost;
    }
}

class Solution {
    
    static LinkedList<String> list = new LinkedList<>();
    static LinkedList<Integer>[] graph;
    
    public boolean isClose(String a, String b) {
        if (a.length() != b.length()) { return false; }
        int diffCnt = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diffCnt += 1;
            }
        }
        if (diffCnt == 1) {
            return true;
        } else {
            return false;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        
        LinkedList<Node> queue = new LinkedList<>();
        HashSet<String> visited = new HashSet<>();
        queue.add(new Node(begin, 0));
        visited.add(begin);
        int answer = 0;
        while (queue.size() > 0) {
            Node curNode = queue.pollFirst();
            if (curNode.source.equals(target)) {
                answer = curNode.cost;
                break;
            }
            for (int i = 0; i < words.length; i++) {
                if (visited.contains(words[i])) {
                    continue;
                }
                if (!isClose(curNode.source, words[i])) {
                    continue;
                }
                visited.add(words[i]);
                queue.add(new Node(words[i], curNode.cost + 1));
            }
        }
        
        return answer;
    }
}