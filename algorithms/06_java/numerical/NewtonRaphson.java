import java.util.function.DoubleUnaryOperator;

// Newton-Raphson root finding (Numerical Recipes 9.4).
public class NewtonRaphson {
    static double newton(DoubleUnaryOperator f, DoubleUnaryOperator df, double x) {
        for (int i = 0; i < 100; i++) {
            double fx = f.applyAsDouble(x);
            if (Math.abs(fx) < 1e-12) break;
            x -= fx / df.applyAsDouble(x);
        }
        return x;
    }

    public static void main(String[] args) {
        double root = newton(v -> v * v - 2, v -> 2 * v, 1.0);
        assert Math.abs(root - Math.sqrt(2.0)) < 1e-9;
        System.out.println("newton-raphson ok");
    }
}
