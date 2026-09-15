using System;

namespace Algorithms.DataStructures
{
    public class CircularBuffer
    {
        private readonly int[] _data;
        private int _head;
        private int _size;

        public CircularBuffer(int capacity)
        {
            _data = new int[capacity];
        }

        public int Count => _size;

        public void Push(int value)
        {
            _data[(_head + _size) % _data.Length] = value;
            if (_size < _data.Length)
            {
                _size++;
            }
            else
            {
                _head = (_head + 1) % _data.Length;
            }
        }

        public int Pop()
        {
            int value = _data[_head];
            _head = (_head + 1) % _data.Length;
            _size--;
            return value;
        }

        public static void Main()
        {
            var buffer = new CircularBuffer(3);
            for (int i = 1; i <= 4; i++)
            {
                buffer.Push(i);
            }
            if (buffer.Pop() != 2 || buffer.Pop() != 3 || buffer.Pop() != 4)
            {
                throw new InvalidOperationException("bad overwrite semantics");
            }
            Console.WriteLine("circular buffer ok");
        }
    }
}
