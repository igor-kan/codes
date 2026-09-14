"""The mutable default argument pitfall."""


def bad_append(item, target=[]):        # noqa: B006 -- intentional demo
    target.append(item)
    return target


def good_append(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target


if __name__ == "__main__":
    assert bad_append(1) == [1]
    assert bad_append(2) == [1, 2]        # shared state!
    assert good_append(1) == [1]
    assert good_append(2) == [2]          # isolated
    print("ok")
