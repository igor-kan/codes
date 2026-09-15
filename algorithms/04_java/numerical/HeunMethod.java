import java.util.function.DoubleBinaryOperator;

// Heun's method for ODEs.
public class HeunMethod {
    static double heunMethod(DoubleBinaryOperator f, double y, double t, double t1, int steps) {
        double h = (t1 - t) / steps;
        for (int i = 0; i < steps; i++) {
            double k1 = f.applyAsDouble(t, y);
            double k2 = f.applyAsDouble(t + h, y + h * k1);
            y += 0.5 * h * (k1 + k2);
            t += h;
        }
        return y;
    }

    public static void main(String[] args) {
        assert Math.abs(heunMethod((t, y) -> y, 1, 0, 1, 1000) - Math.E) < 1e-4;
        System.out.println("heun method ok");
    }
}
