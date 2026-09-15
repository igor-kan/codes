"""Fail Fast: reject work immediately when the system is unhealthy."""
class FailFast:
    def __init__(self) -> None:
        self.healthy = True

    def handle(self, request: dict) -> dict | None:
        if not self.healthy:
            return None  # reject without doing work
        return {"status": "ok", "request": request}


if __name__ == "__main__":
    service = FailFast()
    assert service.handle({"id": 1}) is not None
    service.healthy = False
    assert service.handle({"id": 2}) is None
    print("fail fast ok")
