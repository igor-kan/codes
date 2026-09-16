import java.util.*;

// Codeforces 266A - Stones on the Table.
public class StonesOnTheTable {
    static int stonesOnTable(String row) {
        int removals = 0;
        for (int i = 1; i < row.length(); i++) if (row.charAt(i) == row.charAt(i - 1)) removals++;
        return removals;
    }

    public static void main(String[] args) {
        assert stonesOnTable("RRG") == 1 && stonesOnTable("RRRRR") == 4 && stonesOnTable("BRBG") == 0;
        System.out.println("266A stones on the table ok");
    }
}
