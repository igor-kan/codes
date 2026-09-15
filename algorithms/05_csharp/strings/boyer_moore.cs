using System;

namespace Algorithms.Strings
{
    public static class BoyerMoore
    {
        public static int Search(string text, string pattern)
        {
            int n = text.Length, m = pattern.Length;
            var skip = new int[256];
            for (int i = 0; i < 256; i++) skip[i] = m;
            for (int i = 0; i < m - 1; i++) skip[pattern[i]] = m - 1 - i;
            int pos = 0;
            while (pos + m <= n)
            {
                int j = m - 1;
                while (j >= 0 && text[pos + j] == pattern[j]) j--;
                if (j < 0) return pos;
                pos += skip[text[pos + m - 1]];
            }
            return -1;
        }

        public static void Main()
        {
            if (Search("here is a simple example", "example") != 17 || Search("abc", "xyz") != -1)
            {
                throw new InvalidOperationException("search failed");
            }
            Console.WriteLine("boyer-moore ok");
        }
    }
}
