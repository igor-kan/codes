using System;
using System.Collections.Generic;

namespace Algorithms.DataStructures
{
    public static class MaxHeap
    {
        public static void Main()
        {
            var heap = new List<int>();
            foreach (int value in new[] { 5, 3, 8, 1, 4 })
            {
                Push(heap, value);
            }
            int previous = int.MaxValue;
            while (heap.Count > 0)
            {
                int value = Pop(heap);
                if (value > previous)
                {
                    throw new InvalidOperationException("not a max-heap order");
                }
                previous = value;
            }
            Console.WriteLine("max heap ok");
        }

        public static void Push(List<int> heap, int value)
        {
            heap.Add(value);
            int i = heap.Count - 1;
            while (i > 0)
            {
                int parent = (i - 1) / 2;
                if (heap[parent] >= heap[i])
                {
                    break;
                }
                (heap[parent], heap[i]) = (heap[i], heap[parent]);
                i = parent;
            }
        }

        public static int Pop(List<int> heap)
        {
            int top = heap[0];
            int last = heap[heap.Count - 1];
            heap.RemoveAt(heap.Count - 1);
            if (heap.Count > 0)
            {
                heap[0] = last;
                int i = 0;
                while (true)
                {
                    int left = 2 * i + 1, right = 2 * i + 2, best = i;
                    if (left < heap.Count && heap[left] > heap[best]) best = left;
                    if (right < heap.Count && heap[right] > heap[best]) best = right;
                    if (best == i) break;
                    (heap[i], heap[best]) = (heap[best], heap[i]);
                    i = best;
                }
            }
            return top;
        }
    }
}
