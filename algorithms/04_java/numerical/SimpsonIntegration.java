import java.util.function.DoubleUnaryOperator;

// Composite Simpson's rule (Numerical Recipes 4.1).
public class SimpsonIntegration {
    static double simpson(DoubleUnaryOperator f, double a, double b, int n) {
        if (n % 2 == 1) n++;
        double h = (b - a) / n;
        double total = f.applyAsDouble(a) + f.applyAsDouble(b);
        for (int i = 1; i < n; i++) total += (i % 2 == 1 ? 4.0 : 2.0) * f.applyAsDouble(a + i * h);
        return total * h / 3.0;
    }

    public static void main(String[] args) {
        assert Math.abs(simpson(v -> v * v, 0, 1, 1000) - 1.0 / 3) < 1e-12;
        System.out.println("simpson integration ok");
    }
}
