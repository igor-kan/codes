import java.util.function.DoubleBinaryOperator;

// Forward Euler method for ODEs.
public class EulerMethod {
    static double eulerMethod(DoubleBinaryOperator f, double y, double t, double t1, int steps) {
        double h = (t1 - t) / steps;
        for (int i = 0; i < steps; i++) { y += h * f.applyAsDouble(t, y); t += h; }
        return y;
    }

    public static void main(String[] args) {
        assert Math.abs(eulerMethod((t, y) -> y, 1, 0, 1, 1000) - Math.E) < 0.01;
        System.out.println("euler method ok");
    }
}
