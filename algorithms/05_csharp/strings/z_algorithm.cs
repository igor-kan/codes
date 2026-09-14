using System;

namespace Algorithms.Strings
{
    public static class ZAlgorithm
    {
        public static int[] Compute(string s)
        {
            int n = s.Length;
            var z = new int[n];
            int l = 0, r = 0;
            for (int i = 1; i < n; i++)
            {
                if (i <= r) z[i] = Math.Min(r - i + 1, z[i - l]);
                while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
                if (i + z[i] - 1 > r)
                {
                    l = i;
                    r = i + z[i] - 1;
                }
            }
            return z;
        }

        public static void Main()
        {
            int[] z = Compute("ababab");
            bool ok = z[2] == 4 && z[4] == 2;
            Console.WriteLine(ok ? "[C# ZAlgorithm] ... verified" : "[C# ZAlgorithm] ... FAILED");
        }
    }
}
