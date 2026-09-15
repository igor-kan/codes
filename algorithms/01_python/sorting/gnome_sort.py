"""Gnome sort: adjacent-swap insertion sort."""
def gnome_sort(a: list) -> list:
    a = list(a)
    i = 0
    while i < len(a):
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
    return a


if __name__ == "__main__":
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    assert gnome_sort(data) == sorted(data)
    print("gnome sort ok")
