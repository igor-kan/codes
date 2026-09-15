// Ordinary least squares for a straight line.
public class LeastSquaresLinear {
    static double[] leastSquares(double[] xs, double[] ys) {
        int n = xs.length;
        double meanX = 0, meanY = 0;
        for (int i = 0; i < n; i++) { meanX += xs[i] / n; meanY += ys[i] / n; }
        double numerator = 0, denominator = 0;
        for (int i = 0; i < n; i++) {
            numerator += (xs[i] - meanX) * (ys[i] - meanY);
            denominator += (xs[i] - meanX) * (xs[i] - meanX);
        }
        double slope = numerator / denominator;
        return new double[] {meanY - slope * meanX, slope};
    }

    public static void main(String[] args) {
        double[] fit = leastSquares(new double[] {0, 1, 2, 3}, new double[] {1, 3, 5, 7});
        assert Math.abs(fit[0] - 1) < 1e-12 && Math.abs(fit[1] - 2) < 1e-12;
        System.out.println("least squares linear ok");
    }
}
