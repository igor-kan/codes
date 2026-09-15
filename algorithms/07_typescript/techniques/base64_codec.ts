// Base64 encoding.
const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

function encode(data: string): string {
  let out = "";
  for (let i = 0; i < data.length; i += 3) {
    let value = data.charCodeAt(i) << 16;
    const remaining = data.length - i;
    if (remaining > 1) value |= data.charCodeAt(i + 1) << 8;
    if (remaining > 2) value |= data.charCodeAt(i + 2);
    out += ALPHABET[(value >> 18) & 63];
    out += ALPHABET[(value >> 12) & 63];
    out += remaining > 1 ? ALPHABET[(value >> 6) & 63] : "=";
    out += remaining > 2 ? ALPHABET[value & 63] : "=";
  }
  return out;
}

if (encode("foobar") !== "Zm9vYmFy" || encode("f") !== "Zg==") throw new Error("bad base64");
console.log("base64 ok");
