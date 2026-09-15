"""Identity Map: one object instance per row identity."""
class IdentityMap:
    def __init__(self) -> None:
        self._objects: dict[tuple[type, int], object] = {}

    def get(self, entity_type, identity: int, loader):
        key = (entity_type, identity)
        if key not in self._objects:
            self._objects[key] = loader(identity)
        return self._objects[key]


if __name__ == "__main__":
    loads = []

    def loader(identity: int) -> dict:
        loads.append(identity)
        return {"id": identity, "name": f"user-{identity}"}

    identity_map = IdentityMap()
    first = identity_map.get(dict, 1, loader)
    second = identity_map.get(dict, 1, loader)
    assert first is second and loads == [1]
    print("identity map ok")
