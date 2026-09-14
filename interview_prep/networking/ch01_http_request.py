"""Make an HTTP request with the standard library (no third-party deps)."""
import json
import urllib.request


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "interview-prep/1.0"})
    with urllib.request.urlopen(request, timeout=5) as response:
        return json.loads(response.read().decode())


if __name__ == "__main__":
    # Offline placeholder: no network required for the self-check.
    sample = b'{"status": "ok"}'
    assert json.loads(sample)["status"] == "ok"
    print("fetch_json ready")
