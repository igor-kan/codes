using System;

namespace Algorithms.Strings
{
    public static class Manacher
    {
        public static int[] OddRadii(string s)
        {
            int n = s.Length;
            var d = new int[n];
            int l = 0, r = -1;
            for (int i = 0; i < n; i++)
            {
                int k = i > r ? 1 : Math.Min(d[l + r - i], r - i + 1);
                while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) k++;
                d[i] = k--;
                if (i + k > r)
                {
                    l = i - k;
                    r = i + k;
                }
            }
            return d;
        }

        public static int[] EvenRadii(string s)
        {
            int n = s.Length;
            var d = new int[n];
            int l = 0, r = -1;
            for (int i = 0; i < n; i++)
            {
                int k = i > r ? 0 : Math.Min(d[l + r - i + 1], r - i + 1);
                while (i - k - 1 >= 0 && i + k < n && s[i - k - 1] == s[i + k]) k++;
                d[i] = k--;
                if (i + k > r)
                {
                    l = i - k - 1;
                    r = i + k;
                }
            }
            return d;
        }

        public static string LongestPalindrome(string s)
        {
            if (s.Length == 0) return string.Empty;
            int bestLen = 0, bestStart = 0;

            int[] odd = OddRadii(s);
            for (int i = 0; i < s.Length; i++)
            {
                int len = 2 * odd[i] - 1;
                if (len > bestLen)
                {
                    bestLen = len;
                    bestStart = i - odd[i] + 1;
                }
            }

            int[] even = EvenRadii(s);
            for (int i = 0; i < s.Length; i++)
            {
                int len = 2 * even[i];
                if (len > bestLen)
                {
                    bestLen = len;
                    bestStart = i - even[i];
                }
            }

            return s.Substring(bestStart, bestLen);
        }

        public static void Main()
        {
            bool ok = LongestPalindrome("babad").Length == 3 && LongestPalindrome("abba").Length == 4;
            Console.WriteLine(ok ? "[C# Manacher] ... verified" : "[C# Manacher] ... FAILED");
        }
    }
}
