import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;


class Main {

  static long[] primeNumbers;

  public static void main(String[] args) throws IOException {
    // input
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] values = br.readLine().split(" ");
    long[] numbers = new long[N];
    for (int i = 0; i < numbers.length; i++) {
      numbers[i] = Long.parseLong(values[i]);
    }

    // initialize
    long maxNumber = Arrays.stream(numbers).max().getAsLong();

    // get prime numbers under maxNumber
    primeNumbers = getPrimeNumberUnder(maxNumber);

    // get primeFactor of sum of numbers
    long numbersMultiplied = Arrays.stream(numbers).reduce((result, value) -> result *= value).getAsLong();
    Map<Long, Long> primeFactors = getPrimeFactorsOf(numbersMultiplied);

    // get dividableFactor
    Map<Long, Long> dividableFactor = getDividableFactor(primeFactors, N);

//    Map<Long, Long>[] primeFactorOfNumbers = new Map<Long, Long>[N];
    for (int i = 0; i < N; i++) {
      Map<Long, Long> v = getPrimeFactorsOf(numbers[i]);
      System.out.println("num: " + numbers[i]);
      printMap(v);
    }

    System.out.println(getPrimeFactorToNumber(dividableFactor));
  }

  static int getFixNeededCnt(Map<Long, Long> target, Map<Long, Long> dividableFactor) {
    int haveCnt = 0;
    for (Map.Entry<Long, Long> target_v : target.entrySet()) {
      for (Map.Entry<Long, Long> divadable_v : dividableFactor.entrySet()) {
        if (target_v.getKey() == divadable_v.getKey()) {
          haveCnt += (target_v.getValue() >= divadable_v.getValue() ? divadable_v.getValue() : target_v.getValue());
          break;
        }
      }
    }
    return result;
  }

  static long getPrimeFactorToNumber(Map<Long, Long> primeFacetor) {
    long result = 1;
    for (Map.Entry<Long, Long> v : primeFacetor.entrySet()) {
      result *= (long)Math.pow(v.getKey(), v.getValue());
    }
    return result;
  }

  static void printMap(Map<Long, Long> map) {
    for (Map.Entry<Long, Long> v : map.entrySet()) {
      System.out.println(v.getKey() + "^" + v.getValue());
    }
    System.out.println();
  }

  static Map<Long, Long> getDividableFactor(Map<Long, Long> primeFactors, int N) {
    Map<Long, Long> result = new HashMap<>();
    for (Map.Entry<Long, Long> pf : primeFactors.entrySet()) {
      if (pf.getValue() / N >= 1) {
        result.put(pf.getKey(), pf.getValue() / (long)N);
      }
    }
    return result;
  }

  static Map<Long, Long> getPrimeFactorsOf(long number) {
    Map<Long, Long> result = new HashMap<>();
    for (long primeNumber : primeNumbers) {
      while (number % primeNumber == 0) {
        number /= primeNumber;
        if (result.containsKey(primeNumber))
          result.replace(primeNumber, result.get(primeNumber) + 1L);
        else
          result.put(primeNumber, 1L);
      }
    }
    return result;
  }

  static long[] getPrimeNumberUnder(long maxNumber) {
    long[] result;
    // eratotaenes che
    boolean[] primeAvailables = new boolean[(int)(maxNumber + 1L)];
    Arrays.fill(primeAvailables, true);
    primeAvailables[0] = false;
    primeAvailables[1] = false;
    for (long num = 2L; num * num <= maxNumber; num++) {
      for (long multiple = num * num; multiple <= maxNumber; multiple += num) {
        primeAvailables[(int)multiple] = false;
      }
    }
    int primeCnt = 0;
    for (boolean primeAvailable : primeAvailables) {
      if (primeAvailable)
        primeCnt += 1;
    }
    result = new long[primeCnt];
    int idx = 0;
    for (int i = 2; i < primeAvailables.length; i++) {
      if (primeAvailables[i]) {
        result[idx++] = (long)i;
      }
    }
    return result;
  }
}