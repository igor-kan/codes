using System.Collections.Generic;

namespace Algorithms.Maths
{
    public static class PrimeSieve
    {
        public static List<int> GeneratePrimes(int limit)
        {
            var isPrime = new bool[limit + 1];
            for (int i = 2; i <= limit; i++) isPrime[i] = true;

            for (int p = 2; p * p <= limit; p++)
            {
                if (isPrime[p])
                {
                    for (int i = p * p; i <= limit; i += p)
                        isPrime[i] = false;
                }
            }

            var primes = new List<int>();
            for (int i = 2; i <= limit; i++)
            {
                if (isPrime[i]) primes.Add(i);
            }
            return primes;
        }
    }
}
