"""Codeforces 71A - Way Too Long Words."""
def way_too_long(word):
    return word if len(word) <= 10 else f"{word[0]}{len(word) - 2}{word[-1]}"


if __name__ == "__main__":
    assert way_too_long("word") == "word"
    assert way_too_long("localization") == "l10n"
    assert way_too_long("internationalization") == "i18n"
    print("71A way too long words ok")
