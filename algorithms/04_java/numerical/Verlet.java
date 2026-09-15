import java.util.function.DoubleUnaryOperator;

// Velocity Verlet integration.
public class Verlet {
    static double[] verlet(DoubleUnaryOperator acceleration, double x, double v, double dt, int steps) {
        for (int i = 0; i < steps; i++) {
            double a = acceleration.applyAsDouble(x);
            double xNew = x + v * dt + 0.5 * a * dt * dt;
            double aNew = acceleration.applyAsDouble(xNew);
            v = v + 0.5 * (a + aNew) * dt;
            x = xNew;
        }
        return new double[] {x, v};
    }

    public static void main(String[] args) {
        double[] result = verlet(x -> -x, 1, 0, 0.001, 10000);
        double energy = 0.5 * (result[1] * result[1] + result[0] * result[0]);
        assert Math.abs(energy - 0.5) < 1e-3;
        assert Math.abs(result[0] - Math.cos(10)) < 1e-2;
        System.out.println("verlet ok");
    }
}
