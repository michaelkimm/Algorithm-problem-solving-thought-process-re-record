package com.company;

import java.util.*;

public class Main {

    static class Node {
        String id;
        Node next;
        Node nextFast;

        Node(String id, Node next, Node nextFast) {
            this.id = id;
            this.next = next;
            this.nextFast = nextFast;
        }
    }

    static Map<Character, Integer> movementDict = Map.of('D', 1, 'G', 2, 'K', 3, 'Y', 4, 'M', 5);

    public static void main(String[] args) {


        Node endNode = new Node("AW5", null, null);

        // M-P-W
        Node MP4 = new Node("MP4", endNode, null);
        Node MP3 = new Node("MP3", MP4, null);
        Node MP2 = new Node("MP2", MP3, null);

        // A-W
        Node AW4 = new Node("AW4", endNode, null);
        Node AW3 = new Node("AW3", AW4, null);
        Node AW2 = new Node("AW2", AW3, null);
        Node MA5 = new Node("MA5", AW2, null);

        // P-W
        Node PW4 = new Node("PW4", endNode, null);

        // X-P-A
        Node PA4 = new Node("PA4", MA5, null);
        Node XP3 = new Node("XP3", PA4, PW4);
        Node XP2 = new Node("XP2", XP3, null);


        Node MA4 = new Node("MA4", MA5, null);
        Node MA3 = new Node("MA3", MA4, null);
        Node MA2 = new Node("MA2", MA3, null);
        Node XM5 = new Node("XM5", MA2, MP2);
        Node XM4 = new Node("XM4", XM5, null);
        Node XM3 = new Node("XM3", XM4, null);
        Node XM2 = new Node("XM2", XM3, null);
        Node WX5 = new Node("WX5", XM2, XP2);
        Node WX4 = new Node("WX4", WX5, null);
        Node WX3 = new Node("WX3", WX4, null);
        Node WX2 = new Node("WX2", WX3, null);
        Node startNode = new Node("WX1", WX2, null);

        // "K" -> WX4
        // "M" -> XM2
        // "MY" -> MA2
        // "MM" -> MA3
        // "MMM" -> AW4
        // "YD" -> XP2
        // "YK" -> PA4
        // "YKG" -> AW2
        // "YGD" -> PW4
        // "YGDM" -> AW5
        // "MKD" -> MP2
        // "MKM" -> AW5

        List<String> movementList = List.of("K", "M", "MY", "MM", "MMM", "YD", "YK", "YKG", "YGD", "YGDM", "MKD", "MKM");
        for (String movements : movementList) {
            Node curNode = startNode;
            solution(curNode, movements);
        }
    }

    public static void solution(Node startNode, String movements) {
        Node curNode = startNode;
        for (Character movement : movements.toCharArray()) {
            int movementCount = movementDict.get(movement).intValue();
            if (curNode.nextFast != null) {
                curNode = curNode.nextFast;
                movementCount -= 1;
            }
            while (movementCount > 0 && curNode.next != null) {
                curNode = curNode.next;
                movementCount -= 1;
            }
        }

        System.out.println(curNode.id);
    }
}
