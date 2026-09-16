import java.util.*;

// Codeforces 263A - Beautiful Matrix.
public class BeautifulMatrix {
    static int beautifulMatrix(int[][] grid) {
        for (int row = 0; row < 5; row++)
            for (int column = 0; column < 5; column++)
                if (grid[row][column] == 1) return Math.abs(row - 2) + Math.abs(column - 2);
        return -1;
    }

    public static void main(String[] args) {
        int[][] grid = {
            {0, 0, 0, 0, 0}, {0, 0, 0, 0, 1}, {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0},
        };
        assert beautifulMatrix(grid) == 3;
        System.out.println("263A beautiful matrix ok");
    }
}
