import java.util.function.DoubleUnaryOperator;

// Steffensen's method.
public class Steffensen {
    static double steffensen(DoubleUnaryOperator g, double x) {
        for (int i = 0; i < 100; i++) {
            double x1 = g.applyAsDouble(x);
            double x2 = g.applyAsDouble(x1);
            double denominator = x2 - 2 * x1 + x;
            if (Math.abs(denominator) < 1e-15) return x2;
            double next = x - (x1 - x) * (x1 - x) / denominator;
            if (Math.abs(next - x) < 1e-12) return next;
            x = next;
        }
        return x;
    }

    public static void main(String[] args) {
        assert Math.abs(steffensen(x -> 0.5 * (x + 2 / x), 1) - Math.sqrt(2)) < 1e-12;
        System.out.println("steffensen ok");
    }
}
