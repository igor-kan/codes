import java.util.function.DoubleUnaryOperator;

// Regula falsi root finding.
public class RegulaFalsi {
    static double regulaFalsi(DoubleUnaryOperator f, double a, double b) {
        double fa = f.applyAsDouble(a);
        double fb = f.applyAsDouble(b);
        double c = a;
        for (int i = 0; i < 200; i++) {
            c = (a * fb - b * fa) / (fb - fa);
            double fc = f.applyAsDouble(c);
            if (Math.abs(fc) < 1e-12) return c;
            if (fa * fc < 0) { b = c; fb = fc; } else { a = c; fa = fc; }
        }
        return c;
    }

    public static void main(String[] args) {
        assert Math.abs(regulaFalsi(x -> x * x - 2, 0, 2) - Math.sqrt(2)) < 1e-9;
        System.out.println("regula falsi ok");
    }
}
