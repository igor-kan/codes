public final class Base64Codec {
    private static final String ALPHABET =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    private Base64Codec() {}

    public static String encode(byte[] data) {
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < data.length; i += 3) {
            int v = (data[i] & 0xFF) << 16;
            int rem = data.length - i;
            if (rem > 1) {
                v |= (data[i + 1] & 0xFF) << 8;
            }
            if (rem > 2) {
                v |= data[i + 2] & 0xFF;
            }
            out.append(ALPHABET.charAt((v >> 18) & 63));
            out.append(ALPHABET.charAt((v >> 12) & 63));
            out.append(rem > 1 ? ALPHABET.charAt((v >> 6) & 63) : '=');
            out.append(rem > 2 ? ALPHABET.charAt(v & 63) : '=');
        }
        return out.toString();
    }

    public static void main(String[] args) {
        if (!encode("foobar".getBytes()).equals("Zm9vYmFy") || !encode("f".getBytes()).equals("Zg==")) {
            throw new AssertionError("bad base64");
        }
        System.out.println("base64 ok");
    }
}
