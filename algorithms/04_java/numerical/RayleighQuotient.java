// Rayleigh quotient iteration.
public class RayleighQuotient {
    static double[] rayleigh(double[][] matrix, double[] vector) {
        int n = matrix.length;
        double scale = 0;
        for (double value : vector) scale = Math.max(scale, Math.abs(value));
        double[] x = new double[n];
        for (int i = 0; i < n; i++) x[i] = vector[i] / scale;
        double eigenvalue = 0;
        for (int iteration = 0; iteration < 100; iteration++) {
            double[] product = new double[n];
            double norm = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) product[i] += matrix[i][j] * x[j];
                norm = Math.max(norm, Math.abs(product[i]));
            }
            for (int i = 0; i < n; i++) x[i] = product[i] / norm;
            double numerator = 0, denominator = 0;
            for (int i = 0; i < n; i++) {
                double ax = 0;
                for (int j = 0; j < n; j++) ax += matrix[i][j] * x[j];
                numerator += x[i] * ax;
                denominator += x[i] * x[i];
            }
            double next = numerator / denominator;
            if (Math.abs(next - eigenvalue) < 1e-12) { eigenvalue = next; break; }
            eigenvalue = next;
        }
        return new double[] {eigenvalue, x[0], x[1]};
    }

    public static void main(String[] args) {
        double[] result = rayleigh(new double[][] {{2, 1}, {1, 2}}, new double[] {1, 0});
        assert Math.abs(result[0] - 3) < 1e-9;
        System.out.println("rayleigh quotient ok");
    }
}
