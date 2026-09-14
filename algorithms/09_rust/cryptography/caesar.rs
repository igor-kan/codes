pub fn encrypt(text: &str, shift: u8) -> String {
    text.chars()
        .map(|c| {
            if c.is_ascii_alphabetic() {
                let first = if c.is_ascii_lowercase() { b'a' } else { b'A' };
                (first + (c as u8 - first + shift) % 26) as char
            } else {
                c
            }
        })
        .collect()
}

pub fn decrypt(text: &str, shift: u8) -> String {
    encrypt(text, 26 - (shift % 26))
}
