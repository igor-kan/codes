// LU decomposition with partial pivoting (Numerical Recipes 2.3).
public class LuDecomposition {
    static double[] luSolve(double[][] a, double[] b) {
        int n = a.length;
        for (int col = 0; col < n; col++) {
            int pivot = col;
            for (int r = col + 1; r < n; r++) {
                if (Math.abs(a[r][col]) > Math.abs(a[pivot][col])) pivot = r;
            }
            double[] tmpRow = a[col]; a[col] = a[pivot]; a[pivot] = tmpRow;
            double tb = b[col]; b[col] = b[pivot]; b[pivot] = tb;
            for (int r = col + 1; r < n; r++) {
                double f = a[r][col] / a[col][col];
                for (int k = col; k < n; k++) a[r][k] -= f * a[col][k];
                b[r] -= f * b[col];
            }
        }
        double[] x = new double[n];
        for (int r = n - 1; r >= 0; r--) {
            double s = b[r];
            for (int k = r + 1; k < n; k++) s -= a[r][k] * x[k];
            x[r] = s / a[r][r];
        }
        return x;
    }

    public static void main(String[] args) {
        double[] x = luSolve(new double[][]{{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}},
                             new double[]{8, -11, -3});
        assert Math.abs(x[0] - 2) < 1e-9 && Math.abs(x[1] - 3) < 1e-9 && Math.abs(x[2] + 1) < 1e-9;
        System.out.println("lu decomposition ok");
    }
}
