"""Fallback: return a degraded response when the primary fails."""
def with_fallback(primary, fallback):
    try:
        return primary()
    except Exception:  # noqa: BLE001
        return fallback()


if __name__ == "__main__":
    def broken():
        raise ConnectionError("down")

    assert with_fallback(broken, lambda: "cached") == "cached"
    assert with_fallback(lambda: "live", lambda: "cached") == "live"
    print("fallback ok")
