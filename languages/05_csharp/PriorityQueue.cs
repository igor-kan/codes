/**
 * Generic Binary Heap Min-Priority Queue.
 * 
 * Why C# for this module?
 * C#'s reified generics (no type erasure unlike Java), structs, and IComparable<T>
 * avoid boxing overhead, providing blistering speed for graph search and discrete event simulations.
 */

using System;
using System.Collections.Generic;

public class PriorityQueue<T> where T : IComparable<T>
{
    private readonly List<T> _heap;

    public PriorityQueue()
    {
        _heap = new List<T>();
    }

    public int Count => _heap.Count;

    public void Enqueue(T item)
    {
        _heap.Add(item);
        HeapifyUp(_heap.Count - 1);
    }

    public T Dequeue()
    {
        if (_heap.Count == 0)
            throw new InvalidOperationException("Priority Queue is empty!");

        T root = _heap[0];
        T last = _heap[_heap.Count - 1];
        _heap.RemoveAt(_heap.Count - 1);

        if (_heap.Count > 0)
        {
            _heap[0] = last;
            HeapifyDown(0);
        }

        return root;
    }

    public T Peek()
    {
        if (_heap.Count == 0)
            throw new InvalidOperationException("Priority Queue is empty!");
        return _heap[0];
    }

    private void HeapifyUp(int index)
    {
        while (index > 0)
        {
            int parent = (index - 1) / 2;
            if (_heap[index].CompareTo(_heap[parent]) < 0)
            {
                Swap(index, parent);
                index = parent;
            }
            else break;
        }
    }

    private void HeapifyDown(int index)
    {
        int count = _heap.Count;
        while (true)
        {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;

            if (left < count && _heap[left].CompareTo(_heap[smallest]) < 0)
                smallest = left;
            if (right < count && _heap[right].CompareTo(_heap[smallest]) < 0)
                smallest = right;

            if (smallest != index)
            {
                Swap(index, smallest);
                index = smallest;
            }
            else break;
        }
    }

    private void Swap(int i, int j)
    {
        T temp = _heap[i];
        _heap[i] = _heap[j];
        _heap[j] = temp;
    }

    public static void Main()
    {
        var pq = new PriorityQueue<int>();
        pq.Enqueue(42);
        pq.Enqueue(15);
        pq.Enqueue(88);
        pq.Enqueue(3);

        Console.WriteLine($"C# Min-Priority Queue Extract: {pq.Dequeue()} (Expect 3)");
        Console.WriteLine($"Next Extract: {pq.Dequeue()} (Expect 15)");
    }
}
