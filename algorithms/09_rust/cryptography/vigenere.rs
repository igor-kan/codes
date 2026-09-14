pub fn encrypt(text: &str, key: &str) -> String {
    let key_bytes = key.as_bytes();
    let mut key_idx = 0;

    text.chars()
        .map(|c| {
            if c.is_ascii_alphabetic() {
                let first = if c.is_ascii_lowercase() { b'a' } else { b'A' };
                let shift = (key_bytes[key_idx % key.len()].to_ascii_lowercase() - b'a') % 26;
                key_idx += 1;
                (first + (c as u8 - first + shift) % 26) as char
            } else {
                c
            }
        })
        .collect()
}
