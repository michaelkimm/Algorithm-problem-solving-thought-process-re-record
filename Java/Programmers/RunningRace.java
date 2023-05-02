import java.util.*;

class Solution {
    private static Map<String, Integer> playerInfo = new HashMap<>();
    
    public String[] solution(String[] players, String[] callings) {
        
        for (int i = 0; i < players.length; i++) {
            playerInfo.put(players[i], Integer.valueOf(i));
        }
        
        Arrays.stream(callings).forEach(player -> {
            int idx = playerInfo.get(player);
            String frontPlayer = players[idx - 1];
            // players 변경
            players[idx - 1] = player;
            players[idx] = frontPlayer;
            // playerInfo 변경
            playerInfo.put(player, Integer.valueOf(idx - 1));
            playerInfo.put(frontPlayer, Integer.valueOf(idx));
        });
        
        return players;
    }
}