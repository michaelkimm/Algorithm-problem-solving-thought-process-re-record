import java.util.*;

class Solution {
    static LinkedList<String> results = new LinkedList<>();
    
    public void permutations(String source, int charCnt) {
        if (charCnt > 5) {
           return;
        }
        results.add(source);
        
        for (int i = 0; i < 5; i++) {
            permutations(source + "AEIOU".charAt(i), charCnt + 1);
        }
    }
    
    public int solution(String word) {
        
        permutations("", 0);
        return results.indexOf(word);
    }
}