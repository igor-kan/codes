import java.util.function.DoubleUnaryOperator;

// Fixed-point iteration.
public class FixedPoint {
    static double fixedPoint(DoubleUnaryOperator g, double x) {
        for (int i = 0; i < 200; i++) {
            double next = g.applyAsDouble(x);
            if (Math.abs(next - x) < 1e-12) return next;
            x = next;
        }
        return x;
    }

    public static void main(String[] args) {
        assert Math.abs(fixedPoint(x -> 0.5 * (x + 2 / x), 1) - Math.sqrt(2)) < 1e-9;
        System.out.println("fixed point ok");
    }
}
