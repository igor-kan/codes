import java.util.function.DoubleUnaryOperator;

// Monte Carlo integration.
public class MonteCarloIntegration {
    static double monteCarlo(DoubleUnaryOperator f, double a, double b, int samples) {
        long state = 42;
        long modulus = 1L << 31;
        double total = 0;
        for (int i = 0; i < samples; i++) {
            state = (1103515245L * state + 12345) % modulus;
            total += f.applyAsDouble(a + (b - a) * (double) state / (double) modulus);
        }
        return (b - a) * total / samples;
    }

    public static void main(String[] args) {
        assert Math.abs(monteCarlo(x -> x * x, 0, 1, 100000) - 1.0 / 3.0) < 0.01;
        System.out.println("monte carlo integration ok");
    }
}
