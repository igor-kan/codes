using System;

namespace Algorithms.Geometry
{
    public static class ClosestPair
    {
        public static double Closest(double[][] points)
        {
            double best = double.MaxValue;
            for (int i = 0; i < points.Length; i++)
            {
                for (int j = i + 1; j < points.Length; j++)
                {
                    best = Math.Min(best, Math.Sqrt(
                        Math.Pow(points[i][0] - points[j][0], 2) + Math.Pow(points[i][1] - points[j][1], 2)));
                }
            }
            return best;
        }

        public static void Main()
        {
            var points = new[] { new[] { 2.0, 3.0 }, new[] { 12.0, 30.0 }, new[] { 40.0, 50.0 }, new[] { 5.0, 1.0 }, new[] { 12.0, 10.0 }, new[] { 3.0, 4.0 } };
            if (Math.Abs(Closest(points) - Math.Sqrt(2.0)) > 1e-9)
            {
                throw new InvalidOperationException("wrong closest distance");
            }
            Console.WriteLine($"closest={Closest(points)}");
        }
    }
}
