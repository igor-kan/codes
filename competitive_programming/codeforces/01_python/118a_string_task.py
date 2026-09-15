"""Codeforces 118A - String Task."""
def string_task(text):
    vowels = "aeiouy"
    result = []
    for character in text.lower():
        if character not in vowels:
            result.append(".")
            result.append(character)
    return "".join(result)


if __name__ == "__main__":
    assert string_task("Codeforces") == ".c.d.f.r.c.s"
    assert string_task("aBAcAba") == ".b.c.b"
    print("118A string task ok")
