import java.util.*;
import java.io.*;

class Main {
  private static final String[] numNames = {
      "",
      "one",
      "two",
      "three",
      "four",
      "five",
      "six",
      "seven",
      "eight",
      "nine",
      "ten",
      "eleven",
      "twelve",
      "thirteen",
      "fourteen",
      "quarter",
      "sixteen",
      "seventeen",
      "eighteen",
      "nineteen",
      "twenty",
      "twenty one",
      "twenty two",
      "twenty three",
      "twenty four",
      "twenty five",
      "twenty six",
      "twenty seven",
      "twenty eight",
      "twenty nine",
      "half"
  };

  public static String getNumberInEngWord(int number) {
    return numNames[number];
  }

  public static String addMinuteForm(String minDiffiInEng, int minDiff) {
    if (minDiff == 15 || minDiff == 30) {
        minDiffiInEng += "";
      } else if (minDiff == 1) {
        minDiffiInEng += " minute";
      } else {
        minDiffiInEng += " minutes";
      }
      return minDiffiInEng;
  }

  public static void printInWordClockForm(int h, int m, String hourInEng, String minDiffInEng) {
    if (m == 0) {
        // add O' clock
        System.out.println(hourInEng + " o' clock");
      } else if (m >= 1 && m <= 30) {
        // add past
        System.out.println(minDiffInEng + " past " + hourInEng);
      } else if (m > 30) {
        // add to
        int nextHour = h + 1;
        if (nextHour == 13) {
          nextHour = 1;
        }
        System.out.println(minDiffInEng + " to " + getNumberInEngWord(nextHour));
      }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int h = Integer.parseInt(br.readLine().strip());
    int m = Integer.parseInt(br.readLine().strip());

    

        // <분 표현>
        // minute/minutes

    


    // 1) 시간(시, 분)
        // <숫자 표현>
        // - 정각/쿼터/하프/1-30
        // - 상대성
    int minDiff = m;
    if (m > 30) {
      minDiff = Math.abs(60 - m);
    }
    String minDiffInEng = getNumberInEngWord(minDiff);
    minDiffInEng = addMinuteForm(minDiffInEng, minDiff);

    String hourInEng = getNumberInEngWord(h);

    // 2) 시-분 상대성 표현
        // <O'clock, past, to 표현>
    printInWordClockForm(h, m, hourInEng, minDiffInEng);
  }
}