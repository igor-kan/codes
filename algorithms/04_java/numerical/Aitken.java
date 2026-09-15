// Aitken's delta-squared acceleration.
public class Aitken {
    static double aitken(double x0, double x1, double x2) {
        double denominator = x2 - 2 * x1 + x0;
        if (Math.abs(denominator) < 1e-15) return x2;
        return x2 - (x2 - x1) * (x2 - x1) / denominator;
    }

    public static void main(String[] args) {
        assert Math.abs(aitken(1, 0.5, 0.25)) < 1e-12;
        double[] sequence = new double[3];
        for (int n = 0; n < 3; n++) sequence[n] = 2 - 2 * Math.pow(0.5, n);
        assert Math.abs(aitken(sequence[0], sequence[1], sequence[2]) - 2) < 1e-12;
        System.out.println("aitken ok");
    }
}
