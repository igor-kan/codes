public final class ClosestPair {
    private ClosestPair() {}

    public static double closest(double[][] pts) {
        double best = Double.MAX_VALUE;
        for (int i = 0; i < pts.length; i++) {
            for (int j = i + 1; j < pts.length; j++) {
                best = Math.min(best, Math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1]));
            }
        }
        return best;
    }

    public static void main(String[] args) {
        double[][] pts = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
        if (Math.abs(closest(pts) - Math.sqrt(2)) > 1e-9) {
            throw new AssertionError("wrong closest distance");
        }
        System.out.println("closest=" + closest(pts));
    }
}
