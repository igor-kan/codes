//! Base64 encoding.
fn encode(data: &[u8]) -> String {
    const B: &[u8; 64] =
        b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    let mut out = String::new();
    let mut i = 0;
    while i < data.len() {
        let mut v = (data[i] as u32) << 16;
        let rem = data.len() - i;
        if rem > 1 {
            v |= (data[i + 1] as u32) << 8;
        }
        if rem > 2 {
            v |= data[i + 2] as u32;
        }
        out.push(B[((v >> 18) & 63) as usize] as char);
        out.push(B[((v >> 12) & 63) as usize] as char);
        out.push(if rem > 1 { B[((v >> 6) & 63) as usize] as char } else { '=' });
        out.push(if rem > 2 { B[(v & 63) as usize] as char } else { '=' });
        i += 3;
    }
    out
}

fn main() {
    assert_eq!(encode(b"foobar"), "Zm9vYmFy");
    assert_eq!(encode(b"f"), "Zg==");
    println!("base64 ok");
}
