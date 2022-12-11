import java.util.*;

class Main {
    public static void main(String[] args) {

        // 입력 받은 문자열 안에 가장 자주 나온 문자 순으로 나오는 프로그램

        // input = String(banana)
        // return = String(anb)

        

    }

    String solution(String input) {
        
        HashMap<Character, Integer> map = new HashMap<>();
        // 순회
        for (int i = 0; i < input.length; i++) {
            map.put(input[i], map.getOrDefault(input[i], 0) + 1);
        }

        // map -> 배열로 전환
        // Set<Map.Entry<K, V>> entrySet();

        Set<Map.Entry<Character, Integer>> set = map.entrySet();
        for (Map.Entry<Character, Integer> entry : set) {
            
        }
    }
}