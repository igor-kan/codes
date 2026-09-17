package math;

/**
 * Cholesky LL^T Decomposition in Java (Numerical Recipes 3rd Ed. Chapter 2.6).
 */
public class Cholesky {
    public static double[][] decompose(double[][] A) {
        int n = A.length;
        double[][] L = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                double sum = 0;
                for (int k = 0; k < j; k++) sum += L[i][k] * L[j][k];
                if (i == j) {
                    double val = A[i][i] - sum;
                    if (val <= 0) throw new IllegalArgumentException("Matrix not positive definite");
                    L[i][j] = Math.sqrt(val);
                } else {
                    L[i][j] = (A[i][j] - sum) / L[j][j];
                }
            }
        }
        return L;
    }

    public static void main(String[] args) {
        double[][] A = {
            {4, 12, -16},
            {12, 37, -43},
            {-16, -43, 98}
        };
        double[][] L = decompose(A);
        assert Math.abs(L[0][0] - 2.0) < 1e-6;
        System.out.println("Java Cholesky verified.");
    }
}
