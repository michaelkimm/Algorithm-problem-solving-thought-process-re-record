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

    Map<Long, Long> primeFactors = new HashMap<>();
    for (int i = 0; i < N; i++) {
      Map<Long, Long> v = getPrimeFactorsOf(numbers[i]);
      primeFactors = getPrimeFactorMultiplied(primeFactors, v);
    }

    // get dividableFactor
    Map<Long, Long> dividableFactor = getDividableFactor(primeFactors, N);

    // fix number
    long moveCnt = 0L;
    for (int i = 0; i < N; i++) {
      Map<Long, Long> v = getPrimeFactorsOf(numbers[i]);
      moveCnt += getFixNeededCnt(v, dividableFactor);
    }

    System.out.println(getPrimeFactorToNumber(dividableFactor) + " " + moveCnt);
  }

  static Map<Long, Long> getPrimeFactorMultiplied(Map<Long, Long> primeFactor1, Map<Long, Long> primeFactor2) {
    Map<Long, Long> result = new HashMap<>();
    for (Map.Entry<Long, Long> v1 : primeFactor1.entrySet()) {
      if (primeFactor2.containsKey(v1.getKey())) {
        result.put(v1.getKey(), v1.getValue() + primeFactor2.get(v1.getKey()));
      }
      else
        result.put(v1.getKey(), v1.getValue());
    }

    for (Map.Entry<Long, Long> v2 : primeFactor2.entrySet()) {
      if (!primeFactor1.containsKey(v2.getKey()))
        result.put(v2.getKey(), v2.getValue());
    }
    return result;
  }

  static long getFixNeededCnt(Map<Long, Long> target, Map<Long, Long> dividableFactor) {
    long divCnt = 0L;
    for (Map.Entry<Long, Long> divadable_v : dividableFactor.entrySet()) {
      divCnt += divadable_v.getValue();
    }

    long haveCnt = 0;
    for (Map.Entry<Long, Long> target_v : target.entrySet()) {
      for (Map.Entry<Long, Long> divadable_v : dividableFactor.entrySet()) {
        if (target_v.getKey() == divadable_v.getKey()) {
          haveCnt += (target_v.getValue() >= divadable_v.getValue() ? divadable_v.getValue() : target_v.getValue());
          break;
        }
      }
    }

    return divCnt - haveCnt;
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
      if (pf.getValue() / (long)N >= 1L) {
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
      if (!primeAvailables[(int) num])
        continue;
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