// Neville's algorithm for polynomial interpolation.
public class NevilleInterpolation {
    static double neville(double[] xs, double[] ys, double x) {
        int n = xs.length;
        double[] table = ys.clone();
        for (int k = 1; k < n; k++)
            for (int i = 0; i < n - k; i++)
                table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k]);
        return table[0];
    }

    public static void main(String[] args) {
        assert Math.abs(neville(new double[] {0, 1, 2}, new double[] {1, 3, 2}, 1.5) - 2.875) < 1e-12;
        System.out.println("neville interpolation ok");
    }
}
