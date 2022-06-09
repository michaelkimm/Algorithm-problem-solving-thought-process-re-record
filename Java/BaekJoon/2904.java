import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

  static List<Integer> primeNumbers;
  static int[] gcd;
  static int[][] pfOfNumbers;

  public static void main(String[] args) throws IOException {
    // input
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] values = br.readLine().split(" ");
    int[] numbers = new int[N];
    for (int i = 0; i < numbers.length; i++) {
      numbers[i] = Integer.parseInt(values[i]);
    }
    int maxValue = Arrays.stream(numbers).max().getAsInt();

    // get GCD in primeFactor
    // get primeFactor of Numbers
    int gcdNum = 1;
    primeNumbers = getPrimeNumbersUnder(maxValue);
    gcd = new int[primeNumbers.size()];
    pfOfNumbers = new int[N][primeNumbers.size()];
    System.out.println("primeNumbers.size: " + primeNumbers.size());
    for (int j = 0; j < primeNumbers.size(); j++) {
      for (int i = 0; i < N; i++) {
        int number = numbers[i];
        while (number % primeNumbers.get(j) == 0) {
          number /= primeNumbers.get(j);
          gcd[j]++;
          pfOfNumbers[i][j]++;
        }
      }
      gcd[j] /= N;
      gcdNum *= Math.pow(primeNumbers.get(j), gcd[j]);
    }

    // get move count
    int count = 0;
    for (int idx = 0; idx < N; idx++) {
      for (int j = 0; j < primeNumbers.size(); j++) {
        if (pfOfNumbers[idx][j] < gcd[j])
          count += (gcd[j] - pfOfNumbers[idx][j]);
      }
    }
    System.out.println(gcdNum + " " + count);
  }

  static List<Integer> getPrimeNumbersUnder(int numberBorder) {
    List<Integer> result = new ArrayList<>();
    boolean[] isPrimeNumber = new boolean[numberBorder + 1];

    for (int num = 2; num <= numberBorder; num++) {
      if (!isPrimeNumber[num]) {
        result.add(num);
        for (int multipled = num * 2; multipled <= numberBorder; multipled += num) {
          isPrimeNumber[multipled] = true;
        }
      }
    }
    return result;
  }
}