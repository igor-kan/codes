package math;

/**
 * 1D Kalman Filter in Java (Numerical Recipes 3rd Ed. Chapter 15).
 */
public class KalmanFilter {
    private double x, p, q, r;

    public KalmanFilter(double x0, double p0, double q0, double r0) {
        this.x = x0;
        this.p = p0;
        this.q = q0;
        this.r = r0;
    }

    public void predict() {
        p += q;
    }

    public double update(double z) {
        double k = p / (p + r);
        x += k * (z - x);
        p = (1.0 - k) * p;
        return x;
    }

    public double getX() { return x; }

    public static void main(String[] args) {
        KalmanFilter kf = new KalmanFilter(0, 1, 0.01, 0.1);
        for (double z : new double[]{0.9, 1.1, 0.95, 1.05}) {
            kf.predict();
            kf.update(z);
        }
        assert Math.abs(kf.getX() - 1.0) < 0.2;
        System.out.println("Java Kalman Filter verified.");
    }
}
