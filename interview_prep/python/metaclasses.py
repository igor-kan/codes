"""Metaclasses and __init_subclass__."""


class Registered(type):
    registry: dict[str, type] = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "Base":
            mcls.registry[name] = cls
        return cls


class Base(metaclass=Registered):
    def handle(self) -> str:
        return "base"


class JsonHandler(Base):
    def handle(self) -> str:
        return "json"


class Plugin:
    plugins: list[type] = []

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        Plugin.plugins.append(cls)


class AuthPlugin(Plugin):
    pass


if __name__ == "__main__":
    assert Registered.registry["JsonHandler"] is JsonHandler
    assert JsonHandler().handle() == "json"
    assert AuthPlugin in Plugin.plugins
    print("ok")
