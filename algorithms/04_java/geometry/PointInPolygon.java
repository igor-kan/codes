public final class PointInPolygon {
    private PointInPolygon() {}

    public static boolean inside(double[][] poly, double px, double py) {
        boolean in = false;
        int n = poly.length;
        for (int i = 0, j = n - 1; i < n; j = i++) {
            double xi = poly[i][0], yi = poly[i][1];
            double xj = poly[j][0], yj = poly[j][1];
            if (((yi > py) != (yj > py)) && (px < (xj - xi) * (py - yi) / (yj - yi) + xi)) {
                in = !in;
            }
        }
        return in;
    }

    public static void main(String[] args) {
        double[][] square = {{0, 0}, {4, 0}, {4, 4}, {0, 4}};
        if (!inside(square, 2, 2) || inside(square, 5, 5)) {
            throw new AssertionError("ray casting failed");
        }
        System.out.println("point in polygon ok");
    }
}
