package math;

import java.util.function.DoubleUnaryOperator;

/**
 * Brent's Root Finding in Java (Numerical Recipes 3rd Ed. Chapter 9.3).
 */
public class BrentRoot {
    public static double findRoot(DoubleUnaryOperator f, double a, double b, double tol, int maxIter) {
        double fa = f.applyAsDouble(a);
        double fb = f.applyAsDouble(b);
        if (fa * fb > 0) throw new IllegalArgumentException("Root not bracketed");

        if (Math.abs(fa) < Math.abs(fb)) {
            double t = a; a = b; b = t;
            t = fa; fa = fb; fb = t;
        }

        double c = a, fc = fa, d = 0, s = b;
        boolean mflag = true;

        for (int iter = 0; iter < maxIter; iter++) {
            if (Math.abs(fb) < tol || Math.abs(b - a) < tol) return b;

            if (fa != fc && fb != fc) {
                s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                    (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                    (c * fa * fb) / ((fc - fa) * (fc - fb));
            } else {
                s = b - fb * (b - a) / (fb - fa);
            }

            boolean c1 = (s - (3 * a + b) / 4) * (s - b) > 0;
            boolean c2 = mflag && Math.abs(s - b) >= Math.abs(b - c) / 2;
            boolean c3 = !mflag && Math.abs(s - b) >= Math.abs(c - d) / 2;

            if (c1 || c2 || c3) {
                s = (a + b) / 2;
                mflag = true;
            } else {
                mflag = false;
            }

            double fs = f.applyAsDouble(s);
            d = c; c = b; fc = fb;
            if (fa * fs < 0) { b = s; fb = fs; }
            else { a = s; fa = fs; }

            if (Math.abs(fa) < Math.abs(fb)) {
                double t = a; a = b; b = t;
                t = fa; fa = fb; fb = t;
            }
        }
        return b;
    }

    public static void main(String[] args) {
        double r = findRoot(x -> x * x - 2.0, 0, 2, 1e-10, 100);
        assert Math.abs(r - Math.sqrt(2.0)) < 1e-6;
        System.out.println("Java Brent Root Finding verified.");
    }
}
