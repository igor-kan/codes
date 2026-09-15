public final class GaussianElimination {
    private GaussianElimination() {}

    public static double[] solve(double[][] matrix, double[] rhs) {
        int n = matrix.length;
        double[][] a = new double[n][n + 1];
        for (int i = 0; i < n; i++) {
            System.arraycopy(matrix[i], 0, a[i], 0, n);
            a[i][n] = rhs[i];
        }
        for (int c = 0; c < n; c++) {
            int pivot = c;
            for (int r = c + 1; r < n; r++) {
                if (Math.abs(a[r][c]) > Math.abs(a[pivot][c])) {
                    pivot = r;
                }
            }
            double[] tmp = a[c];
            a[c] = a[pivot];
            a[pivot] = tmp;
            for (int r = c + 1; r < n; r++) {
                double f = a[r][c] / a[c][c];
                for (int k = c; k <= n; k++) {
                    a[r][k] -= f * a[c][k];
                }
            }
        }
        double[] x = new double[n];
        for (int r = n - 1; r >= 0; r--) {
            double s = a[r][n];
            for (int k = r + 1; k < n; k++) {
                s -= a[r][k] * x[k];
            }
            x[r] = s / a[r][r];
        }
        return x;
    }

    public static void main(String[] args) {
        double[] x = solve(new double[][] {{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}}, new double[] {8, -11, -3});
        if (Math.abs(x[0] - 2) > 1e-9 || Math.abs(x[1] - 3) > 1e-9 || Math.abs(x[2] + 1) > 1e-9) {
            throw new AssertionError("wrong solution");
        }
        System.out.println("x=" + x[0] + " " + x[1] + " " + x[2]);
    }
}
