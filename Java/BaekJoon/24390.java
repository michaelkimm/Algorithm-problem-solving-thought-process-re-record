import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bufferedReader.readLine().strip().split(":");
        int minute = Integer.parseInt(inputs[0]);
        int second = Integer.parseInt(inputs[1]);

        int totalSec = minute * 60 + second;
        int tenMinuteCnt = 0;
        int minuteCnt = 0;
        int thirtySecCnt = 0;
        int tenSecCnt = 0;

        // 10분
        tenMinuteCnt = totalSec / 600;
        totalSec %= 600;
        // 1분
        minuteCnt = totalSec / 60;
        totalSec %= 60;
        // 30초
        thirtySecCnt = totalSec / 30;
        totalSec %= 30;
        // 10초
        tenSecCnt = totalSec / 10;
        totalSec %= 10;


        int ret = tenMinuteCnt + minuteCnt + thirtySecCnt + tenSecCnt;
        if (thirtySecCnt == 0) {
            ret += 1;
        }
        System.out.println(ret);
    }
}