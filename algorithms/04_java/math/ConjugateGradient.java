package math;

/**
 * Conjugate Gradient Linear Solver in Java (Numerical Recipes 3rd Ed. Chapter 2.7).
 */
public class ConjugateGradient {
    private static double dot(double[] a, double[] b) {
        double s = 0;
        for (int i = 0; i < a.length; i++) s += a[i] * b[i];
        return s;
    }

    public static double[] solve(double[][] A, double[] b, double tol, int maxIter) {
        int n = b.length;
        double[] x = new double[n];
        double[] r = b.clone();
        double[] p = r.clone();
        double rsOld = dot(r, r);

        for (int iter = 0; iter < maxIter; iter++) {
            if (Math.sqrt(rsOld) < tol) break;
            double[] Ap = new double[n];
            for (int i = 0; i < n; i++) Ap[i] = dot(A[i], p);
            double alpha = rsOld / dot(p, Ap);
            for (int i = 0; i < n; i++) {
                x[i] += alpha * p[i];
                r[i] -= alpha * Ap[i];
            }
            double rsNew = dot(r, r);
            for (int i = 0; i < n; i++) p[i] = r[i] + (rsNew / rsOld) * p[i];
            rsOld = rsNew;
        }
        return x;
    }

    public static void main(String[] args) {
        double[][] A = {{4, 1}, {1, 3}};
        double[] b = {1, 2};
        double[] x = solve(A, b, 1e-8, 50);
        assert Math.abs(x[0] - 1.0 / 11.0) < 1e-5;
        System.out.println("Java Conjugate Gradient verified.");
    }
}
