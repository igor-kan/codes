import java.util.function.DoubleUnaryOperator;

// Bisection root finding.
public class Bisection {
    static double bisection(DoubleUnaryOperator f, double a, double b) {
        double fa = f.applyAsDouble(a);
        for (int i = 0; i < 200; i++) {
            double c = 0.5 * (a + b);
            double fc = f.applyAsDouble(c);
            if (fc == 0 || (b - a) / 2 < 1e-12) return c;
            if (fa * fc < 0) b = c; else { a = c; fa = fc; }
        }
        return 0.5 * (a + b);
    }

    public static void main(String[] args) {
        assert Math.abs(bisection(x -> x * x - 2, 0, 2) - Math.sqrt(2)) < 1e-9;
        System.out.println("bisection ok");
    }
}
