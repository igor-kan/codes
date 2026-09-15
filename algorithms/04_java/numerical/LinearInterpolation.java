// Piecewise linear interpolation.
public class LinearInterpolation {
    static double linearInterpolation(double[] xs, double[] ys, double x) {
        if (x <= xs[0]) return ys[0];
        if (x >= xs[xs.length - 1]) return ys[ys.length - 1];
        for (int i = 1; i < xs.length; i++) {
            if (x <= xs[i]) {
                double slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
                return ys[i - 1] + slope * (x - xs[i - 1]);
            }
        }
        return ys[ys.length - 1];
    }

    public static void main(String[] args) {
        assert Math.abs(linearInterpolation(new double[] {0, 1, 2}, new double[] {0, 2, 4}, 0.5) - 1) < 1e-12;
        assert Math.abs(linearInterpolation(new double[] {0, 1, 4}, new double[] {0, 1, 2}, 2.5) - 1.5) < 1e-12;
        System.out.println("linear interpolation ok");
    }
}
