"""
Mnemonic Phonetic Major System and PAO Cipher Encoder.

Maps digits 0-9 to consonant sounds:
0: s, z | 1: t, d | 2: n | 3: m | 4: r | 5: l | 6: j, sh, ch | 7: k, g | 8: f, v | 9: p, b
"""

MAJOR_RULES = {
    "0": ["s", "z"], "1": ["t", "d"], "2": ["n"], "3": ["m"],
    "4": ["r"], "5": ["l"], "6": ["j", "sh", "ch"], "7": ["k", "g"],
    "8": ["f", "v"], "9": ["p", "b"]
}

SAMPLE_PAO_TABLE = {
    "14": ("Albert Einstein", "Writing", "Chalkboard"),
    "15": ("Isaac Newton", "Dropping", "Apple"),
    "27": ("Carl Friedrich Gauss", "Drawing", "Compass"),
    "31": ("David Hilbert", "Sipping", "Beer mug"),
    "41": ("Nikolai Lobachevsky", "Carving", "Hyperbolic saddle")
}

def encode_pao_digits(digits_str: str):
    """Chunk 6-digit string into Person (P), Action (A), Object (O)."""
    assert len(digits_str) == 6, "Expect 6 digits for full PAO scene!"
    p_chunk = digits_str[0:2]
    a_chunk = digits_str[2:4]
    o_chunk = digits_str[4:6]
    
    person = SAMPLE_PAO_TABLE.get(p_chunk, ("Person_" + p_chunk,))[0]
    action = SAMPLE_PAO_TABLE.get(a_chunk, (None, "Action_" + a_chunk))[1]
    obj = SAMPLE_PAO_TABLE.get(o_chunk, (None, None, "Object_" + o_chunk))[2]
    return f"{person} {action} a {obj}"

if __name__ == "__main__":
    print("=== MAJOR SYSTEM PAO CIPHER ===")
    scene = encode_pao_digits("141531")
    print(f"Encoded 14-15-31: {scene}")
