using System;
using System.Text;

namespace Algorithms.Techniques
{
    public static class Base64Codec
    {
        private const string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

        public static string Encode(string data)
        {
            var output = new StringBuilder();
            for (int i = 0; i < data.Length; i += 3)
            {
                int value = data[i] << 16;
                int remaining = data.Length - i;
                if (remaining > 1) value |= data[i + 1] << 8;
                if (remaining > 2) value |= data[i + 2];
                output.Append(Alphabet[(value >> 18) & 63]);
                output.Append(Alphabet[(value >> 12) & 63]);
                output.Append(remaining > 1 ? Alphabet[(value >> 6) & 63] : '=');
                output.Append(remaining > 2 ? Alphabet[value & 63] : '=');
            }
            return output.ToString();
        }

        public static void Main()
        {
            if (Encode("foobar") != "Zm9vYmFy" || Encode("f") != "Zg==")
            {
                throw new InvalidOperationException("bad base64");
            }
            Console.WriteLine("base64 ok");
        }
    }
}
