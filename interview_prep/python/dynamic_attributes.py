"""__getattr__, __setattr__ and __slots__."""
import logging


class LazyConfig:
    def __init__(self, defaults: dict) -> None:
        object.__setattr__(self, "_data", dict(defaults))

    def __getattr__(self, name: str):
        try:
            return object.__getattribute__(self, "_data")[name]
        except KeyError as exc:
            raise AttributeError(name) from exc

    def __setattr__(self, name: str, value) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self._data[name] = value


class Slotted:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y


if __name__ == "__main__":
    config = LazyConfig({"debug": True})
    assert config.debug is True
    config.port = 8080
    assert config.port == 8080
    s = Slotted(1, 2)
    try:
        s.z = 3
    except AttributeError:
        pass
    else:
        raise AssertionError("slots should block new attributes")
    print("ok")
