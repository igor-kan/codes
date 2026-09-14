using System;

namespace Algorithms.Sorting
{
    public static class CountingSort
    {
        public static int[] Sort(int[] array)
        {
            if (array.Length == 0) return array;

            int min = array[0], max = array[0];
            foreach (int x in array)
            {
                if (x < min) min = x;
                if (x > max) max = x;
            }

            int range = max - min + 1;
            var count = new int[range];
            foreach (int x in array) count[x - min]++;

            var result = new int[array.Length];
            int idx = 0;
            for (int i = 0; i < range; i++)
            {
                for (int j = 0; j < count[i]; j++)
                    result[idx++] = i + min;
            }
            return result;
        }

        public static void Main()
        {
            var sorted = Sort(new[] { 4, 2, 2, 8, 3, 3, 1 });
            bool ok = sorted[0] == 1 && sorted[1] == 2 && sorted[2] == 2 && sorted[6] == 8;
            Console.WriteLine(ok ? "[C# CountingSort] ... verified" : "[C# CountingSort] ... FAILED");
        }
    }
}
