class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine(" ");
        N = Integer.parseInt(input[0]);
        K = Integer.parseInt(input[1]);

        input = br.readLine(" ");
        int[] temperatures = int[N];
        for (int i = 0; i < N; i++) {
            culmulativeSum[i] = Integer.parseInt(pinput[i]);
        }

        int[] culmulativeSum = getCumulativeSum(temperatures);
        
    }

    public static int[] getCumulativeSum(int[] ary) {

    }
}