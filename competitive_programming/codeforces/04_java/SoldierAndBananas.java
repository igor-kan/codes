import java.util.*;

// Codeforces 546A - Soldier and Bananas.
public class SoldierAndBananas {
    static long soldierAndBananas(long cost, long money, long count) {
        long total = cost * count * (count + 1) / 2;
        return Math.max(0, total - money);
    }

    public static void main(String[] args) {
        assert soldierAndBananas(3, 17, 4) == 13 && soldierAndBananas(1, 100, 1) == 0;
        System.out.println("546A soldier and bananas ok");
    }
}
