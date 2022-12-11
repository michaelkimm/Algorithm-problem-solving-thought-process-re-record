import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] numbers1 = {10, 40, 30, 20};
        int k1 = 20;
        int[] numbers2 = {3, 7, 2, 8, 6, 4, 5, 1};
        int k2 = 3;
        System.out.println(solution(numbers2, k2));
    }

    public static int solution(int[] numbers, int K) {
        if (numbers.length == 1) {
            return -1;
        }
        int left = 0;
        int right = 40000;
        int mid = 0;
        int answer = -1;
        while (left <= right) {
            mid = (int) ((left + right) / 2);
            if (checkAdjacentLowerThanAvailable(numbers, K, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }

    public static boolean checkAdjacentLowerThanAvailable(int[] numbers, int K, int availableSwapCnt) {
        // 브루트포스
        // bfs
        LinkedList<Node> queue = new LinkedList<Node>();
        Node startNode = Node.getNewNode(numbers);
        queue.add(startNode);

        // 방문 처리
        HashSet<Numbers> visited = new HashSet<>();
        // visited에선 number
        visited.add(startNode.numbers);

        int tempCnt = 0;

        boolean result = false;
        while (!queue.isEmpty()) {
            Node curNode = queue.pollFirst();
            Numbers curNumbers = curNode.numbers;

            if (curNode.getMaximumDiffBetweenAdjacentElement() <= K) {
                result = true;
                break;
            }
            for (int i = 0; i < curNumbers.data.length; i++) {
                for (int j = i + 1; j < curNumbers.data.length; j++) {
                    // i와 j 교환
                    Node newNode = Node.getNewNode(curNode);
                    newNode.swap(i, j);

                    if (newNode.swapCnt > availableSwapCnt) {
                        continue;
                    }
                    if (visited.contains(newNode.numbers)) {
                        continue;
                    }

                    visited.add(Numbers.getClone(newNode.numbers));
                    queue.addLast(newNode);
                }
            }
        }
        return result;
    }

    static class Numbers {
        int[] data;

        public Numbers(int[] data) {
            this.data = data;
        }

        public void swap(int i, int j) {
            int tmp = this.data[i];
            this.data[i] = this.data[j];
            this.data[j] = tmp;
        }

        public int getMaximumDiffBetweenAdjacentElement() {
            int max = 0;
            for (int i = 0; i < this.data.length - 1; i++) {
                max = Math.max(Math.abs(this.data[i] - this.data[i + 1]), max);
            }
            return max;
        }

        public static Numbers getClone(int[] data) {
            int[] newData = Arrays.copyOf(data, data.length);
            return new Numbers(newData);
        }

        public static Numbers getClone(Numbers numbers) {
            int[] newData = Arrays.copyOf(numbers.data, numbers.data.length);
            return new Numbers(newData);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Numbers)) return false;
            Numbers numbers = (Numbers) o;
            return Arrays.equals(data, numbers.data);
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(data);
        }
    }

    static class Node {
        Numbers numbers;
        int swapCnt;

        public Node(Numbers numbers, int swapCnt) {
            this.numbers = numbers;
            this.swapCnt = swapCnt;
        }

        public int getMaximumDiffBetweenAdjacentElement() {
            return numbers.getMaximumDiffBetweenAdjacentElement();
        }

        public void swap(int i, int j) {
            this.numbers.swap(i, j);
            this.swapCnt += 1;
        }

        public static Node getNewNode(int[] numbers) {
            return new Node(Numbers.getClone(numbers), 0);
        }

        public static Node getNewNode(Node node) {
            return new Node(Numbers.getClone(node.numbers), node.swapCnt);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Node)) return false;
            Node node = (Node) o;
            return swapCnt == node.swapCnt && numbers.equals(node.numbers);
        }

        @Override
        public int hashCode() {
            return Objects.hash(numbers, swapCnt);
        }
    }

}