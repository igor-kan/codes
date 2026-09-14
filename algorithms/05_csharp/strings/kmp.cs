using System.Collections.Generic;

namespace Algorithms.Strings
{
    public static class KnuthMorrisPratt
    {
        public static List<int> Search(string text, string pattern)
        {
            var matches = new List<int>();
            if (string.IsNullOrEmpty(pattern) || string.IsNullOrEmpty(text))
                return matches;

            int[] lps = BuildLps(pattern);
            int i = 0, j = 0;

            while (i < text.Length)
            {
                if (text[i] == pattern[j])
                {
                    i++;
                    j++;
                }

                if (j == pattern.Length)
                {
                    matches.Add(i - j);
                    j = lps[j - 1];
                }
                else if (i < text.Length && text[i] != pattern[j])
                {
                    j = j > 0 ? lps[j - 1] : 0;
                    if (j == 0) i++;
                }
            }

            return matches;
        }

        private static int[] BuildLps(string pattern)
        {
            int[] lps = new int[pattern.Length];
            int length = 0;
            int i = 1;

            while (i < pattern.Length)
            {
                if (pattern[i] == pattern[length])
                {
                    length++;
                    lps[i++] = length;
                }
                else if (length != 0)
                {
                    length = lps[length - 1];
                }
                else
                {
                    lps[i++] = 0;
                }
            }

            return lps;
        }
    }
}
