using System;

namespace Algorithms.Math
{
    public static class GaussianElimination
    {
        public static double[] Solve(double[,] matrix, double[] rhs)
        {
            int n = matrix.GetLength(0);
            var a = new double[n, n + 1];
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++) a[i, j] = matrix[i, j];
                a[i, n] = rhs[i];
            }
            for (int c = 0; c < n; c++)
            {
                int pivot = c;
                for (int r = c + 1; r < n; r++)
                {
                    if (Math.Abs(a[r, c]) > Math.Abs(a[pivot, c])) pivot = r;
                }
                for (int k = 0; k <= n; k++)
                {
                    (a[c, k], a[pivot, k]) = (a[pivot, k], a[c, k]);
                }
                for (int r = c + 1; r < n; r++)
                {
                    double factor = a[r, c] / a[c, c];
                    for (int k = c; k <= n; k++) a[r, k] -= factor * a[c, k];
                }
            }
            var x = new double[n];
            for (int r = n - 1; r >= 0; r--)
            {
                double sum = a[r, n];
                for (int k = r + 1; k < n; k++) sum -= a[r, k] * x[k];
                x[r] = sum / a[r, r];
            }
            return x;
        }

        public static void Main()
        {
            var x = Solve(new double[,] { { 2, 1, -1 }, { -3, -1, 2 }, { -2, 1, 2 } }, new[] { 8.0, -11, -3 });
            if (Math.Abs(x[0] - 2) > 1e-9 || Math.Abs(x[1] - 3) > 1e-9 || Math.Abs(x[2] + 1) > 1e-9)
            {
                throw new InvalidOperationException("wrong solution");
            }
            Console.WriteLine($"x={x[0]} {x[1]} {x[2]}");
        }
    }
}
