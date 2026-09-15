// Thomas algorithm for tridiagonal systems.
public class ThomasAlgorithm {
    static double[] thomas(double[] lower, double[] diagonal, double[] upper, double[] rhs) {
        int n = diagonal.length;
        double[] c = new double[n];
        double[] d = new double[n];
        double[] x = new double[n];
        c[0] = upper[0] / diagonal[0];
        d[0] = rhs[0] / diagonal[0];
        for (int i = 1; i < n; i++) {
            double denominator = diagonal[i] - lower[i] * c[i - 1];
            c[i] = i < n - 1 ? upper[i] / denominator : 0;
            d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
        }
        x[n - 1] = d[n - 1];
        for (int i = n - 2; i >= 0; i--) x[i] = d[i] - c[i] * x[i + 1];
        return x;
    }

    public static void main(String[] args) {
        double[] x = thomas(new double[] {0, -1, -1}, new double[] {2, 2, 2}, new double[] {-1, -1, 0}, new double[] {1, 0, 1});
        for (double value : x) assert Math.abs(value - 1) < 1e-12;
        System.out.println("thomas algorithm ok");
    }
}
