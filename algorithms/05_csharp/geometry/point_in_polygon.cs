using System;

namespace Algorithms.Geometry
{
    public static class PointInPolygon
    {
        public static bool Inside(double[][] polygon, double px, double py)
        {
            bool inside = false;
            int n = polygon.Length;
            for (int i = 0, j = n - 1; i < n; j = i++)
            {
                double xi = polygon[i][0], yi = polygon[i][1];
                double xj = polygon[j][0], yj = polygon[j][1];
                if ((yi > py) != (yj > py) && px < (xj - xi) * (py - yi) / (yj - yi) + xi)
                {
                    inside = !inside;
                }
            }
            return inside;
        }

        public static void Main()
        {
            var square = new[] { new[] { 0.0, 0.0 }, new[] { 4.0, 0.0 }, new[] { 4.0, 4.0 }, new[] { 0.0, 4.0 } };
            if (!Inside(square, 2, 2) || Inside(square, 5, 5))
            {
                throw new InvalidOperationException("ray casting failed");
            }
            Console.WriteLine("point in polygon ok");
        }
    }
}
